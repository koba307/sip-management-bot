# Инструкция по деплою SIP Management Bot

## 1. Локальный запуск (Development)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
# venv\Scripts\activate     # Windows

pip install -r requirements.txt

# Создайте .env файл
cp .env.example .env
# Заполните BOT_TOKEN и другие переменные

python main.py
```

## 2. Деплой на VPS (systemd) — Рекомендуется

### Шаг 1: Копируйте проект на сервер

```bash
git clone https://github.com/koba307/sip-management-bot.git
cd sip-management-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Шаг 2: Настройте `.env`

```bash
cp .env.example .env
nano .env
```

### Шаг 3: Создайте systemd service

```bash
sudo nano /etc/systemd/system/sip-bot.service
```

**Содержимое файла:**

```ini
[Unit]
Description=SIP Management Telegram Bot
After=network.target

[Service]
Type=simple
User=your_user
WorkingDirectory=/home/your_user/sip-management-bot
Environment="PATH=/home/your_user/sip-management-bot/venv/bin"
ExecStart=/home/your_user/sip-management-bot/venv/bin/python main.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

### Шаг 4: Запустите сервис

```bash
sudo systemctl daemon-reload
sudo systemctl enable sip-bot
sudo systemctl start sip-bot
sudo systemctl status sip-bot
```

### Полезные команды

```bash
sudo journalctl -u sip-bot -f          # просмотр логов
sudo systemctl restart sip-bot
```

## 3. Docker (опционально)

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "main.py"]
```

## Важно

- **service_account.json** не загружайте в GitHub!
- Используйте `.env` файл для секретов
- Для продакшена рекомендуется использовать systemd или Docker + systemd

## Поддержка

При возникновении проблем пишите в Issues репозитория.