# WARN: YOU CAN GET BAN IN YOUR ACCOUNT FOR THIS SCRIPT. (...Because this script use Discord API)
# Made by IKlemOfficial

import requests
import time
from datetime import datetime

def debug(message):
    current_time = datetime.now().strftime("[%d.%m.%Y, %H:%M]")
    print(f"{current_time}> {message}")

# Discord token. 
DiscordToken = ""

# 1101720448137429054 - (is "discord.gg/danno", "#general-chat")
# if you wanna do in on others server's replace "1101720448137429054" on your Channel ID.
ChannelID = "1101720448137429054"

# API
API = f"https://discord.com/api/v9/channels/{ChannelID}/typing"

# Send token to discord.
headers = {"Authorization": DiscordToken}

# Sending API's
while True:
	a = requests.post(API, headers=headers) 
	debug(a.status_code) # debug, time + status_code. uwu.
	time.sleep(5)
