import sqlite3


class db_manager:
    def __init__(self, database):
        self.database = database
        self.database.cursor().executescript("""
        CREATE TABLE IF NOT EXISTS salas(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            tipo VARCHAR(10) NOT NULL,
            lotacao INTEGER NOT NULL);
            
        CREATE TABLE IF NOT EXISTS pessoas(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nickname VARCHAR(40) UNIQUE NOT NULL,
            first_name VARCHAR(40) NOT NULL,
            last_name VARCHAR(40) NOT NULL,
            event_room INTEGER,
                
            FOREIGN KEY (event_room) REFERENCES salas(id));
        """)
    def save(self):
        self.database.commit()
    
    # Create (C)
    def insert_into(self, nickname, first_name, last_name):
        try:
            self.database.cursor().executemany("INSERT OR REPLACE INTO pessoas(id, nickname, first_name, last_name) VALUES (NULL, ?,?,?)",
                                            [(nickname, first_name, last_name)])
        except Exception as e:
            raise e
        else:
            self.database.commit()
    # Read (R)
    def read_user_data(self, nickname):
        self.database.cursor().execute(f'SELECT * FROM pessoas WHERE nickname = {nickname} ')
        return self.database.fetchall()
    
    def read_all_data(self):
        self.database.cursor().execute(f'SELECT * FROM pessoas')
        return self.database.fetchall()
    # Update (U)
    def edit_user_data(self, nickname):
        return self.database.cursor().executemany("",
                                                  [()])
    # Delete (D)
    def delete_user_data(self, nickname):
        self.database.cursor().execute(f"DELETE FROM pessoas WHERE nickname = {nickname}")
    