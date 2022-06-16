import os
import json
from bson import ObjectId
from pymongo import MongoClient
from pymongo.errors import BulkWriteError, DuplicateKeyError

from dotenv import load_dotenv
load_dotenv()

DB_URI = os.getenv("DB_URI")

conn = MongoClient(DB_URI)

Jokes = conn.jokesdb.jokes

script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir)

with open(abs_file_path + '/1_jokes_examples/jokes_examples.json') as file:
    data = json.load(file)
    for doc in data:
        id = doc["_id"]['$oid']
        doc['_id'] = ObjectId(id)

try:
    Jokes.insert_many(data)
    jokes = Jokes.find()
    result = [docs for docs in jokes]
    print(f'\n ==== LOAD {len(result)} SEEDS ============= \n')
    print(result)

except (DuplicateKeyError, BulkWriteError) as err:
    print(err)

conn.close()
