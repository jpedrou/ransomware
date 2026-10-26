from cryptography.fernet import Fernet
from main import load_key, search_files

def decrypt_file(file, key):
    f = Fernet(key)

    with open(file, "rb") as fl:
        data = fl.read()
        decrypted_file = f.decrypt(data)

    with open(file, "wb") as fl:
        fl.write(decrypted_file)

def run():
    key = load_key()
    files = search_files("test_files")

    for file in files:
        decrypt_file(file, key)

    print("Files recovered successfully")

if __name__ == "__main__":
    run()