# Put and Delete - http
# Working with api - json

from flask import Flask, jsonify, request

app = Flask(__name__)

# Initial data for to do list
items = [
    {'id': 1, "name": "Item 1", "Description": "This is item 1"},
    {'id': 2, "name": "Item 2", "Description": "This is item 2"}
]

@app.route('/')
def home():
    return 'To Do List App'

# Retrive all items
@app.route('/items', methods = ['GET'])
def get_items():
    return jsonify(items)

# Retrive specific item by id
@app.route('/items/<int:item_id>', methods = ['GET'])
def get_item_id(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'Error: Item Not Found!'})
    return jsonify(item)

# Post: create a new task
@app.route('/items', methods = ['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({'Error: Item Not Found!'})
    new_items = {
        'id': items[-1]['id'] + 1 if items else 1,
        'name': request.json['name'],
        'description': request.json['description']
    }
    items.append(new_items)
    return jsonify(new_items)

# Put Update an Exiting item
@app.route('/items/<int:item_id>', methods = ['PUT'])
def updat_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'Error: Item Not Found!'})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# Delete
@app.route('/items/<int:item_id>', methods = ['DELETE'])
def delete_item(item_id):
    global items
    item = [item for item in items if item['id'] != item_id]
    return jsonify({'Result: Item is Deleted.'})


if __name__ == "__main__":
    app.run(debug = True)
    