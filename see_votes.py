# import sqlite3

# # Connect to the database
# conn = sqlite3.connect('votes.db')
# cursor = conn.cursor()

# # Fetch all rows from votes table
# cursor.execute("SELECT * FROM votes")
# rows = cursor.fetchall()

# # # This will display the funnny votes only
# # print("Funny ones only")
# # cursor.execute("SELECT * FROM votes WHERE vote_type='funny'")
# # rows = cursor.fetchall()
# # print(rows)


# # Display the data
# for row in rows:
#     print(row)

# conn.close()


import sqlite3

conn = sqlite3.connect("votes.db")
c = conn.cursor()

c.execute("PRAGMA table_info(votes)")
for row in c.fetchall():
    print(row)

conn.close()
