# update
sudo apt update
sudo apt upgrade -y

# This is needed for the script to work on ubuntu. works on kali without. 
sudo apt install python3-pip curl -y

sudo pip install -U setuptools

# Install Volatility2
# First, we need to install Python2 and Python2 PIP
# Then install all dependencies
mkdir -p ~/Downloads/vol2
cd ~/Downloads/vol2
sudo apt install -y build-essential git libdistorm3-dev yara libraw1394-11 libcapstone-dev capstone-tool tzdata
sudo apt install -y python2 python2.7-dev libpython2-dev python2-dev
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py
sudo python2 get-pip.py
rm get-pip.py
sudo python2 -m pip install -U pip
sudo python2 -m pip install -U setuptools wheel
#python2 -m virtualenv ~/volatility2_venv
#source ~/volatility2_venv/bin/activate
sudo python2 -m pip install -U distorm3 pycryptodome yara
sudo ln -s /usr/local/lib/python2.7/dist-packages/usr/lib/libyara.so /usr/lib/libyara.so
#ln -s ~/volatility2_venv/lib/python2.7/site-packages/usr/lib/libyara.so ~/volatility2_venv/lib/libyara.so
git clone https://github.com/volatilityfoundation/volatility.git ~/volatility2
cd ~/volatility2
sudo python2 setup.py install

# Install Volatility3
sudo apt install -y python3 python3-dev libpython3-dev python3-pip python3-setuptools python3-wheel
sudo python3 -m pip install -U distorm3 yara pycryptodome pillow openpyxl ujson pytz ipython capstone
git clone https://github.com/volatilityfoundation/volatility3.git ~/volatility3
cd ~/volatility3
sudo python3 setup.py install

# Add Volatility to PATH
echo 'export PATH=~/volatility2:$PATH' >> ~/.bashrc
echo 'export PATH=~/volatility3:$PATH' >> ~/.bashrc
echo 'export PATH=~/volatility2:$PATH' >> ~/.zshrc
echo 'export PATH=~/volatility3:$PATH' >> ~/.zshrc

# Fix shebang so loader knows to use it with Python 2.7
sed -i '1s|.*|#!/usr/bin/env python2.7|' ~/volatility2/vol.py

# Setup linking so we can use vol2.py and vol3.py
# Setup alias so we can also call just vol2 & vol3
ln -s ~/volatility2/vol.py ~/volatility2/vol2.py
ln -s ~/volatility3/vol.py ~/volatility3/vol3.py
chmod +x ~/volatility2/vol2.py
chmod +x ~/volatility3/vol3.py
echo 'alias vol2="vol2.py"' >> ~/.bashrc
echo 'alias vol3="vol3.py"' >> ~/.bashrc
echo 'alias vol2="vol2.py"' >> ~/.zshrc
echo 'alias vol3="vol3.py"' >> ~/.zshrc

echo "Done :D. Open a new shell or type 'source ~/.bashrc'"
