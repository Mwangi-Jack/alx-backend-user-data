#!/usr/bin/env python3
"""BasicAuth class definition"""

import binascii
import re
import base64
from typing import TypeVar

from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth (Auth):
    """This class defines all its methods"""
    def __init__(self):
        """initialization method"""
        super().__init__()

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """This method extracts the base64 authorization header"""
        if authorization_header:
            if isinstance(authorization_header, str):
                pattern = r'^Basic (.*)'
                match = re.match(pattern, authorization_header)

                if match:
                    return match.group(1)

        return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """This method takes in a Base64 string
        'base64_authorization_header and decodes its value
        """
        try:
            if base64_authorization_header:
                if isinstance(base64_authorization_header, str):
                    decoded_str = base64.b64decode(base64_authorization_header)
                    return decoded_str.decode('utf-8')

            return None
        except (binascii.Error, ValueError):
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """
        This method takes in 'decoded_base64_authorization_header' as argument
        and extracts username and email returning a tuple consisting of the two
        """
        if decoded_base64_authorization_header:
            if isinstance(decoded_base64_authorization_header, str):
                pattern = r'^([^:]+):(.+)$'
                match = re.match(pattern, decoded_base64_authorization_header)

                if match:
                    return (match.group(1), match.group(2))

        return (None, None)

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        This method takes in 'user_email' and 'user_pwd' and checks if the user
        exists in the database
        """
        if user_email and user_pwd:
            if isinstance(user_email, str) and isinstance(user_pwd, str):
                user = User.search({'email': user_email})
                if user:
                    if user[0].is_valid_password(user_pwd):
                        return user[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """This method retrieves  the current user"""
        if not request:
            return None

        authorization_header = self.authorization_header(request)
        auth = self.extract_base64_authorization_header(authorization_header)

        b64_auth = self.decode_base64_authorization_header(auth)
        credentials = self.extract_user_credentials(b64_auth)

        if credentials:
            return self.user_object_from_credentials(credentials[0],
                                                     credentials[1])

        return credentials
