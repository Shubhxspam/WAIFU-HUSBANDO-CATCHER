class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "2047725696"
    sudo_users = "7093899037"
    GROUP_ID = -1002000688629
    TOKEN = "7408616113:AAGa8w4hnws4g34s4kK7rdyC1cb83O8o3K0"
    mongo_url = "mongodb+srv://naughtyboy6394:shubhxmusic11@shubhxmusid.wykecqm.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Mrpasserby_1227"
    UPDATE_CHAT = "Mrpasserby_1227"
    BOT_USERNAME = "Waifugrabberprobot"
    CHARA_CHANNEL_ID = "-10020006886291"
    api_id = 16665944
    api_hash = "a35853e36b82fa1ea0ea3e6109ef8cdd"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
