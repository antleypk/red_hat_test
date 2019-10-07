#!/bin/bash

#machine setup
sudo yum install python3 -y
sudo yum install python3-devel -y
sudo yum install git -y
sudo yum install tmux -y
sudo yum install nano -y

#python setup
sudo pip3 install pipenv
sudo pip3 install wheel
sudo pip3 install mysql-connector==2.1.7
sudp pip3 install kaggle

#mariadb setup
sudo yum install mariadb-server -y
sudo systemctl start mariadb
sudo systemctl enable mariadb
# Make sure that NOBODY can access the server without a password
sudo mysql -e "UPDATE mysql.user SET Password = PASSWORD('rh3lt35t') WHERE User = 'root';"
sudo mysql -e "FLUSH PRIVILEGES;"


