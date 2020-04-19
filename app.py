from flask import Flask
from flask import request
from flask import jsonify
import json

app=Flask(__name__)
from controller import EndPointcontrollers
from controller.EndPointcontrollers import mod
app.register_blueprint(
    mod, url_prefix="/api")


if __name__ == '__main__':
    app.run()