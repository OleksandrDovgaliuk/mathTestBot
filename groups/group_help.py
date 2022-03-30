from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp, ChatTypeFilter

from main import dp

@dp.message_handler(CommandHelp(), ChatTypeFilter(chat_type=types.ChatType.GROUP))
async def send_welcome(message: types.Message):
    await message.reply("It's Oleksandr Dovgaliuk's group! Have a nice experiance =)")