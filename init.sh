#!/bin/bash
echo "turn on logging"
set -exou pipefail || echo "logging failed to turn on"
sudo yum update -y || echo "update failed"

#machine setup
echo "machine setup"
sudo yum install python3 -y || echo "python3 failed to install" 
sudo yum install python3-devel -y || echo "python3-devel failed to install"
sudo yum install git -y || echo "git failed to install"
sudo yum install tmux -y || echo "tmux failed to install"
sudo yum install nano -y || echo "nano failed to install"

#python setup
echo "python setup"
sudo pip3 install wheel || echo "wheel failed for python"
sudo pip3 install mysql-connector==2.1.7 || echo "mysql connector failed to set up"


#mariadb setup
echo "mariadb install"
sudo yum install mariadb-server -y || echo "mariadb failed to setup"
sudo systemctl start mariadb || echo "mariadb failed to start"
sudo systemctl enable mariadb || echo "mariadb failed to become enabled at startup"
sudo mysql -e "UPDATE mysql.user SET Password = PASSWORD('rh3lt35t') WHERE User = 'root';"  || echo "root password failed to change for mariadb"
sudo mysql -e "FLUSH PRIVILEGES;" || echo "flush privileges failed"
sudo mysql -h localhost -u root --password='rh3lt35t' -e "create database rh_test;" || echo "create db, rh_test failed"
sudo mysql -h localhost -u root --password='rh3lt35t' rh_test < movie_metadata.sql || echo "failed to create table"
sudo mysql -h localhost -u root --password='rh3lt35t' mysql < svc_user.sql || echo "failed to create svc_user"

sudo python3 data_loader.py || echo "data failed to load into maria db"
sudo python3 top_ten_actors.py || echo "data failed to load to actor table"


