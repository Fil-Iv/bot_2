import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

API_TOKEN = '7956362362:AAF28BTDCVTh-Qu9sdEVGmB9hv7h8c2n3O0'


bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()


PRODUCTS_LINK = 'https://temu.to/k/e0qngcb6ac1'
APP_LINK = 'https://app.temu.com/m/nuxbtljhd5f'


@dp.message(F.text.lower().in_({"стоки", "оферти", "намаления"}))
async def send_products_link(message: Message):
    await message.answer(f"🛍️ Виж най-добрите оферти в Temu тук:\n{PRODUCTS_LINK}")


@dp.message(F.text.lower().in_({"приложение", "app", "изтегляне"}))
async def send_app_link(message: Message):
    await message.answer(f"📲 Изтегли Temu и вземи бонус оферта:\n{APP_LINK}")


@dp.message()
async def menu(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 Оферти", callback_data="show_offers")],
        [InlineKeyboardButton(text="📲 Изтегли приложението", callback_data="download_app")],
    ])
    await message.answer("Избери какво искаш да направиш:", reply_markup=keyboard)


@dp.callback_query(F.data == "show_offers")
async def offers_callback(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f"🛍️ Оферти в Temu:\n{PRODUCTS_LINK}")
    await callback_query.answer()

@dp.callback_query(F.data == "download_app")
async def app_callback(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f"📲 Изтегли приложението тук:\n{APP_LINK}")
    await callback_query.answer()

# Стартиране на бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())