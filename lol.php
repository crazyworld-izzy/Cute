class Config(object):
    LOGGER = True

  # Get this value from my.telegram.org/apps
    API_ID =17057708 
    API_HASH = "b5f97648e6de5f0098db3ca4da989fc3"

    CASH_API_KEY = "awoo"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "something://somewhat:user@hosturl:port/databasename"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001698718312)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Devarora0987:#Dev12345@cluster0.razivtc.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

  # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/7c1ee32ae45ea4a9c106a.jpg"

    SUPPORT_CHAT = "Friendly_Chat_Group"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5972458699:AAH5r-0DBMLMGZ9bAN_hgff8ZBk9LIbFBpA"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "awoo"  # Get this value from https://timezonedb.com/api

    OWNER_ID =1066742780   # User id of your telegram account (Must be integer)
    
    BL_CHATS = (-1001698718312)
    
    DRAGONS =1066742780
    
    DEV_USERS =1066742780
    
    DEMONS =1066742780
    
    TIGERS =1066742780
    
    WOLVES =1066742780

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = (8)

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True
