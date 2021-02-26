from utils.db_api.db_commands import add_item

import asyncio

from utils.db_api.database import create_db

# Используем эту функцию, чтобы заполнить базу данных товарами
async def add_items():
    await add_item(name="ASUS",
                   category_name="🔌 Электроника", category_code="Electronics",
                   subcategory_name="🖥 Компьютеры", subcategory_code="PCs"
                   )


loop = asyncio.get_event_loop()
loop.run_until_complete(create_db())
loop.run_until_complete(add_items())