from sqlalchemy import BigInteger, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///dbaccounts.sqlite3')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    tg_name = mapped_column(String(35))



class Account(Base):
    __tablename__ = 'accounts'

    id: Mapped[int] = mapped_column(primary_key=True)
    game = mapped_column(String(55))
    description = mapped_column(String(355))
    email = mapped_column(String(77))
    password = mapped_column(String(30))


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)