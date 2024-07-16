from flask import Flask, render_template, session, jsonify, json
import os

app = Flask('__name__')
app.secret_key = os.environ['SECRET']

file = open(os.path.dirname(os.path.realpath(__file__)) + "/data/jr_data.json")
data = json.load(file)

## Homepage
@app.route('/')
def index():
    return render_template('index.html', home=True)

## Returns user information
@app.route('/user', methods=['GET'])
def user():
    return render_template('user.html', message=data['user'])

## Returns overall document statistics
@app.route('/stats', methods=['GET'])
def stats():
    return render_template('user.html', message=data['stats'])

##  Returns the list of documents
@app.route('/documents', methods=['GET'])
def doc():
    return render_template('user.html', message=data['documents'])

##  Updates a document's status
@app.route('/documents/<int:id>', methods=['PUT'])
def status(id:int):
    return

## Error handlers
@app.errorhandler(404)
def not_found(e):
    session.clear()
    return render_template('incorrect.html', message="Sorry that page can't be found"), 404

@app.errorhandler(500)
def server_error(e):
    session.clear()
    return render_template('incorrect.html', message="Sorry we ran into a server error"), 500

@app.errorhandler(401)
def auth_error(e):
    session.clear()
    return render_template('incorrect.html', message="Sorry you're not authorized to access that"), 401

@app.errorhandler(400)
def bad_req(e):
    session.clear()
    return render_template('incorrect.html', message="Sorry you sent a bad request"), 400

@app.errorhandler(403)
def forbiden(e):
    session.clear()
    return render_template('incorrect.html', message="Sorry you can't do that"), 403

@app.errorhandler(501)
def unsupported(e):
    session.clear()
    return render_template('incorrect.html', message="Sorry your browser doesn't support that"), 501

@app.errorhandler(502)
def traffic(e):
    session.clear()
    return render_template('incorrect.html', message="Sorry we're expecting heavy traffic at the moment"), 502

@app.errorhandler(503)
def unavailable(e):
    session.clear()
    return render_template('incorrect.html', message="Sorry the service you're trying to reach is unavailable"), 503

if __name__ == "__main__":
    app.run()