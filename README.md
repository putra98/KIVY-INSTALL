# KIVY & KIVYMD
![1](https://user-images.githubusercontent.com/53217950/113902933-575e8e00-97c8-11eb-8736-008484b47846.png)
![2](https://user-images.githubusercontent.com/53217950/113902943-59285180-97c8-11eb-8617-c7fbf03f35c9.jpg)

# Instalasi Menggunakan Ubuntu 18
```
pip3 install --user --upgrade buildozer

sudo apt install python3-pip

sudo apt-get install openjdk-8-jdk

sudo apt update

sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

pip3 install --user --upgrade Cython==0.29.19 virtualenv  # the --user should be removed if you do this in a venv

add the following line at the end of your ~/.bashrc file

export PATH=$PATH:~/.local/bin/
```

# Instalasi Menggunakan MacOS
```
brew install openssl

sudo ln -sfn /usr/local/opt/openssl /usr/local/ssl

brew install pkg-config autoconf automake

python3 -m pip install --user --upgrade Cython==0.29.19 virtualenv  # the --user should be removed if you do this in a venv

add the following line at the end of your `~/.bashrc` file

export PATH=$PATH:~/Library/Python/3.7/bin
```
