from aiogram.filters import BaseFilter
from aiogram.types import MessageReactionUpdated


# TODO filter with counter reactions
class ReactionsEqualUsers(BaseFilter):
    async def __call__(self, reaction: MessageReactionUpdated) -> bool:
        chat_member_count = await reaction.bot.get_chat_member_count(reaction.chat.id)

        total_reactions = sum([r.count for r in reaction.message_reactions])
        return total_reactions == chat_member_count
