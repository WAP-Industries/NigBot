from bot import *

@NigBot.command(name="info", help="Get information about the bot")
async def info(ctx):
    await ctx.send("Hello! I am a bot that is all about niggers!\nType '!help' to see the list of possible commands.")


@NigBot.command(name="img", help="Scrape the internet for pictures of hot black men 🥵🥵")
async def img(ctx):
    queries = ["hot muscular", "hot", "muscular", "well built", "oiled up"]
    await GetImages(f"{random.choice(queries)} black men images", "hot black men", ctx)


@NigBot.command(name="hogrider", help="Who up riding they hogger 💦💦")
async def hogrider(ctx):
    await GetImages("hog rider meme gif", "hogrider", ctx)


@NigBot.command(name="slur", help="Learn a new black slur!")
async def slur(ctx):
    await ctx.send(GetSlur())


@NigBot.command(hidden=True)
async def exit(ctx):
    if ctx.message.author.guild_permissions.administrator:
        await ctx.send("Bye niggas 👋")
        await NigBot.close()
    else:
        await ctx.send("Only administrators can log me out nigga")