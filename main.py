from telethon import TelegramClient, events
import re
import os
from keep_alive import keep_alive

# بيانات الدخول
api_id = 21139372
api_hash = '312b5024cd78726e15afb1b0431b5047'

# إعداد الجلسة
client = TelegramClient('replit_session', api_id, api_hash)

# دالة تنظيف النص
def clean_text(text):
    if not text:
        return ''
    text = re.sub(r'http\\S+', '', text)
    text = re.sub(r'@\\w+', '', text)
    return text.strip()

# الدالة الرئيسية التي تشغّل البوت
async def main():
    await client.start()
    print("✅ Bot is running and listening for crypto_News24_Z...")

    source = await client.get_entity('https://t.me/crypto_News24_Z')
    target = await client.get_entity('https://t.me/fourx00')

    @client.on(events.NewMessage(chats=source))
    async def handler(event):
        message = event.message
        text = clean_text(message.message or message.text)
        print(f"\n📥 New message:\n{text}\n")
        if message.photo:
            await client.send_file(target, message.photo, caption=text)
        elif text:
            await client.send_message(target, text)

    await client.run_until_disconnected()

# شغّل خدمة keep_alive أولًا
keep_alive()

# ثم شغّل البوت
client.loop.run_until_complete(main())
