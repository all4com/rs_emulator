from database.models.users import Users
from dotenv import load_dotenv
import os

load_dotenv()

user_model = Users()
players = {}

API_SERVER_PORT = os.getenv("API_SERVER_PORT")
LOGIN_SERVER_PORT = os.getenv("LOGIN_SERVER_PORT")
GAME_SERVER_PORT = os.getenv("GAME_SERVER_PORT")
COMMUNITY_SERVER_PORT = os.getenv("COMMUNITY_SERVER_PORT")