#!/bin/bash

#running this bash script on a new rhel 8 image will produce desired results

#install git
sudo yum install git -y

#grab the application code
git clone https://github.com/antleypk/red_hat_test.git

#move to application folder
cd red_hat_test

#initialize the application
./init.sh &> out