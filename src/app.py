from flask import Flask, jsonify, request
app = Flask(__name__)


todos= [
    {"label": "My first task", "done": False},
    { "label": "My second task", "done": False}
    ]

@app.route('/todos', methods=['GET'])
def get_todos():
    data= jsonify(todos)
    return data

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    if request_body.get("label") is None or request_body.get("done") is None:
        return jsonify({"Message": "Error, label is required"}) 
    todos.append(request_body)
    return jsonify(todos), 201

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    if position < 0 or position >= len(todos):
        return jsonify({"message": "Invalid position"}), 400
    delete_todo= todos.pop(position)
    return jsonify(delete_todo), 200








if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)