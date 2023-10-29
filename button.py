from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_markup():
    return ReplyKeyboardMarkup(resize_keyboard = True, keyboard = [
        [KeyboardButton(text = "🧾 Sign up")]
])

def get_markup():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text = "accept", callback_data = "✅ accept"))
    builder.add(InlineKeyboardButton(text = "cancel", callback_data = "❌ cancel"))
    return builder.as_markup()