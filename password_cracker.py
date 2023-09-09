import hashlib

def crack_sha1_hash(sha1_hash, use_salts=False):
    # open the file that contains all the passwords
    with open('top-10000-passwords.txt', 'r') as f:
        # split the file into a list of lines
        passwords = f.read().splitlines()
    # open the file that contains all the salts
    with open('known-salts.txt', 'r') as f:
        salts = f.read().splitlines()
    if use_salts:
        for salt in salts:
            for password in passwords:
                # if the sha1 hash of the salt + password equals the input
                if hashlib.sha1((salt + password).encode()).hexdigest() == sha1_hash:
                    return password
                # if the sha1 hash of the password + salt equals the input
                if hashlib.sha1((password + salt).encode()).hexdigest() == sha1_hash:
                    return password
    else:
        for password in passwords:
            if hashlib.sha1(password.encode()).hexdigest() == sha1_hash:
                return password
    # if the password is not found
    return "PASSWORD NOT IN DATABASE"
