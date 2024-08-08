#!/usr/bin/env python3
"""The sessionAuth Class"""

import uuid
from api.v1.auth.auth import Auth


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
