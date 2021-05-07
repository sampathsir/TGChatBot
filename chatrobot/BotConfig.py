import os
class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DB_URL = os.environ.get("DATABASE_URL", None)
    API_HASH = os.environ.get("API_HASH", None)
    API_ID = int(os.environ.get("APP_ID", 6))
    OWNER_ID = int(os.environ.get("OWNER_ID", None))
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", "^/")
    DUMB_CHAT = int(os.environ.get("DUMB_CHAT", False))
    CUSTOM_START = os.environ.get("CUSTOM_START", None)
    JMT_ENABLE = os.environ.get("JMT_ENABLE", False)
    JMTC_ID = int(os.environ.get("JMTC_ID", False))
    JMTC_LINK = os.environ.get("JMTC_LINK", "t.me/AyushBots")
    CUSTOM_IMG = os.environ.get("CUSTOM_IMG", "https://camo.githubusercontent.com/23baa96597c3c43fc039d4d943c272b9792dafbd6a8d50f719f1ca8687ff7bc8/68747470733a2f2f692e696d6775722e636f6d2f5057697a6e7a312e706e67")
