import unit_test_util as ut
import config
import mysql.connector

def check_db():
    response = False
    try:
        conn = mysql.connector.connect(host=config.host,database=config.db,user=config.usr,password=config.pwd)
        response = True
        conn.close()
    except Exception as e:
        if e.errno == 1049:
            print('DB from config file DNE')
    r = {}
    r['name'] ='check_db'
    r['function'] = 'check if db is available'
    r['response'] = response
    return r

def check_movie_metadata():
    response = False
    try:
       conn = mysql.connector.connect(host=config.host,database=config.db,user=config.usr,password=config.pwd)
       statement = "select * from movie_metadata;"
       ut.fetch_sql(statement, conn)
       response = True
    except Exception as e:
        if e.errno == 1146:
            print("table movie_metadata DNE")
    r = {}
    r['name'] ='check_movie_metadata'
    r['function'] = 'check if table movie_metadata is available'
    r['response'] = response
    return r
        
def check_actor():
    response = False
    try:
       conn = mysql.connector.connect(host=config.host,database=config.db,user=config.usr,password=config.pwd)
       statement = "select * from actor;"
       ut.fetch_sql(statement, conn)
       response = True
    except Exception as e:
        if e.errno == 1146:
            print("table actor DNE")
    r = {}
    r['name'] ='check_actor'
    r['function'] = 'check if table actor is available'
    r['response'] = response
    return r
        
def check_director():
    response = False
    try:
       conn = mysql.connector.connect(host=config.host,database=config.db,user=config.usr,password=config.pwd)
       statement = "select * from director;"
       ut.fetch_sql(statement, conn)
       response = True
    except Exception as e:
        if e.errno == 1146:
            print("view director DNE")
    r = {}
    r['name'] ='check_director'
    r['function'] = 'check if view direcotr is available'
    r['response'] = response
    return r

def main():
    responses = []
    responses.append(check_db())
    responses.append(check_movie_metadata())
    responses.append(check_actor())
    responses.append(check_director())

    print(' ')
    print('  Results')
    for response in responses:
        ut.printer(response)
    print(' ')



if __name__ == '__main__':
    main()