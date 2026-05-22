# SIP Management Telegram Bot

Telegram-бот для управления SIP-аккаунтами сотрудников через Google Sheets.

## Основные возможности

- Получение/освобождение/перехват SIP
- Массовое добавление и удаление с предпросмотром
- Автоматическое обновление дубликатов
- Полная архитектура (Handlers → Domain → Repository)
- Защита от #REF! в Google Sheets
- Автонастройка структуры DASHBOARD при запуске

## Стек

- Python 3.11+
- aiogram 3.x
- Google Sheets API (gspread)

## Запуск

1. `pip install -r requirements.txt`
2. Создайте `.env` файл с `BOT_TOKEN`
3. `python main.py`

## Архитектура

Строгое разделение:
- `bot.py` — только UI/handlers
- `domain.py` — вся бизнес-логика
- `sheets.py` — repository (Google Sheets)

## Лицензия

MIT