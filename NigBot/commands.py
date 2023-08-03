from bot import *
import random

@NiggerBot.command(name="info", help="Get information about the bot")
async def info(ctx):
    await ctx.send("Hello! I am a bot that is all about niggers!\nType '!help' to see the list of possible commands.")


@NiggerBot.command(name="img", help="Scrape the internet for pictures of hot black men 🥵🥵")
async def img(ctx):  
    await ctx.send(GetImages("hot muscular black men images", "hot black men"))


@NiggerBot.command(name="hogrider", help="Who up riding they hogger 💦💦")
async def hogrider(ctx):
    await ctx.send(GetImages("hog rider meme gif", "hogrider"))


@NiggerBot.command(name="slur", help="Learn a new black slur!")
async def slur(ctx):
    await ctx.send(GetSlur())

@NiggerBot.command(name="", help="")
async def _(ctx):
    pass