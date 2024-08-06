#!/usr/bin/env python3
"""BasicAuth class definition"""

import re
import base64


class BasicAuth ():
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
