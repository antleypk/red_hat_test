#!/bin/bash

#running this bash script on a new rhel 8 image will produce desired results
# developed and tested on the following:
#               ec2-user$ cat /etc/redhat-release
#               Red Hat Enterprise Linux release 8.0 (Ootpa)       

#install git
sudo yum install git -y

#grab the application code
git clone https://github.com/antleypk/red_hat_test.git

#move to application folder
cd red_hat_test

#initialize the application
sudo ./install.sh &> start_log
