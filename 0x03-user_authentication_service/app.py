#!/usr/bin/env python3
"""This file defines all the API routes"""

from flask import Flask, abort, redirect, request, jsonify, url_for
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', strict_slashes=False)
def index():
    """This function defines the index route"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users/', methods=['POST'], strict_slashes=False)
def users():
    """This function defines a route to register a user"""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)

        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """This mtehod defines the route to login a user"""

    email = request.form.get('email')
    password = request.form.get('password')

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        out = jsonify({"email": email, "message": "logged in"})
        out.set_cookie("session_id", session_id)

        return out

    abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> None:
    """This method defines the route to destroy a session"""

    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if not user:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect(url_for('index'))

@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """This method defines the route to get user profile details"""

    session_id = request.cookies.get('session_id')

    user = AUTH.get_user_from_session_id(session_id)

    if user:
        return jsonify({"email": user.email}), 200

    abort(403)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
