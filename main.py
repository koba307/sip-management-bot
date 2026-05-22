# main.py (v2.5)

import asyncio
# ... импорты

async def main():
    repo = SheetsRepository()
    await repo.init()
    await repo.ensure_dashboard_structure()
    await repo.cleanup_invalid_rows()

    domain = SIPDomain(repo)
    # ... запуск бота

if __name__ == "__main__":
    asyncio.run(main())
