import db_ut
import data_loader_ut as d
import top_ten_genres_ut as gg 
import top_ten_actors_ut as aa
import top_ten_directors_ut as ddl 
import top_imdb_pairs_ut as ip
import top_ten_teams_with_multiple_films_ut as mf
import unit_test_util as ut

def main():
    response = []
    for db in db_ut.machine():
        response.append(db)

    for dd in d.machine():
        response.append(dd)

    for g in gg.machine():
        response.append(g)

    for a in aa.machine():
        response.append(a)    
 
    for ddd in ddl.machine():
        response.append(ddd)
    
    for i in ip.machine():
        response.append(i)
    
    for m in mf.machine():
        response.append(m)

    fail = False
    print('     Test Results')
    for r in response:
        if r['response'] == False:
            fail = True
        ut.printer(r)

    if fail == True:
        print("Failure Occured")

if __name__ == '__main__':
    main()