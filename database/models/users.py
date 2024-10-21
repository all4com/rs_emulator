from database.DB import DB

class Users(DB) :

    def __init__(self) -> None:
        super().__init__()
        self.table = "users"
        self._create_table()
    
    def _create_table(self): 
        query = f'''
            CREATE TABLE IF NOT EXISTS {self.table} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                is_banned INTERGER DEFAULT 0,
                banned_text TEXT,
                banned_date TEXT
            )
        '''
        self.cursor.execute(query)
        self.connection.commit()

    def getByUsername(self, username: str):
        return self.select(["username", "password", "is_banned", "banned_text", "banned_date"], {"username": username})