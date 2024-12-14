from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "7817669190:AAEIHg1P6lJa9l_1ufPPxTjezb4v69ANGnQ")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://musicheysiri:musicsiri123@cluster0.gozblfn.mongodb.net/?appName=Cluster0",
)
