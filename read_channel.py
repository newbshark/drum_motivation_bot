from pyrogram import Client
import asyncio

API_ID = 29100409
API_HASH = "3b4939c97c8431d565d8897811c2cda9"
CHANNEL = "@hogwartsdrums"

async def find_messages_by_keyword(keyword: str):
    async with Client("my_session", api_id=API_ID, api_hash=API_HASH) as app:
        results = []
        print(f"🔍 Поиск сообщений с ключевым словом '{keyword}' в канале {CHANNEL}...")
        async for message in app.search_messages(CHANNEL, keyword, limit=100):
            text = message.text or message.caption or ""
            print(f"✅ Найдено сообщение {message.id}: {text[:50]}")
            results.append({"message_id": message.id, "text": text})
        print(f"🎯 Всего найдено: {len(results)}")
        return results

if __name__ == "__main__":
    keyword = input("Введите пароль-слово для поиска: ")
    asyncio.run(find_messages_by_keyword(keyword))
