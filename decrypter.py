from cryptography.fernet import Fernet
import os

# Lê a chave usada na criptografia
def load_key(key_path="secret.key"):
    with open(key_path, "rb") as key_file:
        return key_file.read()

# Descriptografa um único arquivo
def decrypt_file(file_path, fernet):
    with open(file_path, "rb") as file:
        encrypted = file.read()
    try:
        decrypted = fernet.decrypt(encrypted)
        with open(file_path, "wb") as file:
            file.write(decrypted)
        print(f"[+] Decrypted: {file_path}")
    except Exception as e:
        print(f"[!] Failed to decrypt {file_path}: {e}")

# Descriptografa todos os arquivos da pasta (exceto o script e a chave)
def decrypt_directory(directory, key_path="secret.key"):
    if not os.path.exists(key_path):
        print("[!] Key file not found.")
        return

    key = load_key(key_path)
    fernet = Fernet(key)

    for root, _, files in os.walk(directory):
        for file in files:
            if file in ["encrypter.py", "decrypter.py", "secret.key"]:
                continue
            file_path = os.path.join(root, file)
            decrypt_file(file_path, fernet)

if __name__ == "__main__":
    target_dir = "."  # Pasta atual
    decrypt_directory(target_dir)
