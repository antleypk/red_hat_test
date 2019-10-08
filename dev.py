import data_loader as dl
import unit_test_util as ut
import mysql.connector
import config
# data = dl.get_data('./movie_metadata.csv')

# print('data 1: {}'.format(data[0]))
# print('data len: {}'.format(len(data)))
# d = data[0]
# k = len(d.keys())
# print(k)


conn = mysql.connector.connect(host=config.host,database='test',user=config.usr,password =config.pwd)

ut.clear_table('test', 'movie_metadata')
statement = 'select * from test_movie;'
statement1 ='select * from movie_metadata;'
test = ut.fetch_sql(statement, conn)
actual = ut.fetch_sql(statement1, conn)

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

print('')
print(test_string)
print(' ')
print(actual_string)


if test_string == actual_string:
    print('True')