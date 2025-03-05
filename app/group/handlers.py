import random

from aiogram import Router, F
from aiogram.types import Message
from app.group.filters import MaskedTextFilter
from app.text import LEXICON_RU

router = Router()
router.message.filter(F.chat.type.in_({"group", "supergroup"}))


@router.message(MaskedTextFilter(r"\b(ч+у+р+к+а+)\b"))
async def handle_masked_text(message: Message, word: str):
    await message.answer(LEXICON_RU["чурка"].format(word=word))


@router.message(MaskedTextFilter(r"\b(и+с+л+а+м+)\b"))
async def handle_masked_text(message: Message, word: str):
    await message.answer(LEXICON_RU["ислам"].format(word=word))


@router.message(MaskedTextFilter(r"\b(м+и+т+)\b"))
async def handle_masked_text(message: Message, word: str):
    random_num = random.randint(1, 4)
    await message.answer(LEXICON_RU[f"мит{random_num}"].format(word=word))
