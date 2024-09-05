from pydantic import BaseModel
from typing import Optional, List

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    username: str
    password: str

class User(UserBase):
    id: int
    username: str
    password_hash: str
    password_salt: Optional[str] = None
    created_at: Optional[str]  # 日付のフォーマットとして string を使います
    updated_at: Optional[str]
    last_login_at: Optional[str]

    class Config:
        orm_mode = True

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
