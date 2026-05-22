# keyboards.py (v2.5)

def admin_main_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="➕ Добавить SIP", callback_data="admin:add")
    builder.button(text="➕ Массовое добавление", callback_data="admin:mass_add")
    builder.button(text="🗑 Массовое удаление", callback_data="admin:mass_delete")
    # ... остальные кнопки
    builder.adjust(2, 2, 1)
    return builder.as_markup()

# Другие клавиатуры
