import nextcord
from nextcord.ext import commands
import requests, sys, os, random
from time import sleep

AssetsPath = f"{os.path.dirname(sys.argv[0])}/assets"

NiggerBot = commands.Bot(command_prefix='!', intents=nextcord.Intents.all())

@NiggerBot.event
async def on_ready():
    print(f"{NiggerBot.user.name} is running")

def GetEmoji():
    emojis = "😟😞😔😢😭"
    return random.choice([*emojis])


async def GetImages(query, queryname, ctx):
    extensions = ("jpg", "jpeg", "png", "gif", "webp")
    errmsg = f"Failed to fetch images of {queryname} {GetEmoji()}"
    
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
        await msg.edit(content=
            random.choice([item['link'] for item in response.json().get('items', []) if item["link"].endswith(extensions)]) 
            if response.status_code==200 else errmsg
        )
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
        return f"Failed to get information on black slurs {GetEmoji()}"