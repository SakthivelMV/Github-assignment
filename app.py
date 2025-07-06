from flask import Flask, jsonify, request
from pymongo import MongoClient
import uuid
import hashlib

app = Flask(__name__)

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['todo_db']
todos = db['todos']

@app.route('/api', methods=['GET'])
def get_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)