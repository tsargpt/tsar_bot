import asyncio

from aiogram import Bot, Dispatcher

from app.commands import router as commands_router
from app.reaction.handlers import router as emoji_router
from app.group.handlers import router as group_router
from config import settings

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

dp.include_router(commands_router)
dp.include_router(emoji_router)
dp.include_router(group_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
