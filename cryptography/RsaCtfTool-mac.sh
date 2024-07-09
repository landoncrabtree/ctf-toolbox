brew install libmpc gmp
git clone https://github.com/RsaCtfTool/RsaCtfTool.git
cd RsaCtfTool
python3 -m venv venv
source venv/bin/activate
CXX=g++-14 CC=gcc-14 LD=g++-14 pip install -r requirements.txt
