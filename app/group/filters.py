import re

from aiogram.filters import BaseFilter
from aiogram.types import Message


class MaskedTextFilter(BaseFilter):
    def __init__(self, pattern: str):
        self.pattern = pattern

    async def __call__(self, message: Message) -> bool | dict[str, str]:
        word = re.search(self.pattern, message.text, re.IGNORECASE)
        if word:
            return {"word": word.group(1)}
        return False
