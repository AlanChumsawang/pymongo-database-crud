import os
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self):
        # Retrieving sensitive information from environment variables
        USER = os.getenv('MONGO_USER')
        PASS = os.getenv('MONGO_PASS')
        HOST = os.getenv('MONGO_HOST', 'localhost')
        PORT = int(os.getenv('MONGO_PORT'))
        DB = os.getenv('MONGO_DB')
        COL = os.getenv('MONGO_COLLECTION')
        
        # Initialize Connection
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            result = self.collection.insert_one(data)  # data should be a dictionary
            return result.inserted_id
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Method to implement the R in CRUD.
    def read(self, query=None):
        if query is not None:
            data = self.collection.find(query)
            return list(data)
        else:
            data = self.collection.find()
            return list(data)
