from database.models.users import Users
from dotenv import load_dotenv
import os

load_dotenv()
players = {}

API_SERVER_PORT = os.getenv("API_SERVER_PORT")
LOGIN_SERVER_PORT = os.getenv("LOGIN_SERVER_PORT")
GAME_SERVER_PORT = os.getenv("GAME_SERVER_PORT")
COMMUNITY_SERVER_PORT = os.getenv("COMMUNITY_SERVER_PORT")
SERVER_NAME = os.getenv("SERVER_NAME")

DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")