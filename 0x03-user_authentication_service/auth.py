#!/usr/bin/env python3
"""Authentication methods"""
from typing import Optional
import uuid
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """
    This function takes in a string 'password', hashes it
    and returns the has in  ByteString
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """This method generates a unique string"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

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

    def create_session(self, email: str) -> str:
        """
        This method creates a user session and returns the
        session ID
        """

        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)

            return session_id

        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Optional[User]:
        """
        This method takes in a single string argument 'session_id'
        and returns the User with the session_id or None
        """

        try:
            user = self._db.find_user_by(session_id=session_id)

            return user

        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        This method takes in an integer argument 'user_id'
        and updates the sesssion id of the associated user_id to
        None
        """

        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)

        except NoResultFound:
            return None

    def get_reset_password_token(self, email):
        """
        This method takes in a string argument 'email'
        finds the user corresponding to the 'email' and returns
        a uuid tokes if user exists else None
        """

        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()

            self._db.update_user(user.id, reset_token=reset_token)

            return reset_token

        except NoResultFound as exc:
            raise ValueError from exc

    def update_password(self, reset_token: str, password: str) -> None:
        """
        This method takes in two string arguments 'reset_token' and
        'password' and resets the password of the user with the
        corresponding 'reset_token'
        """

        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)

            self._db.update_user(user.id, hashed_password=hashed_password)

        except NoResultFound as exc:
            raise ValueError from exc
