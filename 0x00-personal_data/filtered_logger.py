#!/usr/bin/env python3

"""obfuscating Personal Identifiable Information"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    This function obfuscates the specified 'fields of the given 'message'
    """
    for field in fields:
        message = re.sub(rf"(?<={field}=)[^{separator}]*", redaction, message)
    return message
