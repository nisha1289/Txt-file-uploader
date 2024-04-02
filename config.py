import os

API_ID = API_ID = 27039595

API_HASH = os.environ.get("API_HASH", "aabe9b61bbdb73ea4b35fc4faa880621")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6614216476:AAFDybAx7C27HAjo2AVPWiwxwwM_i2RMzvk")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6387516803))

LOG = -1001907859284,

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6387516803").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


