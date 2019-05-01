from flask import Flask, request, jsonify

app = Flask(__name__)

ID=''
SALT=''
PW_HASH=''

@app.route('/members/<id>/salt', methods=['GET'])
def salt(id):
    if ID == id:
        return jsonify({'salt': SALT}), 201
    else:
        return 'id doesn\'t exist', 200

@app.route('/members', methods=['POST'])
def sign():
    data = request.get_json()

    if data is None:
        return 'data is None', 400

    if 'type' not in data:
        return 'data doesn\'t include type', 400

    if data['type'] == 'sign_in':
        return _sign_in(data)
    elif data['type'] == 'sign_up':
        return _sign_up(data)
    else:
        return 'type is invalid', 400

def _sign_in(data):
    required = ['id', 'pw_hash', 'salt']
    if not all(key in data for key in required):
        return 'invalid data', 400

    global ID
    global PW_HASH
    global SALT

    ID = data['id']
    PW_HASH = data['pw_hash']
    SALT = data['salt']

    return 'sign-in succeeded', 201

def _sign_up(data):
    required = ['id', 'pw_hash']
    if not all(key in data for key in required):
        return 'invalid data', 400

    if ID == data['id']:
        if PW_HASH == data['pw_hash']:
            return 'sign-up succeeded', 201

    return 'sign-up failed', 200

