import os, time
# Accès aux dossiers sensibles (WhatsApp, Photos, Téléchargements) [cite: 2025-08-28]
def total_control():
    paths = ['/sdcard/DCIM/Camera', '/sdcard/WhatsApp/Media', '/sdcard/Download']
    for p in paths:
        try:
            if os.path.exists(p):
                files = os.listdir(p)
                print(f"Extraction {p}: {len(files)} fichiers trouvés")
        except: continue
    # Boucle de maintien en vie [cite: 2025-08-28]
    while True: time.sleep(60)
if __name__ == "__main__": total_control()
