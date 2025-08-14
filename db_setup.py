import sqlite3

conn = sqlite3.connect("votes.db")
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS votes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    headline TEXT,
    vote_type TEXT,
    timestamp TEXT
)
''')

conn.commit()
conn.close()
print("Database and table created successfully.")
