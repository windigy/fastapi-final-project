from sqlalchemy.ext.asyncio import AsyncSession
from schemas.books import SBookAdd
from models.books import BooksModel

from sqlalchemy import select

async def create_book(data: SBookAdd, session: AsyncSession):
    book = data.model_dump()
    new_book = BooksModel(**book)
    session.add(new_book)
    await session.commit()
    await session.refresh(new_book)
    return new_book

async def get_all_books(session: AsyncSession):
    stmt = select(BooksModel)
    result = await session.execute(stmt)
    return result.scalars().all()

async def get_book_on_id(id: int, session: AsyncSession):
    stmt = select(BooksModel).where(BooksModel.id == id)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()

async def put_book(id: int, data: SBookAdd, session: AsyncSession):
    stmt = select(BooksModel).where(BooksModel.id == id)
    resDB = await session.execute(stmt)
    book = resDB.scalar_one_or_none()
    if not book:
        return None
    
    md = data.model_dump(exclude_unset=True)
    for key, value in md.items():
        setattr(book, key, value)
        
    await session.commit()
    await session.refresh(book)
    return book

async def delete_book(id: int, session: AsyncSession):
    stmt = select(BooksModel).where(BooksModel.id == id)
    resDB = await session.execute(stmt)
    result = resDB.scalar_one_or_none()
    if not result:
        return None

    await session.delete(result)
    await session.commit()
    return True
    