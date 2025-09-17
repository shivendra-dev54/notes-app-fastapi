import asyncio
from src.config.db_connect import Base, engine

# importing tables 
from src.db.schemas.user_schema import User
from src.db.schemas.note_schema import Note

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_models())