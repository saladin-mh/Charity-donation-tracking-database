import sqlite3
connection = sqlite3.connect("AuthorBooks.db")
cursor =  connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS AuthorBooks (
    author_id INTEGER,
    Book_id INTEGER
)
''')
cursor.execute(''' 
INSERT INTO AuthorBooks (author_id, Book_id) VALUES (4290, 4290)
''')
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Authors (
    id INTEGER,
    name VARCHAR,
    address VARCHAR
)
''')
cursor.execute(''' 
INSERT INTO Authors (id, name, address) VALUES (4290, "Salahdine Maamri", "Rue de la republique 
    75003 Paris")
''') 
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Books (
    id INTEGER,
    title VARCHAR,
    Category VARCHAR
)
''')
cursor.execute(''' 
INSERT INTO Books (id, title, Category) VAlues (4290, "Python I get you", "Nightmare")
''')
connection.commit()
connection.close()