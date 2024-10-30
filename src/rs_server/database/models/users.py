from database.DB import DB

class Users(DB) :

    def __init__(self) -> None:
        super().__init__()
        self.collection = self.database['Users']

    # def getByUsername(self, username: str):
    #     return self.select(["username", "password", "is_banned", "banned_text", "banned_date"], {"username": username})