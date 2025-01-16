import sqlite3

# Connect to the database (or create it)
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Set up the Counts table
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# Open the mbox.txt file
with open('mbox.txt') as f:
    for line in f:
        if not line.startswith('From: '):
            continue
        email = line.split()[1]
        org = email.split('@')[1]

        # Update the counts
        cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

# Commit the changes once outside the loop
conn.commit()

# Optional: Print the results to verify
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(row)

cur.close()
