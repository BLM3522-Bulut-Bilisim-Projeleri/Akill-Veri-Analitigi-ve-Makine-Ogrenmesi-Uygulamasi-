# 🧠 Akıllı Veri Analitiği ve Makine Öğrenmesi Uygulaması

Bu proje, sağlık verileri üzerinde makine öğrenmesi modeli geliştirip bu modeli Google Cloud Platform üzerinde dağıtarak gerçek zamanlı tahmin yapılabilen bir API sunmayı amaçlamaktadır.

## 🎯 Proje Amacı

* Breast Cancer (meme kanseri) veri seti ile sınıflandırma modeli geliştirmek
* Eğitilen modeli Google Cloud üzerinde dağıtmak
* Gerçek zamanlı REST API ile tahminler almak
* Veriyle en yakın eşleşen kaydı bulup doğruluğu kontrol etmek

## 🚀 Kullanılan Teknolojiler

* **Backend:** Python (FastAPI)
* **ML Kütüphaneleri:** Scikit-learn, Joblib
* **Bulut Servisleri:**

  * Google Cloud Storage
  * Cloud Build
  * Cloud Run
  * Vertex AI (eğitim)
* **Ek Araçlar:** Docker, Requests, Jupyter Notebook

## 🛠️ Proje Adımları

### 1. Veri Yükleme ve Ön İşleme

* Wisconsin Breast Cancer veri seti kullanıldı
* Eksik veriler ve gereksiz sütunlar temizlendi
* Kategorik etiketler (M/B) sayısal hale getirildi

### 2. Model Geliştirme

* `RandomForestClassifier` ile %96 doğrulukta model eğitildi
* `model.joblib` olarak kaydedildi
* Toplam 32 özellik kullanıldı (`feature_names_in_`)

### 3. Docker ve Deployment

* `main.py`, `requirements.txt`, `Dockerfile`, `model.joblib` dosyalarıyla image oluşturuldu
* `gcloud builds submit` ile container image Cloud Run'a yüklendi

### 4. API Yayınlama

* Cloud Run ile model [https://eda-ml-api-207994772311.us-central1.run.app/predict](https://eda-ml-api-207994772311.us-central1.run.app/predict) adresinde yayınlandı
* POST istekleri ile JSON veri alıyor ve tahmin döndürüyor

### 5. Tahmin ve Test

* İstemciden gelen veri tahminleniyor
* Aynı zamanda veri setindeki en yakın satırla karşılaştırılarak doğruluğu test edildi

## 📦 Örnek API Kullanımı

```python
import requests

url = "https://eda-ml-api-207994772311.us-central1.run.app/predict"
data = {
    "features": [[14.2, 20.5, 95.0, 600.1, 0.1, 0.2, 0.3, 0.4, 0.1, 0.05, ...]]
}

response = requests.post(url, json=data)
print(response.json())
```

## ✅ Elde Edilen Çıktılar

* ✅ ML modeli başarıyla eğitildi
* ✅ Docker container oluşturuldu ve bulutta dağıtıldı
* ✅ API ile tahminler başarılı şekilde alındı
* ✅ Tahmin doğruluğu veri seti ile karşılaştırılarak test edildi
## Youtube
https://youtu.be/6Xe0H6ozY-s
## 📌 Sonuç

Bu proje ile uçtan uca bir makine öğrenmesi çözümü başarıyla geliştirildi ve Google Cloud üzerinde canlıya alındı. Hem veri bilimi hem de bulut mimarisi açısından güçlü bir örnek teşkil etmektedir.
