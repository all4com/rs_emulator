import sqlite3

class DB :

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DB, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, 'initialized'):
            self.database_path = "database/emulator.db"
            self.connection = sqlite3.connect(self.database_path)
            self.cursor = self.connection.cursor()
            self.initialized = True
            self.table = ""

    def set_table(self, table: str) :
        self.table = table

    def insert(self, values: dict):
        columns = ', '.join(values.keys())
        placeholders = ', '.join(['?'] * len(values))
        values = tuple(values.values())
        query = f"INSERT INTO {self.table} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.connection.commit()
    
    def delete(self, id: int):
        query = f"DELETE FROM {self.table} WHERE id = ?"
        self.cursor.execute(query, (id,))
        self.connection.commit()
    
    def update(self, id: int, values: dict, conditions: dict):
        set_str = ', '.join([f"{k} = ?" for k in values.keys()])
        condition_str = ' AND '.join([f"{k} = ?" for k in conditions.keys()])
        query = f"UPDATE {self.table} SET {set_str} WHERE {condition_str}"
        self.cursor.execute(query, tuple(values.values()) + tuple(conditions.values()))
        self.connection.commit()
    
    def select(self, fields: list, conditions: dict, limit: int = 1) :
        fields_str = ', '.join(fields)
        condition_str = ' AND '.join([f"{k} = ?" for k in conditions.keys()])
        query = f"SELECT {fields_str} FROM {self.table} WHERE {condition_str} LIMIT {limit}"
        self.cursor.execute(query, tuple(conditions.values()))
        return self.cursor.fetchall()

