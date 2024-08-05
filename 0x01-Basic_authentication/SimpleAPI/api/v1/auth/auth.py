#!/usr/bin/env python3
"""Authentication class"""

from flask import request
from typing import List, TypeVar

class Auth:
    """This class defined all its methods"""

    def __init__(self) -> str:
        """this method initialized the class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        This method takes in 'path' and 'excluded_paths' as arguments
        and checks if the path needs authentication returning a boolean
        """
        return False

    def authorization_header(self, request=None) -> str:
        """This method returns None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """This method returns None"""
        return None
