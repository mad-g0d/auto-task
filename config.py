import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

ADMIN_DELAY = float(os.getenv("ADMIN_DELAY", 1.5))
FORWARD_DELAY = float(os.getenv("FORWARD_DELAY", 2.0))
BATCH_DELAY = float(os.getenv("BATCH_DELAY", 0.5))
DELETE_DELAY = float(os.getenv("DELETE_DELAY", 0.3))

MAX_BATCH_SIZE = int(os.getenv("MAX_BATCH_SIZE", 20))
MAX_RECURRING_TIME = int(os.getenv("MAX_RECURRING_TIME", 1440))
MAX_DELETE_TIME = int(os.getenv("MAX_DELETE_TIME", 10080))

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = os.getenv("LOG_FORMAT")

ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS").split(",")]
FORCE_SUB_CHANNEL_ID = int(os.getenv("FORCE_SUB_CHANNEL_ID"))

MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
