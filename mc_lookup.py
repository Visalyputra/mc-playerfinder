import requests
import re

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
                print(f"✅ **Java Edition**")
                print(f"Username : {name}")
                print(f"UUID     : {format_uuid(clean_uuid)}")
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
