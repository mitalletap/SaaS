from flask import Flask
app = Flask(__name__)

from controller import EndPointcontrollers
import controller.EndPointcontrollers
from controller.EndPointcontrollers import mod
app.register_blueprint(mod,url_prefix="/api")