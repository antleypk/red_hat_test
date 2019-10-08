
import data_loader as dl 
import unit_test_util as ut
import config
import mysql.connector


def setup():
    ut.drop_db('test')
    ut.create_db('test')
    ut.create_test_movie_table('test')
    ut.create_movie_metadata_table('test')
    ut.load_test_movie_table('test')
    data = dl.get_data('./movie_metadata.csv')
    dl.add_data(data, 'movie_metadata', 'test')
    print('--setup complete')



def test_get_data_length():
    data = dl.get_data('./movie_metadata.csv')
    data_length = len(data)
    excpected = 5043

    response = ut.compare(data_length, excpected)
    r = {}
    r['name'] ='test_get_data_length'
    r['function'] = 'data_loader.get_data()'
    r['response'] =response
    return r


def test_get_data_attributes():
    data = dl.get_data('./movie_metadata.csv')
    d_zero = data[0]
    d_keys = d_zero.keys()
    k_len = len(d_keys)
    expected = 28
    response = ut.compare(k_len, expected)
    r = {}
    r['name'] ='test_get_data_attributes'
    r['function'] = 'data.loader.get_data()'
    r['response'] =response
    return r

def test_load_length():
    expected = True
    actual = dl.check_db('test', 'movie_metadata', 5043)
    response = ut.compare(actual, expected)
    r = {}
    r['name'] ='test_get_load_length'
    r['function'] = 'data_loader.add_data()'
    r['response'] =response
    return r

def test_load_attribute():
    db = 'test'
    host = config.host
    usr = config.usr
    pwd = config.pwd
    conn = mysql.connector.connect(host=host,database=db,user=usr,password =pwd)
    conn1 = mysql.connector.connect(host=host,database=db,user=usr,password =pwd)
    ut.clear_table('test', 'movie_metadata')
    data = dl.get_data('./test_movie_metadata.csv')
    dl.add_data(data, 'movie_metadata', 'test')
    statement = 'select * from test_movie;'
    statement1 ='select * from movie_metadata;'
    test = ut.fetch_sql(statement, conn)
    actual = ut.fetch_sql(statement1, conn1)
    test_string = ''
    for t in test:
        lcl_t =f'{t}'
        lcl_t.lower()
        test_string+=lcl_t
    actual_string = ''
    for a in actual:
        lcl_a =f'{t}'
        lcl_a.lower()
        actual_string+=lcl_a
    
    actual_response = False

    expected = True
    if test_string == actual_string:
        actual_response = True
    
    ut.drop_db('test')

    response = ut.compare(actual_response, expected)
    r = {}
    r['name'] ='test_get_load_attribute'
    r['function'] = 'data_loader.add_data()'
    r['response'] =response
    return r



def main():
    setup()
    responses = []
    responses.append(test_get_data_length())
    responses.append(test_get_data_attributes())
    responses.append(test_load_length())
    responses.append(test_load_attribute())

    for response in responses:
        ut.printer(response)


if __name__ == '__main__':
    main()
