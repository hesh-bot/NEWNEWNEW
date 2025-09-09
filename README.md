# Telegram Anonymous Complaints Bot

## Установка и запуск (локально)
1. Установите Python 3.10+.
2. Распакуйте архив и перейдите в папку проекта:
   ```bash
   cd telegram_anon_bot
   ```
3. Создайте виртуальное окружение:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .venv\Scripts\Activate.ps1 # Windows PowerShell
   ```
4. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
5. Скопируйте `.env.example` в `.env` и укажите `BOT_TOKEN` и `ADMIN_CHAT_ID`.
6. Запустите бота:
   ```bash
   python app.py
   ```

## Деплой (например Railway/Render/Docker)
- Можно запустить бота бесплатно на Railway или Render.
- Для Linux-сервера можно использовать systemd (см. README из расширенной версии).
