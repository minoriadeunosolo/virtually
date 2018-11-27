"""
    Auxiliary function used in the three tasks.
"""
import re


def param_int(str, min_value=None, max_value=None):
    str = str.strip()
    if not str:
        return None
    if str[0] in ('-', '+'):
        if str[1:].isdigit():
            value = int(str)
    elif str.isdigit():
        value = int(str)
    else:
        value = None

    if value:
        if min_value:
            if value < min_value:
                value = None
        if max_value:
            if value > max_value:
                value = None

    return value


def param_string(str, min_len=None, max_len=None, az=False):
    s = str.strip()
    if min_len:
        if len(s) < min_len:
            return None
    if max_len:
        if len(s) > max_len:
            return None
    if az:
        if not Isascii_Az(s):
            return None
    return s


def Isascii_Az(text):
    if re.match('^[a-z]+$', text):
        return True
    else:
        return False
