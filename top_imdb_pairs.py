import os, csv, time, json
import mysql.connector
import config
import top_ten_actors
import unit_test_util as ut

def get_data(host=config.host,db=config.db, usr=config.usr, pwd=config.pwd):
    """ Gets data from database, returns it as list of dicts"""
    conn = mysql.connector.connect(host=host,database=db,user=usr,password =pwd)
    statement = f"""
    SELECT Concat("Director: ", director_name, ", Actor: ", actor_name) as pair, 
       imdb_score 
        FROM   actor 
        ORDER  BY imdb_score DESC
        limit 15; """

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

def filter_records(records):
    """filters set of records for top ten UNIQUE records"""
    record_set = set()
    for record in records:
        record_set.add(record['pair'])
        if len(record_set) == 10:
            break
    r_records = []
    for rs in record_set:
        for r in records:
             if rs == r['pair']:
                 r_frame = {}
                 r_frame['pair'] = rs
                 r_frame['score'] = r['imdb_score']
                 r_records.append(r_frame)
                 break

    return sorted(r_records, key=lambda k: k['score'], reverse=True)

def setup(host=config.host, db=config.db, usr=config.usr, pwd=config.pwd):
    """confirms actor table is loaded, loads table if not """
    conn = mysql.connector.connect(host=host,database=db,user=usr,password =pwd)
    statement = f"""SELECT COUNT(1) as knt FROM actor;"""
    cursor = conn.cursor()
    cursor.execute(statement)
    records =cursor.fetchall()
    record = records[0]
    count = record[0]
    if count != 11673:
        ut.clear_table(db, 'actor')
        top_ten_actors.main()

def print_pairs(records):
    """Takes list of records and prints them in aesthetic way"""
    count = 1
    print('  TOP TEN IMDB PAIRS ')
    for r in records:
        pair = r['pair']
        score = r['score']
        print(f'{count}: {pair}, IMDB Score: {score}')
        count+=1
    print(' ')

def main():
    setup() 
    records = get_data()
    f_records = filter_records(records)
    print_pairs(f_records)

if __name__ == '__main__':
    main()