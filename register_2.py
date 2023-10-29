from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from state import RegisterState

router_2 = Router() 

@router_2.message(RegisterState.full_name, F.text)
async def send_fio(message: types.Message, state: FSMContext):
    full_name = message.text
    if full_name.isalpha():
        await state.set_data({'full_name': full_name})
        await message.answer("📅 Your age")
        await state.set_state(state=RegisterState.age)
    else:
        await message.answer('😠 Unsupported type')
