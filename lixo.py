import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

user_input = "1 OR 1=1"
query = f"SELECT * FROM users WHERE id = {user_input}"  # inseguro
cursor.execute(query)

