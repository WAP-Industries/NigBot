import os
from dotenv import load_dotenv
from commands import *

if __name__=="__main__":
    load_dotenv()
    NigBot.run(os.environ.get("TOKEN"))