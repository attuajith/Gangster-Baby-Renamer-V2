import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5882823811:AAHebSL9Ggdpdj_v2_QTtoy2Y3VbmeiTy_c")

API_ID = int(os.environ.get("API_ID", "27884084"))

API_HASH = os.environ.get("API_HASH", "f41ef10f7e283ba0b6b18fac6fbe8226")

STRING = os.environ.get("STRING", "BQCJE0O6dt8IIs1SltuaWuV4XdmxEt5nGyJnwPYctsjrK4PiTgRlqpETGYrJuyQsscE88NqjYKCP6hTcJldOnSmdW1xOIBNvrSrjZIWXRWmB7RJGTx57Xf1m7yj87Pcg2f621piW4Sl8TCPV7k_x1CB0sy6ApEEYABHL818ys21rqx58nfv0YyHr4rU5m3yQdae4bSA34xqQTI0yL_XvpShm8ZhcVqt4F6dQ37Hk8aHHr7hXA-O-ZdeU9KKU295GONSRga2ivm4pbH5Ors91njc9HYyZ9SvngjKlmn9pnS5r2pdx9yKMspUO7hljIS4u2Qm-XAWTqckE2kzLxdrA_XIFAAAAAVf_yYkA")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
