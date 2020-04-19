from flask import Flask, request, jsonify
import json

app=Flask(__name__)
from controller import EndPointcontrollers

if __name__ == '__main__':
    app.run()