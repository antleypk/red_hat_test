import data_loader as dl 
import unit_test_util as ut
import data_loader as dl
import config
import mysql.connector
import top_ten_actors as aa

def setup():
    ut.create_db('test')
    ut.create_actor_table('test')

def test_get_data():
    r_count = len(aa.get_data())
    print('r count: {}'.format(r_count))
    expected = 3891
    response = ut.compare(r_count, expected)
    r = {}
    r['name'] ='test_get_data_length'
    r['function'] = 'top_ten_actors.get_data()'
    r['response'] = response
    return r

def test_transform_records():
    ut.clear_table('test','actor')
    record = {}
    record['gross'] = 5000
    record['budget'] = 6000
    record['movie_title'] = 'test'
    record['director_name'] = 'peter antley'
    record['actor_1_name'] = 'tyler childers'
    record['imdb_score'] = 9.9
    record['actor_2_name'] = 'tyler moore'
    record['actor_3_name'] = 'hugo antley'
    records = [record]

    aa.transform_records(records, config.host, 'test', config.usr, config.pwd)

    expected = True
    actual = dl.check_db('test', 'actor', 3)
    response = ut.compare(actual, expected)
    r = {}
    r['name'] ='test_transform records'
    r['function'] = 'top_ten_actors.transform_records()'
    r['response'] = response
    return r

def test_load_record():
    ut.clear_table('test','actor')
    gross = 700
    budget = 300
    movie = 'a day at the park'
    actor = 'hugo the dog'
    director = 'peter antley'
    imdb = 7.3
    db = 'test'
    conn = mysql.connector.connect(host=config.host,database=db,user=config.usr,password =config.pwd)
    r_conn = aa.load_record(gross, budget, movie, director, actor, imdb, conn)
    statement = "select * from actor;"
    datas = ut.fetch_sql(statement, r_conn)
    data = datas[0]
    lcl_actor = data['actor_name']
    response = ut.compare(lcl_actor, actor)
    ut.clear_table('test','actor')
    r = {}
    r['name'] ='test_load_record'
    r['function'] = 'top_ten_actors.load_record()'
    r['response'] = response
    return r

def machine():    
    setup()
    
    responses = []
    responses.append(test_get_data())
    responses.append(test_transform_records())
    responses.append(test_load_record())
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
