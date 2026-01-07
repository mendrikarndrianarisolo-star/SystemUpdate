sudo apt update
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf > /dev/null
sudo apt update
sudo apt upgrade -y
exit
