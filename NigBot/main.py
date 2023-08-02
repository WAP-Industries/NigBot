import os
from dotenv import load_dotenv
from bot import *
from commands import *

if __name__=="__main__":
    load_dotenv()
    NiggerBot.run(os.environ.get("TOKEN"))