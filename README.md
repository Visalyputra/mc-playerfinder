# Minecraft Player Lookup Tool

A simple and easy-to-use Python script that allows you to look up Minecraft players by entering **either their UUID or their Username/Gamertag**.

It automatically detects whether the player is on **Java Edition** or **Bedrock Edition** and displays the correct information. 

# 📋 Changelog

All notable changes to **mc_lookup.py** will be documented here.

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
