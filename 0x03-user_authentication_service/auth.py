#!/usr/bin/env python3
"""Authentication methods"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    This function takes in a string 'password', hashes it
    and returns the has in  ByteString
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
