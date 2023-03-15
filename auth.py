from flask import Flask, request, jsonify
from functools import wraps

USERS = {
    'marcel': 'marcel',
    'user2': 'password2'
}


# function to check if a username and password are valid
def check_auth(username, password):
    return username in USERS and USERS[username] == password

# decorator function to require basic authentication
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return jsonify({'message': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated
