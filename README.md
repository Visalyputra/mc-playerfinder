# Minecraft Player Lookup Tool

A simple and easy-to-use Python script that allows you to look up Minecraft players by entering either their UUID or their Username/Gamertag.

It automatically detects whether the player is on Java Edition or Bedrock Edition and displays the correct information.

# 📋 Changelog

All notable changes to `mc_lookup.py` will be documented here.

---

## [v1.3.0] - 2026-10-03

### ✨ Added
- **Expanded cape detection for modern Mojang cape families**
  - Added support for newer cape naming patterns, including Minecraft Dungeons and Dungeons II promo-style URLs
  - Added generic fallback matching for new cape families that do not match the older hardcoded list
  - Improved detection priority so Dungeons II and promo variants are recognized before generic matches

### 🔧 Updated
- Updated the `KNOWN_CAPES` dictionary to include newer cape labels such as:
  - `Dungeons Cape`
  - `Dungeons II Cape`
  - `Dungeons II Promo Cape`
  - `Adventure Cape`
  - `Promo Cape`
  - `Pride Cape`
  - `Winter Cape`
  - `Festival Cape`
  - `Birthday Cape`
  - `Creator Cape`
- Improved the `identify_cape()` logic to detect cape URLs built from modern naming conventions like:
  - `dungeons-ii`
  - `dungeons2`
  - `minecraft-dungeons-ii`
  - `promo`

### 🐛 Fixed
- Unknown or newer cape URLs are no longer limited to a generic `Unknown / Custom Cape` label when they clearly match a known modern cape family.
- Cape detection is now more resilient to variations in Mojang texture URL naming.

---

## [v1.2.0] - 2025-06-07

### ✨ Added
- **Cape detection** for Java Edition players
  - Decodes Mojang's base64 texture payload to check for active cape
  - Identifies known capes by name (see full list below)
  - Displays direct cape texture URL for verification
  - Shows `⚠️ Not available` notice for Bedrock Edition players

### 🎭 Recognized Capes
| Cape Name | Source |
|---|---|
| MineCon 2011 | Minecon Event |
| MineCon 2012 | Minecon Event |
| MineCon 2013 | Minecon Event |
| MineCon 2015 | Minecon Event |
| MineCon 2016 | Minecon Event |
| Migrator Cape | Java Account Migration |
| Vanilla Cape | Vanilla Anniversary |
| Cherry Blossom | Limited Event |
| Cobalt | Mojang x Cobalt |
| OptiFine Cape | OptiFine Mod Donation |
| Mojang Classic | Mojang Staff / Early Access |
| Realms Mapmaker | Realms Content Creator |
| Dungeons Cape | Minecraft Dungeons |
| Dungeons II Cape | Minecraft Dungeons II |
| Dungeons II Promo Cape | Minecraft Dungeons II promo |

> Unknown or unlisted capes are shown as `Unknown / Custom Cape`

---

## [v1.1.0] - 2025-06-07

### ✨ Added
- **Bedrock Edition support** via GeyserMC API
  - XUID lookup from Gamertag
  - Gamertag lookup from XUID
  - Floodgate-style UUID display for Bedrock players
- Auto-detection of UUID vs username/gamertag input format
- Fallback: if not found on Java, automatically checks Bedrock

---

## [v1.0.0] - 2025-06-07

### 🚀 Initial Release
- **Java Edition** player lookup via Mojang API
  - Username → UUID resolution
  - UUID → Username resolution
- UUID formatting with hyphens for readability
- Interactive CLI loop with `quit`/`exit`/`q` to stop

### Features

- Lookup by **UUID** (Java or Bedrock)
- Lookup by **Username** (Java) or **Gamertag** (Bedrock)
- Automatically detects Java or Bedrock Edition
- For Bedrock players: Shows Gamertag and XUID
- For Java players: Shows Username and UUID
- Clean and user-friendly interactive interface
- No installation of extra packages required (only `requests`)

### What is this tool used for?

This tool is perfect for:
- Finding your friends' current Minecraft usernames from their UUID
- Checking if a player is on Java or Bedrock Edition
- Looking up Bedrock Gamertags from XUIDs (especially useful for GeyserMC/Floodgate servers)
- Quickly verifying player identities without opening Minecraft or using multiple websites

### How to Use

1. **Save the script** as `mc_lookup.py`

2. **Run the script** using Python:
   ```bash
   python mc_lookup.py
   ```

3. **Enter either**:
   - A Java UUID
   - A Minecraft username
   - A Bedrock gamertag

4. The tool will automatically detect the platform and display the result

---

## Recent Script Update Summary

The latest update improves cape recognition for modern Minecraft promotions and event-based cape textures.

This is especially useful for identifying players who have:
- Minecraft Dungeons capes
- Minecraft Dungeons II promo capes
- newer Mojang event capes that use modern naming patterns in their texture URLs

The script now checks for both legacy and modern cape naming conventions, making it more future-proof and accurate when identifying player cosmetics.
