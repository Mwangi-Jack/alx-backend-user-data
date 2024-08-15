#!/usr/bin/env python3
"""This file defines all the API routes"""

from flask import Flask, request, jsonify
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
