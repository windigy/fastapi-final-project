from typing import Annotated

from database import SessionDep
from fastapi import APIRouter, Depends, status, HTTPException
from repository import create_book, get_all_books, get_book_on_id, put_book, delete_book
from schemas.books import SBook, SBookAdd

router = APIRouter(
    prefix="/api/v1",
    tags=["Books"]
)

@router.post("/books", status_code=status.HTTP_201_CREATED, response_model=SBook)
async def create_book_endpoint(data: SBookAdd, session: SessionDep):
    result = await create_book(data, session)
    return result

@router.get("/books", response_model=list[SBook])
async def get_books(session: SessionDep):
    return await get_all_books(session)

@router.get("/books/{id}", response_model=SBook)
async def get_book_on_id_endpoint(id: int, session: SessionDep):
    result = await get_book_on_id(id, session)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Книга не найдена"
        )
    
    return result

@router.put("/books/{id}", response_model=SBook)
async def put_book_endpoint(id: int, data: SBookAdd, session: SessionDep):
    result = await put_book(id, data, session)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Книга не найдена"
        )
    return result

@router.delete("/books/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_endpoint(id: int, session: SessionDep):
    result = await delete_book(id, session)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Книга не найдена"
        )
    