from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from state import RegisterState
from button import main_markup

router_7 = Router()

@router_7.callback_query(F.data == '❌ cancel', RegisterState.confirm)
async def choose_cancel(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer('😧 Deleted', reply_markup = main_markup())
    await state.clear()
