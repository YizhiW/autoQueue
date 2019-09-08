import os
from pathlib import Path
import dotenv

CWD = Path(os.getcwd())
ROOT = os.path.dirname(os.path.abspath(__file__))

# preload env var
dotenv.load_dotenv(CWD / ".env")

# env var
WOW_ICON_X = int(os.getenv("WOW_ICON_X"))
WOW_ICON_Y = int(os.getenv("WOW_ICON_Y"))
RUNGAME_X = int(os.getenv("RUNGAME_X"))
RUNGAME_Y = int(os.getenv("RUNGAME_Y"))
SERVER_X = int(os.getenv("SERVER_X"))
SERVER_Y = int(os.getenv("SERVER_Y"))
WAIT_TIME_BTW = int(os.getenv("WAIT_TIME_BTW"))



