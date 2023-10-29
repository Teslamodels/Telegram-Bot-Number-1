from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from state import RegisterState

router_3 = Router()

@router_3.message(F.text, RegisterState.age)
async def send_age(message: types.Message, state: FSMContext):
    age = message.text
    if age.isdigit():
        await state.update_data({'age': age})
        await message.answer("📸 Your picture")
        await state.set_state(state = RegisterState.avatar)
    else:
        await message.answer("😩 Unsupported type")
