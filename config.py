from os import getenv

LOAD = getenv("LOAD", "").split()

NO_LOAD = getenv("NO_LOAD", "").split()

TOKEN = getenv("TOKEN", "7932576136:AAH_p85vw5A1cJfO7hz9GVGLfr2qnzOSW3k")

MONGO_DB_URL = getenv(
    "MONGO_DB_URL",
    "mongodb+srv://musicheysiri:musicsiri123@cluster0.gozblfn.mongodb.net/?appName=Cluster0",
)
