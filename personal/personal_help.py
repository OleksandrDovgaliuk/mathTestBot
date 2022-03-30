from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp, ChatTypeFilter

from main import dp

@dp.message_handler(CommandHelp(), ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
async def send_welcome(message: types.Message):
    await message.reply("How can I help u?")