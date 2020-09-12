from flask import Flask
from .config import DevConfig
#initializing the application

app = Flask(__name__, instance_relative_config= True)
#setting up configuration

from app import views