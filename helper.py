import os, csv, time, json
import mysql.connector
import config


def get_data(table, host,db, usr, pwd):
    conn = mysql.connector.connect(host=host,database=db,user=usr,password =pwd)
    statement = f"select * from {table};"
    cursor = conn.cursor()
    cursor.execute(statement)
    records = cursor.fetchall()
    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]    
    j_records = []
    for r in records:
        lcl_record = {}
        index = 0
        for f in field_names:
            lcl_record[f] = r[index]
            index+=1
        j_records.append(lcl_record)
    return j_records

def filter_top_ten(data):
    count = 0
    r_list = []
    for item in data:
        if count < 10:
            r_list.append(item)
        count+=1
        if count == 10:
            break
    return r_list