from pathlib import Path
import json

DATA_DIR = Path(__file__).parent


def load_test_data():
    with open(DATA_DIR / "test_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

