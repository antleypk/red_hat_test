import os, csv, time, json
import mysql.connector
import config
import top_ten_actors

def get_data(host,db, usr, pwd):
    conn = mysql.connector.connect(host=host,database=db,user=usr,password =pwd)
    statement = f""" 
        SELECT director_name, 
            actor_name, 
            Avg(imdb_score) AS avg_score, 
            Count(1) AS knt 
        FROM   actor 
        GROUP  BY director_name, 
                actor_name 
        HAVING knt > 1 
        ORDER  BY knt DESC
        LIMIT 10; 
        """

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


def setup(host, db, usr, pwd):
    conn = mysql.connector.connect(host=host,database=db,user=usr,password =pwd)
    statement = f"""SELECT COUNT(1) as knt FROM actor;"""
    cursor = conn.cursor()
    cursor.execute(statement)
    records =cursor.fetchall()
    record = records[0]
    count = record[0]
    if count != 11670:
        top_ten_actors.main()

def print_pairs(records):
    count = 1
    print(' ')
    print('   TOP TEN TEAMS ')
    for r in records:
        director = r['director_name']
        actor = r['actor_name']
        score = r['avg_score']
        movie_count = r['knt']
        print(f'{count}: Director: {director}, Actor: {actor}, Total Movies: {movie_count}, Average Score: {score}')
        count+=1
    print(' ')

def main():
    host = config.host
    db = config.db
    usr = config.usr
    pwd = config.pwd
    setup(host, db, usr, pwd)
    records = get_data(host,db, usr, pwd)
    print_pairs(records)

if __name__ == '__main__':
    main()