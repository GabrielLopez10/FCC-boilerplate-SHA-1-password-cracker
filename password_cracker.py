import hashlib

def crack_sha1_hash(sha1_hash, use_salts=False):
    with open('top-10000-passwords.txt', 'r') as f:
        passwords = f.read().splitlines()
    with open('known-salts.txt', 'r') as f:
        salts = f.read().splitlines()
    if use_salts:
        for salt in salts:
            for password in passwords:
                if hashlib.sha1((salt + password).encode()).hexdigest() == sha1_hash:
                    return password
                if hashlib.sha1((password + salt).encode()).hexdigest() == sha1_hash:
                    return password
    else:
        for password in passwords:
            if hashlib.sha1(password.encode()).hexdigest() == sha1_hash:
                return password
    return "PASSWORD NOT IN DATABASE"
   