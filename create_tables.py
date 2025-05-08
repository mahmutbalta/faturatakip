from app.database import Base, engine
from app.models import User, Bill  # ❗ Mutlaka sınıfları doğrudan import et

print("🛠️ Tablolar oluşturuluyor...")
Base.metadata.create_all(bind=engine)
print("✅ Tablolar başarıyla oluşturuldu.")
