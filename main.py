from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import config_bot

bot = Bot(config_bot.TOKEN_API)
dp = Dispatcher(bot=bot, storage=MemoryStorage)
logging.basicConfig(level=logging.INFO, filemode='w', filename='bot.log',
                    format='%(asctime)s | %(levelname)s | %(message)s')




def main():
    logging.info('START BOT')
    executor.start_polling(dispatcher=dp, skip_updates=True)

if __name__ == '__main__':
    main()