import nextcord
from nextcord.ext import commands
import requests, sys, os, random
from time import sleep
from datetime import datetime

AssetsPath = f"{os.path.dirname(sys.argv[0])}/assets"

OWNER_ID = lambda: int(os.environ.get("OWNER_ID"))
NigBot = commands.Bot(command_prefix='!', intents=nextcord.Intents.all())


# override help
class CustomHelp(commands.HelpCommand):
    async def send_bot_help(self, mapping): pass
NigBot.help_command = CustomHelp()

@NigBot.event
async def on_ready():
    print(f"> {NigBot.user.name} is running")


def SadEmoji():
    emojis = "😟😞😔😢😭"
    return random.choice([*emojis])

async def GetImages(ctx, queryname, queries, adq=""):
    query = (random.choice(queries) if type(queries).__name__=="list" else queries)+f" {adq}"
    extensions = ("jpg", "jpeg", "png", "gif", "webp")
    errmsg = f"Failed to fetch images of {queryname} {SadEmoji()}"
    
    async def FetchAnim(message):
        text = message.content
        sep = ". "
        for i in range(0, random.randint(3,7)):
            sleep(0.5)
            text = text.replace(sep, "") if text.count(sep)>=3 else text+sep
            await message.edit(content=text)

    Params = {
        "Base": "https://www.googleapis.com/customsearch/v1",
        "Query": query,
        "Key": os.environ.get("API_KEY"),
        "CX": os.environ.get("CX_TOKEN"),
        "Images": 10
    }
    search_url = f'{Params["Base"]}?q={Params["Query"]}&cx={Params["CX"]}&key={Params["Key"]}&searchType=image&num={Params["Images"]}'
    
    msg = await ctx.send("Fetching images")
    await FetchAnim(msg)
        
    try:
        response = requests.get(search_url)     
        link = (random.choice([item['link'] for item in response.json().get('items', []) if item["link"].endswith(extensions)]) 
                if response.status_code==200 else None)
        fetchinfo = "\n".join([f"Time: {datetime.now().strftime('%d/%m/%Y %H:%M')}", f"Query: {query}", f"Image link: {link}"])
        await msg.edit(content=fetchinfo if link else errmsg)
    except:
        await ctx.send(errmsg)


def GetSlur():
    try:
        with open(f"{AssetsPath}/slurs.txt", "r") as file:
            text = file.read()
            text = text.split("\n")
            index = random.randint(0, len(text)/2-1)*2
            return f"```-- {text[index]} --  \n  \n{text[index+1]}```"
    except:
        return f"Failed to get information on black slurs {SadEmoji()}"