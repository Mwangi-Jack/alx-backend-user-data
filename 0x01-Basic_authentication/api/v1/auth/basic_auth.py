#!/usr/bin/env python3
"""BasicAuth class definition"""

import re
import base64
from auth import Auth


class BasicAuth (Auth):
    """This class defines all its methods"""
    def __init__(self):
        """initialization method"""
        pass

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
        except ValueError:
            return None
