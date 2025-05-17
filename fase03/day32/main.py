import json

from flask import Flask, jsonify, request

PATH_JSON = "data.json"

app = Flask(__name__)


def load_items():
    with open(PATH_JSON, "r") as f:
        return json.load(f)


def save_items(items):
    with open(PATH_JSON, "w") as f:
        json.dump(items, f, indent=4)


@app.route('/items', methods=['GET'])
def get_items():
    return load_items()


@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    data = load_items()

    for item in data:
        if item["id"] == item_id:
            return item
        else:
            return jsonify({"error": "Item not found"}), 404


@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()

    if not new_item or "name" not in new_item or "price" not in new_item:
        return jsonify({"error": "Missing 'name' or 'price'"}), 400

    items = load_items()
    new_id = max([item["id"] for item in items], default=0) + 1
    new_item["id"] = new_id
    items.append(new_item)
    save_items(items)

    return jsonify(new_item), 201


@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    items = load_items()

    for item in items:
        if item["id"] == item_id:
            item["name"] = data.get("name", item["name"])
            item["price"] = data.get("price", item["price"])
            save_items(items)
            return jsonify(item)
    return jsonify({"error": "Item no encontrado"}), 404


@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    items = load_items()
    filtered_items = [item for item in items if item["id"] != item_id]

    if len(filtered_items) == len(items):
        return jsonify({"error": "Item not found"}), 404

    save_items(filtered_items)
    return jsonify({"message": f"Item with id {item_id} deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)
