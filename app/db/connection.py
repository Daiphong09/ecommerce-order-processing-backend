from app.core.config import get_env
import psycopg2
def get_connection():
    config = get_env()
    return psycopg2.connect(host=config.get("DB_HOST"), 
                            port=config.get("DB_PORT"),
                            dbname=config.get("DB_NAME"),
                            user=config.get("DB_USER"),
                            password=config.get("DB_PASSWORD"))

