import hashlib

def hash_password(password):
    # create a md5 object
    hasher = hashlib.md5()
    # hash the password
    hasher.update (password.encode('utf-8'))
    # get the hexadecimal representation of the bash
    hashed_password =hasher.hexdigest()
    return hashed_password