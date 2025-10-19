import os
import psycopg2
import redis

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))
POSTGRES_USER = os.getenv("POSTGRES_USER", "devuser")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "devpass")
POSTGRES_DB = os.getenv("POSTGRES_DB", "main_db")

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

def test_postgres():
    try:
        conn = psycopg2.connect(
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            dbname=POSTGRES_DB
        )
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        print("✅ Conexión exitosa a PostgreSQL:", cur.fetchone())
        cur.close()
        conn.close()
    except Exception as e:
        print("❌ Error en conexión PostgreSQL:", e)

def test_redis():
    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        r.ping()
        print("✅ Conexión exitosa a Redis")
    except Exception as e:
        print("❌ Error en conexión Redis:", e)

if __name__ == "__main__":
    test_postgres()
    test_redis()
