#!/usr/bin/env python3
"""Authentication class"""

import os
from typing import List, TypeVar
from flask import request


class Auth:
    """This class defined all its methods"""

    def __init__(self) -> str:
        """this method initialized the class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        This method takes in 'path' and 'excluded_paths' as arguments
        and checks if the path needs authentication returning a boolean
        """

        if not path:
            return True

        if not excluded_paths:
            return True

        path = os.path.normpath(path).strip('/')
        excluded_paths = [os.path.normpath(p).strip('/') for p in excluded_paths]

        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                prefix = excluded_path[:1]
                if path.startswith(prefix):
                    return False
            elif path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """This method returns None"""
        if not request:
            return None

        if not request.headers.get('Authorization'):
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """This method returns None"""
        return None
