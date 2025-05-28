from database.models import async_session
from database.models import User, Account
from sqlalchemy import select


async def set_user(tg_id, tg_name):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id,tg_name=tg_name))
            await session.commit()
    

async def proverka_accounts():
    async with async_session() as session:
        return await session.scalar(select(Account.id))
    

# async def addgaid(namefail, descriptiongaid, fail, pricecardgaid, pricestargaid):
#     async with async_session() as session:
#         session.add(Gaid(namefail=namefail, descriptiongaid=descriptiongaid, fail=fail, pricecardgaid=pricecardgaid, pricestargaid=pricestargaid))
#         await session.commit()


async def select_accounts():
    async with async_session() as session:
        return await session.scalars(select(Account))
    

async def get_game(global_game):
    async with async_session() as session:
        result = await session.scalars(select(Account).where(Account.game == global_game))
        return result
    

# async def get_gaid(getgaid):
#     async with async_session() as session:
#         result = await session.scalars(select(Gaid).where(Gaid.namefail == getgaid))
#         return result
    

# async def droptablegaid(delitintgaid):
#     async with async_session() as session:
#         namegaid = await session.scalars(select(Gaid).where(Gaid.id == delitintgaid))
#         for gaid in namegaid:
#             await session.delete(gaid)
#         await session.commit()
