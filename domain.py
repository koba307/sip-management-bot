# domain.py
# SIPDomain - бизнес-логика (v2.5)

from typing import Dict, List

from sheets import SheetsRepository
from logger import log, log_error
from config import EMPLOYEE_FREE_VALUE, STATUS_WORK, STATUS_NOT_WORK


class SIPDomain:
    def __init__(self, repo: SheetsRepository):
        self.repo = repo

    async def get_statistics(self) -> Dict:
        return await self.repo.get_statistics()

    # ... (другие методы: take_sip, release_sip, intercept_sip и т.д.)

    async def admin_mass_add_sips(self, admin_name: str, parsed_data: list) -> Dict:
        """ Массовое добавление с авто-обновлением дубликатов """
        existing = await self.repo.get_existing_logins()
        added = []
        updated = []

        for item in parsed_data:
            login = item["login"]
            if login in existing:
                # Обновляем
                if item.get("domain"):
                    await self.repo.edit_sip(login, "Домен", item["domain"])
                if item.get("password"):
                    await self.repo.edit_sip(login, "Пароль", item["password"])
                if item.get("phone"):
                    await self.repo.edit_sip(login, "Телефонный номер", item["phone"])
                if item.get("provider"):
                    await self.repo.edit_sip(login, "Провайдер", item["provider"])
                if item.get("note"):
                    await self.repo.edit_sip(login, "Примечание", item["note"])
                updated.append(login)
            else:
                await self.repo.add_sip(
                    login,
                    item.get("domain", ""),
                    item.get("password", ""),
                    item.get("phone", ""),
                    item.get("provider", ""),
                    item.get("note", "")
                )
                added.append(login)

        if added or updated:
            await self.repo.add_history(
                "MASS_ADD_UPDATE", admin_name,
                f"+{len(added)} / ~{len(updated)}",
                f"Добавлено: {len(added)}, Обновлено: {len(updated)}"
            )

        return {
            "added": len(added),
            "updated": len(updated),
            "added_logins": added[:10],
            "updated_logins": updated[:10]
        }

    # Другие методы (предпросмотр, массовое удаление и т.д.) могут быть добавлены аналогично
