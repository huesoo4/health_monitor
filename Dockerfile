FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema necesarias para psutil
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar aplicación
COPY . .

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]
