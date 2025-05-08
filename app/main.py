from fastapi import FastAPI
from app.routes import router  # ← dikkat: direkt `router` import ediliyor

app = FastAPI(
    title="Fatura Takip Sistemi",
    description="Kullanıcılar ve faturalar için REST API",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Fatura Takip API çalışıyor."}
