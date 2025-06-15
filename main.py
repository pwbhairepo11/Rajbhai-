from logging import getLogger, basicConfig, INFO

basicConfig(level=INFO)
LOGGER = getLogger(__name__)

class Config:
    API_ID = 123456
    API_HASH = "your_api_hash"
    BOT_TOKEN = "your_bot_token"
    DOWNLOAD_LOCATION = "./downloads"
    LOG_CH = -1001234567890
    PREFIX = "/"

class Msg:
    TXT_MSG = "**Send your .txt or .html file**"
    CMD_MSG_1 = "**File `{txt}` received with `{no_of_links}` links.**"

prefixes = ["/", ".", "!", "#"]
Store = type("Store", (), {})()
Store.SPROUT_URL = "https://example.com"