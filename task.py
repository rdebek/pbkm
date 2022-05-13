from ast import AugStore
from hashlib import md5
from re import A

MD5_SECRET = "top secret string value"

# admin: HelloWorld!
# john: HiImJohn!

AUTH_TABLE = [
    ("admin", "86b904e461ee2bee9b05962ba1114c6d"),
    ("john", "29b150b6587619fdcb495ac0ba9ea589"),
]


def hash_password(password: str) -> str:
    result = md5(password.encode("utf-8"))
    result.update(MD5_SECRET.encode("utf-8"))
    return result.hexdigest()


class Authenticator:
    @staticmethod
    def login(username: str, password: str) -> bool:
        password_hash = hash_password(password)
        for user, passwd in AUTH_TABLE:
            if username == user and password_hash == passwd:
                return True
        return False



if __name__ == "__main__":
    pass





