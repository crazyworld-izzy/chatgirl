from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "mongodb+srv://Mrdaxx123:Mrdaxx123@cluster0.q1da65h.mongodb.net/?retryWrites=true&w=majority")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://musicheysiri:musicsiri123@cluster0.gozblfn.mongodb.net/?appName=Cluster0",
)
