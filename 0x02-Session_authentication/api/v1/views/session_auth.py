#!/usr/bin/env python3
"""Session Authentication routes"""

from os import getenv
from flask import jsonify, request
from models.user import User
from api.v1.views import app_views


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """login route"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': email})

    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"})

    from api.v1.app import auth

    session_id = auth.create_session(user[0].id)

    # session[getenv('SESSION_NAME')] = session_id
    out = jsonify(user[0].to_json())

    out.set_cookie(getenv('SESSION_NAME'), session_id)

    return jsonify(user.to_json())
