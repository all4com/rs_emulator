from database.DB import DB

class Servers(DB) :
    initial_data = [
        {"name": "Prandel", "type": 0},
        {"name": "Nacriema", "type": 1},
        {"name": "Mundo da chibata", "type": 3},
        {"name": "GVG World 1", "type": 4},
        {"name": "Test Server", "type": 5},
    ]

    def __init__(self) -> None:
        super().__init__()
        self.collection = self.database['login_server']
        if self.collection.count_documents({}) == 0:
            self.collection.insert_many(self.initial_data)
