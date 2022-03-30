from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, ChatTypeFilter

from main import dp

@dp.message_handler(CommandStart(), ChatTypeFilter(chat_type=types.ChatType.GROUP))
async def bot_start(message: types.Message):
    await message.answer(f'Welcome in the chat, {message.from_user.full_name}!')