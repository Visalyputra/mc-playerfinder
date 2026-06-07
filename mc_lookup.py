import requests
import re
import base64
import json

def is_uuid(text: str) -> bool:
    """Check if input looks like a UUID"""
    clean = re.sub(r'[^0-9a-fA-F]', '', text.lower())
    return len(clean) == 32

def format_uuid(uuid: str) -> str:
    """Format UUID with hyphens for better readability"""
    clean = uuid.replace("-", "").lower()
    if len(clean) == 32:
        return f"{clean[0:8]}-{clean[8:12]}-{clean[12:16]}-{clean[16:20]}-{clean[20:32]}"
    return uuid


KNOWN_CAPES = {
    "OptiFine Cape":     "optifine",
    "MineCon 2011":      "c2edc0",
    "MineCon 2012":      "a2536a",
    "MineCon 2013":      "0571b0",
    "MineCon 2015":      "5d963b",
    "MineCon 2016":      "b06c71",
    "Migrator Cape":     "migrator",
    "Vanilla Cape":      "vanilla",
    "Cherry Blossom":    "cherry",
    "Cobalt":            "cobalt",
    "Mojang Classic":    "mojangfirst",
    "Realms Mapmaker":   "mapmaker",
}

def decode_cape_info(properties: list) -> dict | None:
    """Decode the textures property from a Mojang profile and extract cape info."""
    for prop in properties:
        if prop.get("name") == "textures":
            try:
                decoded = base64.b64decode(prop["value"]).decode("utf-8")
                texture_data = json.loads(decoded)
                textures = texture_data.get("textures", {})
                cape = textures.get("CAPE")
                skin = textures.get("SKIN")
                return {
                    "cape_url": cape.get("url") if cape else None,
                    "skin_url": skin.get("url") if skin else None,
                }
            except Exception:
                pass
    return None


def identify_cape(cape_url: str) -> str:
    """Try to match a cape URL to a known cape name."""
    url_lower = cape_url.lower()
    for name, keyword in KNOWN_CAPES.items():
        if keyword in url_lower:
            return name
    return "Unknown / Custom Cape"


def print_cape_info(properties: list):
    """Print cape collection status for a Java player."""
    info = decode_cape_info(properties)
    if info is None:
        print("🎭 Cape    : Unable to decode texture data")
        return

    if info["cape_url"]:
        cape_name = identify_cape(info["cape_url"])
        print(f"🎭 Cape    : ✅ Has a cape! ({cape_name})")
        print(f"   Cape URL: {info['cape_url']}")
    else:
        print("🎭 Cape    : ❌ No cape equipped")


def lookup_player(input_str: str):
    input_str = input_str.strip()
    print(f"\n🔍 Looking up: {input_str}")

    if is_uuid(input_str):
        # UUID Mode
        clean_uuid = input_str.replace("-", "").lower()
        print("Detected: UUID format")

        # Try Java first
        try:
            mojang_url = f"https://sessionserver.mojang.com/session/minecraft/profile/{clean_uuid}"
            r = requests.get(mojang_url, timeout=10)
            if r.status_code == 200:
                data = r.json()
                name = data.get("name")
                properties = data.get("properties", [])
                print(f"✅ **Java Edition**")
                print(f"Username : {name}")
                print(f"UUID     : {format_uuid(clean_uuid)}")
                print_cape_info(properties)
                return
        except:
            pass

        # Try Bedrock
        print("Not found as Java player. Checking Bedrock...")
        xuid = clean_uuid[16:] if clean_uuid.startswith("0000000000000000") else clean_uuid
        get_bedrock_gamertag(xuid)

    else:
        # Username / Gamertag Mode
        print("Detected: Username / Gamertag format")
        username = input_str

        # Try Java first
        try:
            java_url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
            r = requests.get(java_url, timeout=10)
            if r.status_code == 200:
                data = r.json()
                uuid = data.get("id")
                name = data.get("name")
                print(f"✅ **Java Edition**")
                print(f"Username : {name}")
                print(f"UUID     : {format_uuid(uuid)}")
                # Fetch full profile to get cape/texture data
                try:
                    profile_url = f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid}"
                    pr = requests.get(profile_url, timeout=10)
                    if pr.status_code == 200:
                        properties = pr.json().get("properties", [])
                        print_cape_info(properties)
                    else:
                        print("🎭 Cape    : Unable to fetch profile for cape data")
                except Exception:
                    print("🎭 Cape    : Unable to fetch profile for cape data")
                return
            elif r.status_code in (204, 404):
                print("Not found as Java player. Checking Bedrock...")
        except:
            pass

        # Try Bedrock
        get_bedrock_xuid_and_gamertag(username)


def get_bedrock_gamertag(xuid: str):
    url = f"https://api.geysermc.org/v2/xbox/gamertag/{xuid}"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            gamertag = data.get("gamertag")
            if gamertag:
                print(f"✅ **Bedrock Edition**")
                print(f"Gamertag : {gamertag}")
                print(f"XUID     : {xuid}")
                print(f"🎭 Cape    : ⚠️  Cape detection not available for Bedrock Edition")
                return
    except:
        pass
    print("❌ Could not find Bedrock player with this XUID.")


def get_bedrock_xuid_and_gamertag(gamertag: str):
    url = f"https://api.geysermc.org/v2/xbox/xuid/{gamertag}"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            xuid = data.get("xuid")
            if xuid:
                print(f"✅ **Bedrock Edition**")
                print(f"Gamertag : {gamertag}")
                print(f"XUID     : {xuid}")
                bedrock_uuid = f"00000000-0000-0000-{xuid[0:4]}-{xuid[4:16]}"
                print(f"UUID     : {bedrock_uuid} (Floodgate style)")
                print(f"🎭 Cape    : ⚠️  Cape detection not available for Bedrock Edition")
                return
    except:
        pass
    print("❌ Could not find Bedrock player with this Gamertag.")


# ========================
# Main Program
# ========================

if __name__ == "__main__":
    print("🎮 Minecraft Player Lookup Tool (UUID or IGN)")
    print("   Supports Java Edition & Bedrock Edition")
    print("=" * 65)
    
    # Credits
    print("   Coded by Visalyputra using Grok AI")
    print("=" * 65)

    while True:
        user_input = input("\nEnter UUID or Username (or 'quit' to exit): ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Goodbye! Happy gaming!")
            break
            
        if user_input:
            lookup_player(user_input)
