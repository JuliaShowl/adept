from flask import Flask, render_template, session, jsonify
import os

app = Flask('__name__')
app.secret_key = os.environ['SECRET']

## Homepage
@app.route('/')
def index():
    return render_template('index.html', home=True)

## Returns user information
@app.route('/user', methods=['GET'])
def user():
    return

## Returns overall document statistics
@app.route('/stats', methods=['GET'])
def stats():
    return

##  Returns the list of documents
@app.route('/documents', methods=['GET'])
def doc():
    return

##  Updates a document's status
@app.route('/documents/<id>', methods=['PUT'])
def docs():
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