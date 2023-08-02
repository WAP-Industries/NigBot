import nextcord
from nextcord.ext import commands
import requests, sys, os, random

AssetsPath = f"{os.path.dirname(sys.argv[0])}/assets"

NiggerBot = commands.Bot(command_prefix='!', intents=nextcord.Intents.all())

@NiggerBot.event
async def on_ready():
    print(f"{NiggerBot.user.name} is running")


def GetEmoji():
    emojis = "☹😔😢😭"
    return random.choice([*emojis])


def GetImages(query, queryname):
    
    errmsg = f"Failed to fetch images of {queryname} {GetEmoji()}"
    try:
        Params = {
            "Base": "https://www.googleapis.com/customsearch/v1",
            "Query": query,
            "Key": "AIzaSyDIl-1vBwIwHmtRdci-cTol-1UwVAIVUXI",
            "CX": "b3fc8ce5a0415410b",
            "Images": 10
        }
        search_url = f'{Params["Base"]}?q={Params["Query"]}&cx={Params["CX"]}&key={Params["Key"]}&searchType=image&num={Params["Images"]}'
        response = requests.get(search_url)
        extensions = ("jpg", "jpeg", "png", "gif", "webp")
        return random.choice([item['link'] for item in response.json().get('items', []) if item["link"].endswith(extensions)])  if response.status_code==200 else errmsg
    except:
        return errmsg


def GetSlur():
    try:
        with open(f"{AssetsPath}/slurs.txt", "r") as file:
            text = file.read()
            text = text.split("\n")
            index = random.randint(0, len(text)/2-1)*2
            return f"```-- {text[index]} --  \n  \n{text[index+1]}```"
    except:
        return f"Failed to get information on black slurs {GetEmoji()}"