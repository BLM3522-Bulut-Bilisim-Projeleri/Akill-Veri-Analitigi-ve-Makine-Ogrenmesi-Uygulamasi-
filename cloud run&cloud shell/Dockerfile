# Python 3.9 slim imajı ile başla
FROM python:3.9-slim

# Uygulama klasörünü oluştur
WORKDIR /app

# Gerekli Python paketlerini yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ana Python uygulama dosyasını ve modeli kopyala
COPY main.py .
COPY model.joblib .

# API'yi başlat
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

