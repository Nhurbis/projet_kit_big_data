from pymongo.mongo_client import MongoClient
from utils.loggers import debug_logger, errors_logger

MONGO_INITDB_DATABASE = 'todolist'
DATABASE_URL = "mongodb+srv://wkuupartage:tpaaHpGUO5Tfy6VB@bigdata.d4ltb6k.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"

# Create a new client and connect to the server
client = MongoClient(DATABASE_URL)
# Send a ping to confirm a successful connection
try:
    conn = client.server_info()
    print(f'Connected to MongoDB {conn.get("version")}')
    db = client[MONGO_INITDB_DATABASE]
    debug_logger.info("Connexion à la base de données réussie.")
except Exception as e:
    errors_logger.error(
        "Erreur lors de la connexion à la base de données: %s", DATABASE_URL)
    errors_logger.exception(e)
    debug_logger.debug("Erreur lors de la connexion à la base de données.")
    print(e)
