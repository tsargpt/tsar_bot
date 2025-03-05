from aiogram import Router
from aiogram.types import MessageReactionUpdated

router = Router()


@router.message_reaction()
async def get_new_reaction_handle(reaction: MessageReactionUpdated):
    emoji = reaction.new_reaction if reaction.new_reaction else None
    await reaction.bot.set_message_reaction(
        reaction.chat.id, reaction.message_id, reaction=emoji
    )
    return reaction
