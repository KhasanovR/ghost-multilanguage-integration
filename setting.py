from dotenv import load_dotenv
import ast
import os


load_dotenv()

APP_NAME = os.getenv("APP_NAME")
APP_URL = os.getenv("APP_URL")

DB_CONNECTION_URL = os.getenv("DB_CONNECTION_URL")

GHOST_ADMIN_API_TOKEN = os.getenv("GHOST_ADMIN_API_TOKEN")
GHOST_ADMIN_URL = os.getenv("GHOST_ADMIN_URL")

LANGAUGES = os.getenv("LANGAUGES")
LANGAUGES = ast.literal_eval(LANGAUGES)
LANGAUGES = [n.strip() for n in LANGAUGES]
