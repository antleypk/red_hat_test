import os, csv, time, json
import mysql.connector

def add_data(data,table, hst, db, usr, pwd):
    print('-- add data --')
    try:
        failures = []
        count = 0
        conn = mysql.connector.connect(host=hst,database=db,user=usr,password =pwd)
        for row in data:
            count+=1
            print('count: {}'.format(count))
            
            
            keys = ['color', 'director_name' , 'num_critic_for_reviews' , 'duration' , 'director_facebook_likes' , 'actor_3_facebook_likes' , 'actor_2_name', 'actor_1_facebook_likes' , 'gross' , 'genres' , 'actor_1_name' , 'movie_title' , 'num_voted_users' , 'cast_total_facebook_likes' , 'actor_3_name' , 'facenumber_in_poster' , 'plot_keywords' , 'movie_imdb_link' , 'num_user_for_reviews' , 'movie_language', 'country' , 'content_rating' , 'budget' , 'title_year', 'actor_2_facebook_likes', 'imdb_score','aspect_ratio','movie_facebook_likes']
            num_keys = ['num_critic_for_reviews','duration', 'director_facebook_likes', 'actor_3_facebook_likes', 'actor_1_facebook_likes', 'gross', 'num_voted_users', 'cast_total_facebook_likes', 'facenumber_in_poster', 'num_user_for_reviews', 'budget', 'title_year', 'actor_2_facebook_likes', 'imdb_score', 'aspect_ratio', 'movie_facebook_likes' ]
  
            vals = "("
            intro_pop = 0
            avatar_pop = 0
            for i in keys:
                lcl_row = row[i]
                if lcl_row == "":
                   # print(f'key: {i}')
                    if i in num_keys:
                        lcl_row = "NULL"
                lcl_data = '"'+lcl_row.replace('"','q')+'",'
                if lcl_row == "NULL":
                    lcl_data = "Null,"
                #lcl_data = '"'+row[i].replace('"','q')+'",'
                #lcl_data = '"'+row[i]+'"'

                vals=vals+lcl_data

            vals = vals[:-1] + ')'                
            keys_string = '{}'.format((keys))
            keys_string = '('+keys_string[1:-1]+')'
            keys_string = keys_string.replace("'","")
            # vals = vals.replace("\xEF\xB8\x8F","specail")
            # vals = vals.replace("\xE2\x80\x8BCel...","specail")

            statement = 'insert into {} {} VALUES {};'.format(table, keys_string,vals)
            print(statement)

            cursor = conn.cursor()
            counter = 0
            interval = 20
            full_counter = 0
            
            try:
                cursor.execute(statement)
                conn.commit()
                
                
            except Exception as e:
                print('bad data e: {}'.format(e))
                statement+=f', error {e}'
                failures.append(statement)
            counter =+1

        conn.close()
        if len(failures) > 0:
            with open('./errors', 'a',newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=",")
                writer.writerow(['time: {}'.format(time.time())])
                for ff in failures:
                    writer.writerow([ff]) 


        return data        

    except Exception as e:
        print('error {}'.format(e))


def get_data(pv_path):
    print('-- get data -- {}'.format(pv_path))
    count = 0
    max = 5050
    with open(pv_path) as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        first = True
        for row in reader:
            if not (first):
                data.append(row)
            if (first):
                first = False
            count+=1
            if count == max:        
                return data
        return data

def main():
    lcl_path = './movie_metadata.csv'
    data = get_data(lcl_path)
    table = 'movie_metadata'
    host = 'localhost'
    db = 'rh_test'
    usr = 'root'
    pwd = 'rh3lt35t'
    add_data(data,table, host, db, usr, pwd)


if __name__ == '__main__':
    main()