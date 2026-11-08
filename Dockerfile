FROM python:3.14-slim

LABEL org.opencontainers.image.title="Ficha técnica de aplicación móvil" \
      org.opencontainers.image.authors="Ricardo Palomares Viseras y Pablo Morales Gabarron" \
      org.opencontainers.image.source="https://github.com/Rykyp/ficha-app-xx"

WORKDIR /app

COPY ficha_app.py .

CMD ["python", "ficha_app.py"]