import unit_test_util as ut
import config
import mysql.connector
import top_ten_directors as dd

def test_setup():
    statement = 'DROP VIEW IF EXISTS director;'
    db = 'rh_test'
    conn = mysql.connector.connect(host=config.host,database=db,user=config.usr,password =config.pwd)
    cursor = conn.cursor()
    cursor.execute(statement)
    conn.commit()
    dd.setup()
    status = None
    statement2 = "SELECT COUNT(1) FROM director;"
    try:
        count = ut.fetch_sql(statement2, conn)
        status = True
    except:
        status = False
    r = {}
    r['name'] ='test_setup'
    r['function'] = 'top_ten_directors.setup()'
    r['response'] = status
    return r

def test_get_top_directors():
    directors = dd.get_top_directors()
    response = False
    if len(directors) == 10:
        if directors[0]['director_name'] == 'Tim Miller':
            response = True
    print(response)

    r = {}
    r['name'] ='test_get_top_directors'
    r['function'] = 'top_ten_directors.get_top_directors()'
    r['response'] = response
    return r

def machine():
    responses = []
    responses.append(test_setup())
    responses.append(test_get_top_directors())
    return responses

def main():
    responses = machine()

    print(' ')
    print('  Results')
    for response in responses:
        ut.printer(response)
    print(' ')
    


if __name__ == '__main__':
    main()