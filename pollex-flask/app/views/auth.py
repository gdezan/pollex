from flask import Blueprint, request, jsonify
from werkzeug import generate_password_hash, check_password_hash

from app.models import User

auth_module = Blueprint('auth', __name__, url_prefix='/auth')

@auth_module.route('', methods=['POST'])
def authenticate_user():
    try:
        username = request.json['username']
        password = request.json['password']

        # TODO: verify user
        user = {}

        if True: #user and check_password_hash('user.password', password):
            return jsonify(id=42, token="$2fr43Pv")

        return jsonify({ "message": "Invalid credentials" }), 400

    except:
        return jsonify({ "message": "expected a json with username and password" }), 400

@auth_module.route('/sign_up', methods=['POST'])
def register_user():
    data = request.get_json()

    user = User.create(email=data["email"], name=data["name"], n_usp=data["n_usp"])
    return jsonify({ "token": "not implemented" })
