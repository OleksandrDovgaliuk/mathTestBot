from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5208987233:AAG5wps1Qy3wf-sAcbeix8uT7Gq2k2ZGkSE'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dp, skip_updates=True)