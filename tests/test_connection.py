from src.db_connection import get_connection

def test_connection():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 'Connected to Oracle!' FROM dual")
    print(cursor.fetchone()[0])
    conn.close()

if __name__ == "__main__":
    test_connection()
