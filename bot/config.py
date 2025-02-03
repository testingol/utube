import os


class Config:

    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN environment variable is required!")

    SESSION_NAME = os.environ.get("SESSION_NAME", ":memory:")

    API_ID = os.environ.get("API_ID")
    if not API_ID:
        raise ValueError("API_ID environment variable is required!")
    API_ID = int(API_ID)

    API_HASH = os.environ.get("API_HASH")
    if not API_HASH:
        raise ValueError("API_HASH environment variable is required!")

    CLIENT_ID = os.environ.get("CLIENT_ID")
    if not CLIENT_ID:
        raise ValueError("CLIENT_ID environment variable is required!")

    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    if not CLIENT_SECRET:
        raise ValueError("CLIENT_SECRET environment variable is required!")

    BOT_OWNER = os.environ.get("BOT_OWNER")
    if not BOT_OWNER:
        raise ValueError("BOT_OWNER environment variable is required!")
    BOT_OWNER = int(BOT_OWNER)

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")
    AUTH_USERS = [BOT_OWNER] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",") if user.strip()]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")
    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE", "private")
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = "private"

    CRED_FILE = "auth_token.txt"
