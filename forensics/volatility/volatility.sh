# username=$(whoami)

# mkdir -p ~/.local/bin

# sudo apt install -y build-essential git libdistorm3-dev yara libraw1394-11 libcapstone-dev capstone-tool tzdata
# sudo apt install -y python2 python2.7-dev libpython2-dev
# curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
# sudo python2 get-pip.py
# sudo python2 -m pip install -U setuptools wheel
# python2 -m pip install -U distorm3 yara pycrypto pillow openpyxl ujson pytz ipython capstone
# sudo python2 -m pip install yara
# sudo ln -s /usr/local/lib/python2.7/dist-packages/usr/lib/libyara.so /usr/lib/libyara.so
# python2 -m pip install -U git+https://github.com/volatilityfoundation/volatility.git
# mv ~/.local/bin/vol.py ~/.local/bin/vol2.py

# sudo apt install -y python3 python3-dev libpython3-dev python3-pip python3-setuptools python3-wheel
# python3 -m pip install -U distorm3 yara pycrypto pillow openpyxl ujson pytz ipython capstone
# python3 -m pip install -U git+https://github.com/volatilityfoundation/volatility3.git
# mv ~/.local/bin/vol ~/.local/bin/vol3.py

# echo 'export PATH=/home/'"$username"'/.local/bin:$PATH' >> ~/.bashrc
# echo 'export PATH=/home/'"$username"'/.local/bin:$PATH' >> ~/.zshrc

# echo 'Close this shell and open a new one!'
# echo 'vol2.py for volatility2 and vol3.py for volatility3'

mkdir -p ~/Downloads/vol2
cd ~/Downloads/vol2

sudo apt install -y build-essential git libdistorm3-dev yara libraw1394-11 libcapstone-dev capstone-tool tzdata
sudo apt install -y python2 python2.7-dev libpython2-dev python2-dev

curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
sudo python2 get-pip.py
rm get-pip.py
sudo python2 -m pip install -U setuptools wheel
sudo python2 -m pip install virtualenv

virtualenv -p python2 ~/volatility2
source ~/volatility2/bin/activate

python2 -m pip install -U distorm3 pycrypto
python2 -m pip install -U yara pillow openpyxl ujson pytz ipython capstone

git clone https://github.com/volatilityfoundation/volatility.git
cd volatility
python2 setup.py install

echo <<<EOF
#!/bin/bash
source ~/volatility2/bin/activate

EOF >> 


