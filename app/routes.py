from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Bu e-posta zaten kayıtlı.")
    return crud.create_user(db, user)

@router.get("/users/{user_id}/bills/", response_model=list[schemas.BillOut])
def get_user_bills(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_bills(db, user_id)

@router.post("/users/{user_id}/bills/", response_model=schemas.BillOut)
def create_bill_for_user(user_id: int, bill: schemas.BillCreate, db: Session = Depends(get_db)):
    return crud.create_bill(db, bill, user_id)

@router.get("/bills/", response_model=list[schemas.BillOut])
def get_all_bills(db: Session = Depends(get_db)):
    return crud.get_all_bills(db)
