from passlib.hash import pbkdf2_sha256


def hash(pwd: str):
    return pbkdf2_sha256.hash(pwd)


def verify(plain_password, hashed_password):
    return pbkdf2_sha256.verify(plain_password, hashed_password)