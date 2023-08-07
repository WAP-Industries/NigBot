from bot import *

@NigBot.command()
async def exit(ctx):
    if ctx.message.author.id==OWNER_ID():
        await ctx.send("Bye niggas 👋")
        await NigBot.close()
        print(f"> Exited {NigBot.user.name}")
    else:
        await ctx.send("Only my owner can log me out nigga")

@NigBot.command()
async def cmdlist(ctx):
    menu = ""
    longest = len(sorted(NigBot.commands, key=lambda c: len(c.name), reverse=True)[0].name)
    
    for cog in NigBot.cogs.values():
        menu += cog.qualified_name+":\n"

        for cmd in cog.get_commands():
            menu += "\t{:<{width}}{info}\n".format(cmd.name, width=longest+3, info=cmd.help)
        menu+="\n"
    await ctx.send(f"```{menu}```")
    

# image fetching
class Image_Search(commands.Cog, name="Image Search"):
    @commands.command(name="hotnigga", help="Love me some hot niggas 🥵🥵")
    async def hotnigga(self, ctx):
        queries = ["hot muscular", "hot", "muscular", "well built", "oiled up"]
        await GetImages(ctx, "hot black men", queries, "black men images")
    
    @commands.command(name="fatnigga", help="Gotta give them bbms some love 😋")
    async def fatnigga(self, ctx):
        queries = ["fat", "obese", "morbidly obese", "extremely fat"]
        await GetImages(ctx, "fat black men", queries, "black men images")

    @commands.command(name="hogrider", help="Who up riding they hogger 💦💦")
    async def hogrider(self, ctx):
        await GetImages(ctx, "hogrider", "hog rider meme gif")

    @commands.command(name="gaynigga", help='"KAKAROT! I MUST EXPRESS MY SAIYAN PRIDE!!"')
    async def gaynigga(self, ctx):
        queries = ["black homosexuals kissing", "black gay men kissing"]
        await GetImages(ctx, "gay niggas", queries, "images")

    # @commands.command(name="search", help="General image search")
    # async def search(self, ctx, query):
    #     await GetImages(ctx, query, query)


# other
class Other(commands.Cog, name="Other"):
    @commands.command(name="info", help="Get information about the bot")
    async def info(self, ctx):
        await ctx.send("Hello! I am a bot used primarly for fetching images of niggers!\nType '!cmdlist' to see the list of possible commands.")         
    
    @commands.command(name="slur", help="Learn a new black slur!")
    async def slur(self, ctx):
        await ctx.send(GetSlur())

    @commands.command(name="neverita", help="Yo estoy puesto pa ti y tú te me quitas")
    async def neverita(self, ctx):
        await ctx.send(file=nextcord.File(f"{AssetsPath}/neverita.jpg"))


NigBot.add_cog(Image_Search(NigBot))
NigBot.add_cog(Other(NigBot))