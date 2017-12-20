import os
from flask import Flask
from .config import *

app = Flask(__name__, template_folder=os.path.abspath("vr/templates"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + CONFIG_BD_USER + ':' + CONFIG_BD_PASS +'@' + CONFIG_BD_DIR + ':' + CONFIG_BD_PORT + '/' + CONFIG_BD_NAME
app.config['SQLALCHEMY_POOL_RECYCLE'] = 500

from .controllers import *