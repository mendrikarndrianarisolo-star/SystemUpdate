import sys

def rotate_and_save(input_file, key, output_file):
    try:
        # Lecture du code source
        with open(input_file, 'r', encoding='utf-8') as f:
            data = f.read().encode('utf-8')
        
        # Chiffrement XOR pour la furtivité 2026 [cite: 2025-08-28]
        encrypted = bytearray(data[i] ^ ord(key[i % len(key)]) for i in range(len(data)))
        
        # Écriture physique du fichier chiffré
        with open(output_file, 'wb') as f:
            f.write(encrypted)
        print(f"✅ Génération réussie : {output_file}")
    except Exception as e:
        print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    if len(sys.argv) == 4:
        rotate_and_save(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: python3 rotator.py source.py CLE destination.dat")
