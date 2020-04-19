from flask import Flask, request, jsonify,Blueprint
import json

app=Flask(__name__)
import controller.EndPointcontrollers
from controller.EndPointcontrollers import mod

app.register_blueprint(mod,url_prefix="/api")
if __name__ == '__main__':
    app.run()