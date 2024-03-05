from typing import List
from pydantic import BaseModel

class coinInput(BaseModel):
    coin: int

class BookIdList(BaseModel):
    book_id : List[int]