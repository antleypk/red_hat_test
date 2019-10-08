import unittest
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



class LoaderTest(unittest.TestCase):



    def test_get_data_length(self):
        data = dl.get_data('./movie_metadata.csv')
        data_length = len(data)
        excpected = 5042

        self.assertEqual(data_length, excpected)
    
    def test_get_data_attributes(self):
        data = dl.get_data('./movie_metadata.csv')
        d_zero = data[0]
        d_keys = d_zero.keys()
        k_len = len(d_keys)
        expected = 28
        self.assertEqual(k_len, expected)

    def test_load_length(self):
        expected = True
        actual = dl.check_db('test', 'movie_metadata', 5042)
        self.assertEqual(actual, expected)

    # def test_load_attribute(self)
        

    #     conn = mysql.connector.connect(host=config.host,database='test',user=config.user,password =config.pwd)
    #     statement = 'select * from test_movie;'
    #     statement1 ='select * from movie_metadata limit 5;'
    #     test = ut.fetch_sql(statement, conn)
    #     actual = ut.fetch_sql(statement1, conn)


if __name__ == '__main__':
    print(' ')
    print('--data_loader_ut.py')
    setup()
    unittest.main()
