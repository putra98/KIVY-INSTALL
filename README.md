# KIVY
<div style="text-align:center"><img src="https://user-images.githubusercontent.com/53217950/113902933-575e8e00-97c8-11eb-8736-008484b47846.png" /></div>

# Instalasi Menggunakan Ubuntu 18
```
pip3 install --user --upgrade buildozer
sudo apt install python3-pip
sudo apt-get install openjdk-8-jdk
sudo apt update
sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
pip3 install --user --upgrade Cython==0.29.19 virtualenv
export PATH=$PATH:~/.local/bin/
```

# Instalasi Menggunakan MacOS
```
brew install openssl
sudo ln -sfn /usr/local/opt/openssl /usr/local/ssl
brew install pkg-config autoconf automake
python3 -m pip install --user --upgrade Cython==0.29.19 virtualenv
export PATH=$PATH:~/Library/Python/3.7/bin
```

# Instalasi Google Colab
```
!wget https://github.com/HeaTTheatR/KivyMD-data/raw/master/install-kivy-buildozer-dependencies.sh
!chmod +x install-kivy-buildozer-dependencies.sh
!./install-kivy-buildozer-dependencies.sh
!sudo apt update
!sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
!pip install --upgrade Cython==0.29.19 virtualenv
!sudo apt install unzip

```
