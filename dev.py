import config
import top_ten_genres as gg
host = config.host
db = config.db
usr = config.usr
pwd = config.pwd
records = gg.get_data('movie_metadata',host, 'rh_test', usr, pwd)
# print('      ')
# print (' records ')
# print('  ')
# # for record in records:
# #     print(record)
# #     print(' ')

r_len = len(records)
print(r_len)