import unit_test_util as ut
import config
import mysql.connector
import top_ten_teams_with_multiple_films as tt

def test_get_data():
    records = tt.get_data()
    response = False

    if len(records) == 10:
        if records[0]['director_name'] == 'Clint Eastwood':
            if records[0]['actor_name'] == 'Clint Eastwood':
                response = True
    r = {}
    r['name'] ='test_get_data'
    r['function'] = 'top_ten_teams_with_multiple_films.get_data()'
    r['response'] = response
    return r 

def test_setup():
    ut.clear_table('rh_test', 'actor')
    tt.setup()
    conn = mysql.connector.connect(host=config.host,database=config.db,user=config.usr,password =config.pwd)
    statement = "select count(1) as knt from actor;"
    knt = ut.fetch_sql(statement, conn)
    count = knt[0]['knt']
    expected = 11673
    response = ut.compare(count, expected)
    r = {}
    r['name'] ='test_setup'
    r['function'] = 'top_ten_teams_with_multiple_films.setup()'
    r['response'] = response
    print(response)
    return r


def main():
    responses = []
    responses.append(test_get_data())
    responses.append(test_setup())

    print(' ')
    print('  Results')
    for response in responses:
        ut.printer(response)

if __name__ == '__main__':
    main()