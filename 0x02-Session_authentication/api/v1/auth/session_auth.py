#!/usr/bin/env python3
"""The sessionAuth Class"""

import uuid
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """
    This class defines all the methods  used for
    session authentication
    """
    user_id_by_session_id = {}

    def __init__(self):
        """This method initializes the class"""
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """
        This method takes in 'user_id' as argument and
        creates a session id for the 'user_id'
        """

        if user_id and isinstance(user_id, str):
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id

            return session_id

        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        This method takes in 'session_id' and retrieves  the user_id
        associated with the provided 'session_id'
        """

        if session_id and isinstance(session_id, str):
            return self.user_id_by_session_id.get(session_id)

        return None

    def current_user(self, request=None):
        """
        This method takes in a request object as its parameter
        and retrieves the current user based on the cookies on
        the request
        """

        session_id = self.session_cookie(request)

        user_id = self.user_id_for_session_id(session_id)

        print(User.get(user_id))

        return User.get(user_id)
