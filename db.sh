#!/bin/bash
set -exou pipefail
echo "build table to hold data"
sudo mysql -h localhost -u root --password='rh3lt35t' rh_test < movie_metadata.sql || echo "failed to create table"
echo "load movie data into table 'rh_test.movie_metadata'"
sudo python3 data_loader.py