from dotenv import load_dotenv
from pathlib import Path
import os

# Load .env from project root
env_path = Path(__file__).resolve().parent.parent / ".env"

load_dotenv(env_path)

# =========================
# OpenAI
# =========================

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)

# =========================
# Twilio
# =========================

TWILIO_ACCOUNT_SID = os.getenv(
    "TWILIO_ACCOUNT_SID"
)

TWILIO_AUTH_TOKEN = os.getenv(
    "TWILIO_AUTH_TOKEN"
)

TWILIO_PHONE_NUMBER = os.getenv(
    "TWILIO_PHONE_NUMBER"
)

# =========================
# Athena Test Number
# =========================

ATHENA_TEST_NUMBER = os.getenv(
    "ATHENA_TEST_NUMBER",
    "+18054398008"
)

# =========================
# ngrok
# =========================

NGROK_URL = "https://detonator-playtime-capped.ngrok-free.dev"

# =========================
# Optional Paths
# =========================

RECORDINGS_DIR = "recordings"

TRANSCRIPTS_DIR = "transcripts"

REPORTS_DIR = "reports"


# =========================
# Validation
# =========================

required_vars = {
    "OPENAI_API_KEY": OPENAI_API_KEY,
    "TWILIO_ACCOUNT_SID": TWILIO_ACCOUNT_SID,
    "TWILIO_AUTH_TOKEN": TWILIO_AUTH_TOKEN,
    "TWILIO_PHONE_NUMBER": TWILIO_PHONE_NUMBER,
    "NGROK_URL": NGROK_URL,
}

missing = [
    key
    for key, value in required_vars.items()
    if not value
]

if missing:

    raise ValueError(
        f"Missing environment variables: {', '.join(missing)}"
    )