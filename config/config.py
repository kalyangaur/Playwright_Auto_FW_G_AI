import json
import os
from pathlib import Path
from typing import Dict, Any


class Settings:
    """Application and test execution settings loaded from settings.json and environment."""

    def __init__(self):
        config_path = Path(__file__).parent / "settings.json"
        data: Dict[str, Any] = {}
        if config_path.exists():
            with open(config_path, "r", encoding="utf-8") as f:
                data = json.load(f)

        self.base_url: str = os.getenv("BASE_URL", data.get("base_url", "https://demoqa.com"))
        self.browser: str = os.getenv("BROWSER", data.get("browser", "chromium")).lower()
        
        headless_env = os.getenv("HEADLESS")
        if headless_env is not None:
            self.headless: bool = headless_env.lower() in ("true", "1", "yes")
        else:
            self.headless: bool = data.get("headless", True)

        self.timeout: int = int(os.getenv("TIMEOUT", data.get("timeout", 30000)))
        self.navigation_timeout: int = int(os.getenv("NAVIGATION_TIMEOUT", data.get("navigation_timeout", 45000)))
        self.viewport: Dict[str, int] = data.get("viewport", {"width": 1920, "height": 1080})
        self.slow_mo: int = int(os.getenv("SLOW_MO", data.get("slow_mo", 0)))
        self.video: str = data.get("video", "retain-on-failure")
        self.trace: str = data.get("trace", "retain-on-failure")
        self.screenshot: str = data.get("screenshot", "only-on-failure")


settings = Settings()

