from flask import Flask, request, jsonify
from controller import controller
app = Flask(__name__)

@app.route('/memory')
def memory_stat():






