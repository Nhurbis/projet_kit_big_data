from pymongo.mongo_client import MongoClient

MONGO_INITDB_DATABASE = 'todolist'
DATABASE_URL = "mongodb+srv://wkuupartage:tpaaHpGUO5Tfy6VB@bigdata.d4ltb6k.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"

# Create a new client and connect to the server
client = MongoClient(DATABASE_URL)
# Send a ping to confirm a successful connection
try:
    conn = client.server_info()
    print(f'Connected to MongoDB {conn.get("version")}')
except Exception as e:
    print(e)

db = client[MONGO_INITDB_DATABASE]
