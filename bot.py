# bot.py (v2.5 - с исправленным админ-меню и массовыми операциями)

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

# ... (импорты)

class AdminStates(StatesGroup):
    mass_add_input = State()
    mass_add_preview = State()
    mass_add_confirm = State()
    # другие состояния

# Исправленный cmd_start
@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    if _is_admin(message.from_user.id):
        await message.answer(
            "👑 <b>Админ-панель</b>",
            reply_markup=admin_main_menu()
        )
    else:
        # обычное меню
        pass

# Обработчики массового добавления с предпросмотром
# ... (полный код из предыдущих ответов)
