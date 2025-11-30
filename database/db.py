import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()


def get_db_connection():
    """
    Creates and returns a connection to the database.
    Returns a psycopg2 connection object.
    """
    try:
        conn = psycopg2.connect(
            host=os.getenv("PGHOST", "localhost"),
            database=os.getenv("PGDATABASE"),
            user=os.getenv("PGUSER"),
            password=os.getenv("PGPASSWORD"),
            port=os.getenv("PGPORT", 5432),
            cursor_factory=RealDictCursor,
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        raise e
