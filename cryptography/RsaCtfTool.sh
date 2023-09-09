username=$(whoami)

sudo apt install libgmp3-dev libmpc-dev
mkdir -p ~/.local/bin
git clone https://github.com/RsaCtfTool/RsaCtfTool.git ~/.local/bin/RsaCtfTool
python3 -m pip install -r ~/.local/bin/RsaCtfTool/requirements.txt
echo 'export PATH=/home/'"$username"'/.local/bin/RsaCtfTool:$PATH' >> ~/.zshrc
echo 'export PATH=/home/'"$username"'/.local/bin/RsaCtfTool:$PATH' >> ~/.bashrc
