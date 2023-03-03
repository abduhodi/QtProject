class User:
    def __init__(self, username: str='', email: str='', passwd: str='') -> None:
        self.username = username
        self.email = email
        self.passwd = passwd