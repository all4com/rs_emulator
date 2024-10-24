from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.results import InsertOneResult
import common.state as state

class DB:

    def __init__(self) -> None:
        self.database_path = f"mongodb://{state.DATABASE_USERNAME}:{state.DATABASE_PASSWORD}@{state.DATABASE_HOST}:{state.DATABASE_PORT}/?authSource=admin"
        self.cursor = MongoClient(self.database_path)
        self.database = self.cursor[state.DATABASE_NAME]
        self.collection = self.database.admin  # Agora é um objeto de coleção

    def set_collection(self, collection_name: str):
        self.collection = self.database.collection_name

    def insert(self, values: dict):
        return self.collection.insert_one(values)

    def delete(self, id):
        self.collection.delete_one({"_id": ObjectId(id)})

    def update(self, id, values: dict):
        self.collection.update_one({"_id": ObjectId(id)}, {"$set": values})

    def select(self, fields: list = None, conditions: dict = {}, limit: int = 0):
        projection = {field: 1 for field in fields} if fields else None
        cursor = self.collection.find(conditions, projection)
        if limit:
            cursor = cursor.limit(limit)
        return list(cursor)
