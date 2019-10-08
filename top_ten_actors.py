import os, csv, time, json
import mysql.connector
import config

def get_data(host,db, usr, pwd):
    conn = mysql.connector.connect(host=host,database=db,user=usr,password =pwd)
    statement = f"""
            SELECT gross, 
            budget, 
            actor_1_name, 
            actor_2_name, 
            actor_3_name, 
            movie_title,
            director_name,
            imdb_score 
        FROM   movie_metadata 
        WHERE  gross IS NOT NULL 
            AND budget IS NOT NULL; """

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

def transform_records(records, host, db, usr, pwd):
    conn = mysql.connector.connect(host=host,database=db,user=usr,password =pwd)
    for record in records:
       # print(record)
        gross = record['gross']
        budget = record['budget']
        movie = record['movie_title']
        director = record['director_name']
        actor_1_name = record['actor_1_name']
        imdb = record['imdb_score']
        #print('actor 1 name: {}'.format(actor_1_name))
        actor_2_name = record['actor_2_name']
        #print('actor 2 name: {}'.format(actor_2_name))
        actor_3_name = record['actor_3_name']
        #print('actor 3 name: {}'.format(actor_3_name))
        if actor_1_name is not None:
            conn = load_record(gross, budget, movie, director, actor_1_name, imdb,  conn)
        if actor_2_name is not None:
            conn = load_record(gross, budget, movie, director, actor_2_name, imdb, conn)
        if actor_3_name is not None:
            conn = load_record(gross, budget, movie, director, actor_3_name, imdb, conn)

def load_record(gross, budget, movie, director, actor, imdb, conn):
    statement = f"""insert into actor (actor_name, movie_title, director_name, gross, budget, imdb_score)
                    values ("{actor}", "{movie}", "{director}", "{gross}", "{budget}", "{imdb}") """
    print(statement)
    print(' ')
    cursor = conn.cursor()
    cursor.execute(statement)
    conn.commit()
    return conn    

def setup(host, db, usr, pwd):
    conn = mysql.connector.connect(host=host,database=db,user=usr,password =pwd)
    statement = f"""SELECT COUNT(1) as knt FROM actor;"""
    cursor = conn.cursor()
    cursor.execute(statement)
    records =cursor.fetchall()
    record = records[0]
    count = record[0]
    if count != 11670:
        delete(host, db, usr, pwd)
        records = get_data(host,db, usr, pwd)
        transform_records(records, host, db, usr, pwd)

def delete(host,db, usr, pwd):
    
    conn = mysql.connector.connect(host=host,database=db,user=usr,password =pwd)
    statement = "DELETE FROM actor;"

    cursor = conn.cursor()
    cursor.execute(statement)
    conn.commit()

def get_top_ten(host, db, usr, pwd):
    conn = mysql.connector.connect(host=host,database=db,user=usr,password =pwd)
    statement = f"""
        SELECT a.actor_name, 
        Avg (a.profit) AS profit 
        FROM   (SELECT actor_name, 
                    gross, 
                    budget, 
                    gross - budget AS profit 
                FROM   actor) a 
        GROUP  BY actor_name 
        ORDER  BY profit DESC 
        LIMIT  10;    
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

def actor_printer(actors):
    count = 1
    print('    Results')
    for actor in actors:
        lcl_actor = actor['actor_name']
        profit = actor['profit']
        profit_list = str(profit).split('.')
        big = str(profit_list[0])
        little = str(profit_list[1])
        profit_string = big+'.'+little[:2]
        print(f'{count}: Actor: {lcl_actor}, AVG Profit: {profit_string}')
        count+=1
    print(' ')

def main():
    host = config.host
    db = config.db
    usr = config.usr
    pwd = config.pwd
    setup(host, db, usr, pwd)
    top_ten = get_top_ten(host, db, usr, pwd)
    actor_printer(top_ten)



if __name__ == '__main__':
    main()