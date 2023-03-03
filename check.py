import re

def check_name(name: str):
    if len(name) < 2:
        return False
    return True

def check_email(mail: str):
    if re.match("[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", mail):
        return True
    return False

def check_passwd(passwd: str):
    if re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[?!@$%^&*-]).{8,}$", passwd):
        return True
    return False