from flask import Flask, request, json, jsonify
from datetime import datetime

app = Flask(__name__)

with open("./data/jr_data.json", "r") as file:
    data = json.load(file)

valid_statuses = ["In Draft", "In Review", "Pending Approval", "Complete"]
json_statuses = {"In Draft": "inDraft", "In Review": "inReview", "Pending Approval": "pendingApproval", "Complete": "complete"}

## Returns user information
@app.route('/user', methods=['GET'])
def get_user():
    user = data['user']
    return jsonify({"user": user})

## Returns overall document statistics
@app.route('/stats', methods=['GET'])
def get_stats():
    stats = data['stats']
    return jsonify({"stats": stats})

##  Returns the list of documents
@app.route('/documents', methods=['GET'])
def get_docs():
    docs = data['documents']
    return jsonify({"docs": docs})

##  Updates a document's status
@app.route('/documents/<int:id>', methods=['PUT'])
def update_status(id):
    new_status = request.json.get("status")
    if not new_status or new_status not in valid_statuses:
        return jsonify({"message": "Unable to process request"}, 400)
    
    for d in data['documents']:
        if d.get('id') == id:
            current_status = json_statuses[d.get('status')]
            d['status'] = new_status
            d['lastEdited'] = datetime.today().strftime("%Y-%m-%d")
            with open("./data/jr_data.json", "w", encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            
            stats = data['stats']
            new_status = json_statuses[new_status]
            stats[current_status] -= 1
            stats[new_status] += 1
            with open("./data/jr_data.json", "w", encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            return jsonify({"message": "Update complete"}, 201)
        
    return jsonify({"message": "Unable to find document"}, 404)

if __name__ == "__main__":
    app.run(debug=True)