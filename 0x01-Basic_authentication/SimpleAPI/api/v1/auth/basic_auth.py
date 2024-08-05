#!/usr/bin/env python3
"""BasicAuth class definition"""

import re


class BasicAuth:
    """This class defines all its methods"""
    def __init__(self):
        """initialization method"""
        pass

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """This method extracts the base64 authorization header"""
        if authorization_header:
            if isinstance(authorization_header, str):
                pattern = r'^Basic (.*)'
                match = re.match(pattern, authorization_header)

                if match:
                    return match.group(1)

        return None
