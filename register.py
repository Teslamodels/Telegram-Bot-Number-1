from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from state import RegisterState

router = Router()

@router.message(F.text == "🧾 Sign up")
async def sign_up(message: types.Message, state: FSMContext):
    await message.answer("📝 Full name", reply_markup = ReplyKeyboardRemove())
    await state.set_state(state=RegisterState.full_name)





