#!/bin/bash

sudo yum install git -y
git clone https://github.com/antleypk/red_hat_test.git
cd red_hat_test
./init.sh &> out