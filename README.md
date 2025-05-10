# 🧾 Fatura Takip ve Yönetim Sistemi

Bu proje, bireylerin veya kurumların fatura takibini kolaylaştırmak amacıyla geliştirilmiş bir web uygulamasıdır.  
FastAPI, Firebase ve Jinja2 template engine kullanılarak hazırlanmıştır.

---

## 🚀 Özellikler

✅ Fatura ekleme (numara, tarih, kategori, tutar, durum)  
✅ Firebase Realtime Database ile veri kaydı  
✅ Kullanıcı bazlı fatura listeleme  
✅ Fatura silme özelliği  
✅ Otomatik son ödeme tarihi hesaplama (14 gün)  
✅ Temiz, responsive HTML (Bootstrap 5 ile)

---

## 🖼️ Ekran Görüntüleri

### 📥 Fatura Ekleme Formu
![fatura-form](https://via.placeholder.com/600x300.png?text=Fatura+Ekleme+Ekrani)

### 📋 Faturalar Listesi
![fatura-list](https://via.placeholder.com/600x300.png?text=Fatura+Liste+Ekrani)

---

## 🛠️ Kullanılan Teknolojiler

| Katman        | Teknoloji             |
|---------------|------------------------|
| Backend       | FastAPI (Python)       |
| Frontend      | HTML + Bootstrap       |
| Veritabanı    | Firebase (Realtime DB) |
| Loglama       | Python logging         |

---

## 📦 Kurulum

```bash
git clone https://github.com/kullaniciadi/faturatakip.git
cd faturatakip
pip install -r requirements.txt
uvicorn app.main:app --reload
json_file_path = "firebase_key.json"
👨‍🏫 Hazırlayan
Mahmut Balta

GitHub Profilim

