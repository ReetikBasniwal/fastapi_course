from passlib.hash import pbkdf2_sha256


def hash(pwd: str):
    return pbkdf2_sha256.hash(pwd)