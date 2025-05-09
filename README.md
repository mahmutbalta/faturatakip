# 🧾 Fatura Takip Sistemi

Bu proje, kullanıcıların fatura bilgilerini takip etmelerini ve ödemelerini yönetmelerini sağlar.

## 🚀 Özellikler

- Kullanıcı Kaydı & Girişi
- Fatura Ekleme & Görüntüleme
- Ödeme Durumu Takibi
- Admin Panel
- Loglama ve Docker Desteği
- PostgreSQL ile veritabanı bağlantısı
- FastAPI & HTML arayüzü

## 📁 Proje Yapısı

faturatakip/
├── app/
│ ├── main.py
│ ├── models.py
│ ├── database.py
│ ├── logging_config.py
│ └── routes.py
├── templates/
├── .env
├── Dockerfile
├── requirements.txt
└── README.md

## 🐳 Docker ile Çalıştırma

```bash
docker build -t faturatakip .
docker run -d -p 8000:8000 --name fatura-api faturatakip
🌐 Uygulama URL'leri
Kullanıcı Paneli: http://localhost:8000/panel

Swagger UI: http://localhost:8000/docs

👤 Geliştirici
Mahmut Balta → GitHub

#### 3. **Git ile GitHub'a gönderin:**

```bash
git add README.md
git commit -m "📄 README eklendi"
git push origin main
