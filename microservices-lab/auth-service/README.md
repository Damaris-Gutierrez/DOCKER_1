# Auth Service

Este servicio contiene el script `test_connection.py`, usado para probar la conexión con PostgreSQL y Redis desde el entorno Docker Compose.

## 📂 Estructura

```plaintext
auth-service/
│
├── test_connection.py
└── README.md

## ▶️ Cómo ejecutar la prueba

1. Asegúrate de tener los contenedores levantados:
   docker compose up -d
   docker ps
2. Ejecuta el script desde tu máquina:
    python auth-service/test_connection.py
