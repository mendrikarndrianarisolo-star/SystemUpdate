#!/bin/bash

# Couleurs pour un terminal propre
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}--- 🔐 LANCEMENT DU CHIFFREMENT (ROTATOR) ---${NC}"

# 1. Exécution du rotator pour générer payload.dat et control.txt
python3 rotator.py

# On vérifie si le rotator a réussi (code de sortie 0)
if [ $? -eq 0 ]; then
    echo -e "${GREEN}--- ✅ CHIFFREMENT REUSSI ---${NC}"
    
    echo -e "${GREEN}--- 🛰️ SYNCHRONISATION GITHUB ---${NC}"
    
    # 2. Ajout des fichiers modifiés
    git add main.py rotator.py loader.py payload.dat control.txt ghost_push.sh
    
    # 3. Création du commit avec la date actuelle pour le suivi [cite: 2025-08-28]
    git commit -m "Update Ghost Engine v3.0 - $(date +'%H:%M:%S')"
    
    # 4. Envoi vers ton dépôt SystemUpdate
    git push origin main
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}--- 🚀 TOUT EST EN LIGNE ET PRET ! ---${NC}"
    else
        echo -e "${RED}--- ❌ ERREUR LORS DU PUSH GITHUB ---${NC}"
    fi
else
    echo -e "${RED}--- ❌ ERREUR : LE CHIFFREMENT A ECHOUE ---${NC}"
    exit 1
fi
