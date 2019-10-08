import mysql.connector
import config

def create_db(db, host=config.host, usr=config.usr, pwd=config.pwd):
    print(f'--Create Database {db}')
    conn = mysql.connector.connect(host=host,user=usr,password=pwd)
    statement = f"""CREATE DATABASE IF NOT EXISTS {db};"""
    cursor = conn.cursor()
    cursor.execute(statement)
    conn.commit()

def load_test_movie_table(db, host=config.host, usr=config.usr, pwd=config.pwd):
    print(f'--Load Test Movie Table in db: {db}')
    statement =      """   INSERT INTO test_movie
                    (color, 
                    director_name, 
                    num_critic_for_reviews, 
                    duration, 
                    director_facebook_likes, 
                    actor_3_facebook_likes, 
                    actor_2_name, 
                    actor_1_facebook_likes, 
                    gross, 
                    genres, 
                    actor_1_name, 
                    movie_title, 
                    num_voted_users, 
                    cast_total_facebook_likes, 
                    actor_3_name, 
                    facenumber_in_poster, 
                    plot_keywords, 
                    movie_imdb_link, 
                    num_user_for_reviews, 
                    movie_language, 
                    country, 
                    content_rating, 
                    budget, 
                    title_year, 
                    actor_2_facebook_likes, 
                    imdb_score, 
                    aspect_ratio, 
                    movie_facebook_likes) 
        VALUES      ("Color","James Cameron","723","178","0","855","Joel David Moore","1000","760505847","Action|Adventure|Fantasy|Sci-Fi","CCH Pounder","Avatar","886204","4834","Wes Studi","0","avatar|future|marine|native|paraplegic","http://www.imdb.com/title/tt0499549/?ref_=fn_tt_tt_1","3054","English","USA","PG-13","237000000","2009","936","7.9","1.78","33000"); """


    conn = mysql.connector.connect(host=host, database=db, user=usr,password=pwd)
    cursor = conn.cursor()
    cursor.execute(statement)
    conn.commit()

def create_test_movie_table(db, host=config.host, usr=config.usr, pwd=config.pwd):
    print(f'--Create Test Movie Table in db: {db}')
    conn = mysql.connector.connect(host=host, database=db, user=usr,password=pwd)
    statement = """
    CREATE TABLE IF NOT EXISTS test_movie(color VARCHAR(16)
						, director_name VARCHAR(32)
						, num_critic_for_reviews INT(3)
						, duration INT(3)
						, director_facebook_likes INT(5)
						, actor_3_facebook_likes INT(5)
						, actor_2_name VARCHAR(28)
						, actor_1_facebook_likes INT(6)
						, gross INT(9)
						, genres VARCHAR(64)
						, actor_1_name VARCHAR(27)
						, movie_title VARCHAR(87)
						, num_voted_users INT(7)
						, cast_total_facebook_likes INT(6)
						, actor_3_name VARCHAR(29)
						, facenumber_in_poster INT(2)
						, plot_keywords VARCHAR(149)
						, movie_imdb_link VARCHAR(52)
						, num_user_for_reviews INT(4)
						, movie_language VARCHAR(10)
						, country VARCHAR(20)
						, content_rating VARCHAR(9)
						, budget BIGINT(14)
						, title_year INT(4)
						, actor_2_facebook_likes INT(6)
						, imdb_score DECIMAL(4,2)
						, aspect_ratio DECIMAL(4,2)
						, movie_facebook_likes INT(6)); """

    cursor = conn.cursor()
    cursor.execute(statement)
    conn.commit()

def create_actor_table(db, host=config.host, usr=config.usr, pwd=config.pwd):
    print(f'--Create actor Movie Table in db: {db}')
    conn = mysql.connector.connect(host=host, database=db, user=usr,password=pwd)
    statement = """
    CREATE TABLE IF NOT EXISTS actor 
    ( 
        actor_name    VARCHAR(29), 
        movie_title   VARCHAR(87), 
        director_name VARCHAR(32), 
        gross         INT(9), 
        budget        BIGINT(14),
        imdb_score    DECIMAL(4,2) 
    ); 
    """

    cursor = conn.cursor()
    cursor.execute(statement)
    conn.commit()


def create_movie_metadata_table(db, host=config.host, usr=config.usr, pwd=config.pwd):
    print(f'Create movie_metadata in db: {db}')
    statement = """
    CREATE TABLE IF NOT EXISTS movie_metadata(color VARCHAR(16)
						, director_name VARCHAR(32)
						, num_critic_for_reviews INT(3)
						, duration INT(3)
						, director_facebook_likes INT(5)
						, actor_3_facebook_likes INT(5)
						, actor_2_name VARCHAR(28)
						, actor_1_facebook_likes INT(6)
						, gross INT(9)
						, genres VARCHAR(64)
						, actor_1_name VARCHAR(27)
						, movie_title VARCHAR(87)
						, num_voted_users INT(7)
						, cast_total_facebook_likes INT(6)
						, actor_3_name VARCHAR(29)
						, facenumber_in_poster INT(2)
						, plot_keywords VARCHAR(149)
						, movie_imdb_link VARCHAR(52)
						, num_user_for_reviews INT(4)
						, movie_language VARCHAR(10)
						, country VARCHAR(20)
						, content_rating VARCHAR(9)
						, budget BIGINT(14)
						, title_year INT(4)
						, actor_2_facebook_likes INT(6)
						, imdb_score DECIMAL(4,2)
						, aspect_ratio DECIMAL(4,2)
						, movie_facebook_likes INT(6));"""
   
    conn = mysql.connector.connect(host=host, database=db, user=usr,password=pwd)
    cursor = conn.cursor()
    cursor.execute(statement)
    conn.commit()

def compare(val_1, val_2):
    if val_1 == val_2:
        return 'True'
    return 'False'

def printer(jdat):
    response = jdat['response']
    statement = 'Test name: {}, on function: {}, returned: {}'.format(jdat['name'], jdat['function'], response)
    print(statement)

def drop_db(db, host=config.host, usr=config.usr, pwd=config.pwd):
    print(f'--Drop db, {db}')
    try:
        conn = mysql.connector.connect(host=host, database=db, user=usr,password=pwd)
        statement = f"DROP DATABASE IF EXISTS {db};"
        cursor = conn.cursor()
        cursor.execute(statement)
        conn.commit()
        conn.close()
    except:
        print('DB Does Not EXIST')

def fetch_sql(statement, conn):
    cursor = conn.cursor()
    cursor.execute(statement)
    records = cursor.fetchall()
    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]    
    j_records = []
    for r in records:
        lcl_record = {}
        index = 0
        for f in field_names:
            lcl_record[f] = r[index]
            index+=1
        j_records.append(lcl_record)
    
    conn.close()
    return j_records


def clear_table(db, table):
    conn = mysql.connector.connect(host=config.host,database=db,user=config.usr,password =config.pwd)
    statement = f"DELETE FROM {table}"
    cursor = conn.cursor()
    cursor.execute(statement)
    conn.commit()


def main():
    print(f'--unit_test_util.main()')
    create_db('test')
    #create_test_movie_table('test')
    #load_test_movie_table('test')
    #create_movie_metadata_table('test')
    create_actor_table('test')
    #drop_db('test')

if __name__ == '__main__':
    main()