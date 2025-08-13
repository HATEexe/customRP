from pypresence import Presence
import time
import random
import os
from dotenv import load_dotenv

load_dotenv()

RPC = Presence(os.getenv("TOKEN"))
RPC.connect()

img = os.getenv("IMG")
state = "𝙴𝚁𝚁𝙾𝚁:𝙵𝙸𝙻𝙴_𝙽𝙾𝚃_𝙴𝚇𝙸𝚂𝚃"
details = "═════════════════════"

while True:
    RPC.update(
        state = state,
        details = details,
        large_image = img,
    )

    time.sleep(40)