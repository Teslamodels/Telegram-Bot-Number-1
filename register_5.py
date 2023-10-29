from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from state import RegisterState
from button import get_markup


router_5 = Router()

@router_5.message(F.contact, RegisterState.phone_number)
async def send_contact(message: types.Message, state: FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data({"phone_number": phone_number})
    data = await state.get_data()
    text = f"Full Name: {data.get('full_name')}\nAGE: {data.get('age')}\nPhone: {data.get('phone_number')}"
    await message.answer_photo(photo = data.get('file_id'), caption = text, reply_markup = ReplyKeyboardRemove())
    await message.answer("🧠 Do you confirm information?", reply_markup = get_markup())
    await state.set_state(state = RegisterState.confirm)
