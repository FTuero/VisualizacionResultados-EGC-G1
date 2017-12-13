from flask import Flask
from .config import *

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + CONFIG_BD_USER + ':' + CONFIG_BD_PASS +'@' + CONFIG_BD_DIR + '/' + CONFIG_BD_NAME

from .controllers import *