import requests
import re
from urllib.parse import urlparse  # extra safety (not strictly needed here)

def is_uuid(text: str) -> bool:
    """Improved UUID validation"""
    if not text:
        return False
    # Remove all non-hex characters and check length
    clean = re.sub(r'[^0-9a-fA-F]', '', text.lower())
    return len(clean) == 32

def safe_get(url: str, timeout: int = 10):
    """Wrapper to add extra safety (optional)"""
    # Optional: extra check that we're only calling allowed domains
    allowed_domains = {
        "sessionserver.mojang.com",
        "api.mojang.com",
        "api.geysermc.org"
    }
    parsed = urlparse(url)
    if parsed.netloc not in allowed_domains:
        raise ValueError("Attempted to call unauthorized domain")
    
    return requests.get(url, timeout=timeout, headers={"User-Agent": "MinecraftLookupTool/1.0"})
