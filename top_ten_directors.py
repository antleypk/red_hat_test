import os, csv, time, json
import mysql.connector
import config, helper





def main():
    table = config.table
    host = config.host
    db = config.db
    usr = config.usr
    pwd = config.pwd
    records = helper.get_data(table, host, db, usr, pwd)
    directors = helper.find_directors(records)
    print('directors length: {}'.format(len(directors)))

if __name__ == '__main__':
    main()