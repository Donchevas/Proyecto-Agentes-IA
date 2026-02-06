FROM python:3.10-slim
# Se cambió el espacio por "=" (Línea 2 y 3)
ENV PYTHONUNBUFFERED=True
ENV APP_HOME=/app
WORKDIR $APP_HOME
COPY . ./
RUN pip install --no-cache-dir -r requirements.txt
# Se recomienda formato JSON para CMD (Línea 8)
CMD ["gunicorn", "--bind", ":8080", "--workers", "1", "--threads", "8", "--timeout", "0", "main:app"]