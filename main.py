from database.db import get_db_connection


def main():
    print("Connecting to database...")
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Example query
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        print(f"Database version: {db_version['version']}")

        # Don't forget to close the cursor and connection
        cur.close()
        conn.close()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
