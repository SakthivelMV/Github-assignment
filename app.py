from flask import Flask, jsonify, request
from pymongo import MongoClient
import uuid
import hashlib
import json

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

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = request.get_json()
    item = {
        'itemId': data['itemId'],
        'itemUuid': data['itemUuid'],
        'itemHash': data['itemHash'],
        'itemName': data['itemName'],
        'itemDescription': data['itemDescription']
    }
    todos.insert_one(item)
    return jsonify({'message': 'Todo item added successfully'})

if __name__ == '__main__':
    app.run(debug=True)