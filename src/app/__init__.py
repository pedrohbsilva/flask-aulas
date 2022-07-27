import os
from flask import Flask, jsonify
from src.app.config import app_config

app = Flask(__name__)

app.config.from_object(app_config[os.getenv('FLASK_ENV')])

@app.route('/developers', methods = ['POST'])
def hello_world():

  return jsonify({"records": "Info"}), 400

