from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

# Kullanıcı Şemaları
class UserBase(BaseModel):
    full_name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    class Config:
        orm_mode = True

# Fatura Şemaları
class BillBase(BaseModel):
    type: str
    amount: float
    due_date: Optional[date] = None

class BillCreate(BillBase):
    pass

class BillOut(BillBase):
    id: int
    paid: bool
    user_id: int
    class Config:
        orm_mode = True
