from telethon import events
import FINAL.client
import time
import os

client = FINAL.client.client

@events.register(events.NewMessage(outgoing=True, pattern=r'^\.م17$'))
async def alive(event):
    client = event.client
    me = await client.get_me()
    username = me.username
    img = await client.download_profile_photo(username)
    time.sleep(0.5)
    await event.respond(f"""**
<━━━[★] اوامر التنصيب [★]━━━>

▪︎||عـذرا الميزة غير متاحة للاستخدام بسبب انك قمت بالتنصيب من خلال البوت .


**""", file=img, parse_mode="markdown")
    await event.message.delete()
    os.remove(img)
