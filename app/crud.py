from sqlalchemy.orm import Session
from app import models, schemas
from typing import List, Optional

# Kullanıcı oluştur
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        full_name=user.full_name,
        email=user.email,
        password=user.password  # Gerçekte hashlemelisin
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# E-posta ile kullanıcı getir
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Fatura ekle
def create_bill(db: Session, bill: schemas.BillCreate, user_id: int):
    db_bill = models.Bill(**bill.dict(), user_id=user_id)
    db.add(db_bill)
    db.commit()
    db.refresh(db_bill)
    return db_bill

# Kullanıcının faturalarını getir
def get_user_bills(db: Session, user_id: int):
    return db.query(models.Bill).filter(models.Bill.user_id == user_id).all()

# Tüm faturaları getir
def get_all_bills(db: Session):
    return db.query(models.Bill).all()
