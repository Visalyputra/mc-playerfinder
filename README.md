# Minecraft Player Lookup Tool

A simple and easy-to-use Python script that allows you to look up Minecraft players by entering **either their UUID or their Username/Gamertag**.

It automatically detects whether the player is on **Java Edition** or **Bedrock Edition** and displays the correct information.

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
