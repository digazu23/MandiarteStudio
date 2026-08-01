<<<<<<< HEAD
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
SETTINGS_FILE=ROOT/"settings.json"
=======
"""
Mandiarte Studio

Constantes globales del proyecto.
"""

from pathlib import Path

APP_NAME = "Mandiarte Studio"

VERSION = "0.1.0"

ROOT = Path(__file__).resolve().parent.parent

ASSETS_DIR = ROOT / "assets"

OUTPUT_DIR = ROOT / "output"

PROFILE_DIR = ROOT / "profiles"

DEFAULT_PROFILE = "woocommerce.json"

SETTINGS_FILE = ROOT / "settings.json"
>>>>>>> 6eb822cc94213bf390d7c5b94e4d23cab996c31a
