#!/usr/bin/env python3
"""Authentication methods"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """
    This function takes in a string 'password', hashes it
    and returns the has in  ByteString
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _generate_uuid(self):
        """This method generates a unique string"""
        return str(uuid4())

    def register_user(self, email: str, password: str) -> User:
        """
        This method takes in two str arguments 'email' and 'password'
        registers the user to the database and returns the created user
        """

        try:
            user = self._db.find_user_by(email=email)

            raise ValueError(f'User {email} already exists')

        except NoResultFound:
            hashed_pass = _hash_password(password)
            user = self._db.add_user(email=email, hashed_password=hashed_pass)

            return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        This function takes in two string parameters 'email'
        and 'password' and checks if a user with these parameters
        exists
        """

        try:
            user = self._db.find_user_by(email=email)

            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)

        except NoResultFound:
            return False
