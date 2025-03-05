import random

from aiogram import Router, F
from aiogram.types import Message
from app.group.filters import MaskedTextFilter
from app.text import LEXICON_RU

router = Router()
router.message.filter(F.chat.type.in_({"group", "supergroup"}))


@router.message(MaskedTextFilter(r"\b(ч+у+р+к+а*(?:а|и|у|е|ой|ами|ах)?)\b"))
async def handle_masked_text(message: Message, word: str):
    await message.answer(LEXICON_RU["чурка"].format(word=word))


@router.message(MaskedTextFilter(r"\b(и+с+л+а+м+)\b"))
async def handle_masked_text(message: Message):
    await message.answer(LEXICON_RU["ислам"])


@router.message(MaskedTextFilter(r"\b(м+и+т+)\b"))
async def handle_masked_text(message: Message):
    random_num = random.randint(1, 4)
    await message.answer(LEXICON_RU[f"мит{random_num}"])


@router.message(MaskedTextFilter(r"\b(р+е+л+и+г+и+(?:я|и|ю|е|й|ям|ями|ях)?)\b"))
async def handle_religion_text(message: Message):
    await message.answer(LEXICON_RU["религия"])


@router.message(lambda message: "🕌" in message.text)
async def handle_mosque_text(message: Message):
    await message.answer(LEXICON_RU["мечеть"])
