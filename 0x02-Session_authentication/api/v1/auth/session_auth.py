#!/usr/bin/env python3
"""The sessionAuth Class"""


from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    This class defines all the methods  used for
    session authentication
    """

    def __init__(self):
        """This method initializes the class"""
        super().__init__()

