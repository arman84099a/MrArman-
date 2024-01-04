from MrArman.core.bot import Arman
from MrArman.core.dir import dirr
from MrArman.core.git import git
from MrArman.core.userbot import Userbot
from MrArman.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Arman()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
