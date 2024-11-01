from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.results import InsertOneResult
import common.state as state

class DB:

    def __init__(self) -> None:
        self.database_path = f"mongodb://{state.DATABASE_USERNAME}:{state.DATABASE_PASSWORD}@{state.DATABASE_HOST}:{state.DATABASE_PORT}/?authSource=admin"
        self.client = MongoClient(self.database_path)
        self.database = self.client[state.DATABASE_NAME] 

    def set_collection(self, collection_name: str):
        self.collection = self.database.collection_name

    def insert(self, values: dict):
        return self.collection.insert_one(values)

    def delete(self, id):
        self.collection.delete_one({"_id": ObjectId(id)})

    def update(self, id, values: dict):
        self.collection.update_one({"_id": ObjectId(id)}, {"$set": values})

    def select(self, conditions: dict = {}, limit: int = 0):
        cursor = self.collection.find_one(conditions)
        if limit:
            cursor = cursor.limit(limit)
        return dict(cursor)

    def find(self, projection=None,filter=None, sort=None):
        res = []
        cursor = self.collection.find(projection=projection,filter=filter,sort=sort)
        for doc in cursor:
            res.append(doc)
        return res 