import os

API_ID = API_ID = 20499923

API_HASH = os.environ.get("API_HASH", "b33b8c26d7f2d94ef2600d8adec1cc4a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6677111924:AAFplEJgI7tuCdJnEXTjryvERR9v4WE2ZyU")

OWNER = int(os.environ.get("OWNER", 5931737600)

LOG = -1001889383537,

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5931737600").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


