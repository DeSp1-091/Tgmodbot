import os
from dotenv import load_dotenv, find_dotenv
import logging
from aiogram import Bot, Dispatcher
from filters import IsAdminFilter

#log level
logging.basicConfig(level=logging.INFO)

#bot init
load_dotenv(find_dotenv())
bot = Bot(os.getenv('Token'))
dp = Dispatcher(bot)

#filter
dp.filters_factory.bind(IsAdminFilter)