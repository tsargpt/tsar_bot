from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from text import LEXICON_RU


router = Router()


@router.message(Command("start"))
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU["/start"])


@router.message(Command("help"))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU["/help"])
