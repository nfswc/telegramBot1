from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from settings_local.py import API_TOKEN

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
@dp.message_handler(regexp="(^cat[s]?$|puss)")
async def cats(message: types.Message):
  await message.reply(text="Cats are here🍖")

if __name__ == "__main__":
  executor.start_polling(dp, skip_updates=True)