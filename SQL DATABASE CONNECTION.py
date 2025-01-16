
import sqlite3
import csv

# Function to create the necessary tables
def create_tables(conn):
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Artist (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Genre (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Album (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id INTEGER,
        title TEXT UNIQUE
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Track (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE,
        album_id INTEGER,
        genre_id INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    )''')

    conn.commit()

# Function to insert data from the CSV file into the database
def insert_data_from_csv(conn, csv_filename):
    cur = conn.cursor()

    with open(csv_filename, 'r') as f:
        reader = csv.DictReader(f)

        # Debugging: print CSV column names to ensure they match
        print("CSV columns:", reader.fieldnames)

        for row in reader:
            # Insert Artist
            cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES (?)''', (row['Artist'],))

            # Insert Genre
            cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES (?)''', (row['Genre'],))

            # Insert Album
            cur.execute('''INSERT OR IGNORE INTO Album (artist_id, title) 
                VALUES ((SELECT id FROM Artist WHERE name = ?), ?)''', 
                (row['Artist'], row['Album']))

            # Insert Track
            cur.execute('''INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) 
                VALUES (?, (SELECT id FROM Album WHERE title = ?), 
                        (SELECT id FROM Genre WHERE name = ?), ?, ?, ?)''', 
                (row['Track'], row['Album'], row['Genre'], row['Length'], row['Rating'], row['Count']))

    conn.commit()

# Function to query the database and display the results
def query_database(conn):
    cur = conn.cursor()
    cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name 
                   FROM Track 
                   JOIN Genre ON Track.genre_id = Genre.id
                   JOIN Album ON Track.album_id = Album.id
                   JOIN Artist ON Album.artist_id = Artist.id
                   ORDER BY Artist.name LIMIT 3''')

    rows = cur.fetchall()
    print("\nTop 3 Tracks:")
    for row in rows:
        print(f"Track: {row[0]}, Artist: {row[1]}, Album: {row[2]}, Genre: {row[3]}")

# Main function to execute the program
def main():
    # Connect to SQLite database
    conn = sqlite3.connect('musicdb.sqlite')
    
    # Create the necessary tables
    create_tables(conn)

    # Insert data from the provided CSV file
    insert_data_from_csv(conn, 'tracks.csv')

    # Query the database and print results
    query_database(conn)

    conn.close()

if __name__ == '__main__':
    main()
