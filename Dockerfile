# Usa la imagen base de Python 3.10
FROM python:3.10-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requerimientos al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias especificadas en el archivo de requerimientos
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del servicio a /app
COPY . .

# Comando por defecto para ejecutar la aplicación
CMD ["python", "myapp.py"]
