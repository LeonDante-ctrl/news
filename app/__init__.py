from flask import Flask
from .config import DevConfig
#initializing the application

app = Flask(__name__)
from app import views