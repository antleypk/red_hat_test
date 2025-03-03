import os, csv, time, json
import mysql.connector
import config
import unit_test_util as ut

def setup(host=config.host,db=config.db, usr=config.usr, pwd=config.pwd):
    """confirms view, director, has been built; builds if not found"""
    try:
        statement = 'select * from director;'
        conn = mysql.connector.connect(host=config.host,database=db,user=config.usr,password =config.pwd)
        count = ut.fetch_sql(statement, conn)
        conn.close()
    except Exception as e:
        if e.errno == 1146:
            conn = mysql.connector.connect(host=config.host,database=db,user=config.usr,password =config.pwd)
            statement = """
            CREATE VIEW IF NOT EXISTS director AS 
            ( 
                    SELECT   director_name,
                            movie_title, 
                            gross, 
                            budget, 
                            gross-budget AS profit 
                    FROM     movie_metadata 
                    WHERE    gross IS NOT NULL 
                    AND      budget IS NOT NULL 
                    ORDER BY director_name 
            ); """ 
            cursor = conn.cursor()
            cursor.execute(statement)
            conn.commit()
            conn.close()


def get_top_directors(host=config.host,db=config.db, usr=config.usr, pwd=config.pwd):
    """returns top directors from the view: 'director' """
    try:
        conn = mysql.connector.connect(host=host,database=db,user=usr,password=pwd)
        statement = f"""select director_name, avg(profit) as avg_profit 
                    from director
                    group by director_name
                    order by avg_profit desc limit 10;"""
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
        return j_records

    except Exception as e:
        if e.errno == 1146:
            print(f"View '{db}.director' does not exist")

              



def director_printer(directors):
    count = 1
    print('     Results')
    for director in directors:
        profit = director['avg_profit']
        director = director['director_name']
        profit_list = str(profit).split('.')
        big = str(profit_list[0])
        little = str(profit_list[1])
        profit_string = big+'.'+little[:2]
        print(f'{count}: Director: {director}, AVG Profit: {profit_string}') 
        count+=1
    print(' ')


def main():
    setup()
    top_directors = get_top_directors()
    director_printer(top_directors)

if __name__ == '__main__':
    main()