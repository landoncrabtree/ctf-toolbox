username=$(whoami)

sudo apt install libgmp3-dev libmpc-dev
sudo git clone https://github.com/RsaCtfTool/RsaCtfTool.git /usr/local/bin/RsaCtfTool
python3 -m pip install -r /usr/local/bin/RsaCtfTool/requirements.txt --user --break-system-packages
echo 'export PATH=/home/'"$username"'/usr/local/bin/RsaCtfTool:PATH' >> ~/.zshrc
echo 'export PATH=/home/'"$username"'/usr/local/bin/RsaCtfTool:$PATH' >> ~/.bashrc
