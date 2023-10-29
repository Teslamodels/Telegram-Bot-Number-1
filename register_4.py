from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from state import RegisterState

router_4 = Router()

@router_4.message(F.photo, RegisterState.avatar)
async def send_photo(message: types.Message, state: FSMContext):
    file_id = message.photo[-1].file_id
    await state.update_data({'file_id': file_id})
    await message.answer("☎️ Phone number", reply_markup = ReplyKeyboardMarkup(resize_keyboard = True, keyboard = [
        [KeyboardButton(text = '📞 Phone number', request_contact = True)]]))
    await state.set_state(state = RegisterState.phone_number)
