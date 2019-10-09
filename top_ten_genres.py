import os, csv, time, json
import mysql.connector
import config





def find_record_genres(record):
    """Returns the genre for a specific recod"""
    lcl_genres = record['genres'].split('|')
    return lcl_genres

def calculate_profitablity(gross, budget, count):
    """calculate profitablity based (gross, budget, count) for a set of movies in genre"""
    net = gross - budget
    avg = net / count
    return avg

def calculate_profitablities(records, genres):
    """calculates how profitable every genre of movie is"""
    g_profits = []

    for g in genres:
        gross = 0
        budget = 0
        genre_records = get_movies_by_genre(g, records)
        lcl_records = genre_records['records']
        count = 0
        for r in lcl_records:
            lcl_gross = r['gross']
            lcl_budget = r['budget']
            lcl_title = r['movie_title']
            if isinstance(lcl_gross, int):
                if isinstance(lcl_budget, int):
                    gross+=lcl_gross
                    budget+=lcl_budget
                    count+=1
                else:
                    print(f'{lcl_title} has bad budget data, attribute: {lcl_budget}')
            else:
                print(f'{lcl_title}, has bad gross data, attribute: {lcl_gross}')

        if count > 0:
            profitablity = calculate_profitablity(gross, budget, count)
            lcl_f = {}
            lcl_f['genre'] = g
            lcl_f['profitablity'] = profitablity
            g_profits.append(lcl_f)
    
    return sorted(g_profits, key=lambda k: k['profitablity'], reverse=True)


def get_movies_by_genre(genre, records):
    """returns a list of all movies in a specifc genre"""
    lcl_g = {}
    lcl_g['genre'] = genre
    lcl_records = []
    for r in records:
        lcl_gs = find_record_genres(r)
        for lcl_genre in lcl_gs:
            if lcl_genre == genre:
                lcl_records.append(r)
    lcl_g['records'] = lcl_records
    return lcl_g

def profit_printer(profitabalities):
    count = 1
    print('     Results')
    for genre in profitabalities:
        p = str(genre['profitablity']).split('.')
        p_big = p[0]
        p_little = p[1]
        p_little = p_little[:2]
        p = p_big+'.'+p_little
        print("{}: {}, ${}".format(count,genre['genre'], p))
        count+=1

def get_data(table, host,db, usr, pwd):
    """returns all data from a specific table"""
    conn = mysql.connector.connect(host=host,database=db,user=usr,password =pwd)
    statement = f"select * from {table};"
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

def find_genres(records):
    """returns all of the unique genres features in a list of records"""
    genres = set()
    for record in records:
        for genre in find_record_genres(record):
            genres.add(genre)
    return genres

def filter_top_ten(data):
    """trims a sorted list and returns the top ten records"""
    count = 0
    r_list = []
    for item in data:
        if count < 10:
            r_list.append(item)
        count+=1
        if count == 10:
            break
    return r_list


def main():
    table = config.table
    host = config.host
    db = config.db
    usr = config.usr
    pwd = config.pwd
    records = get_data(table, host, db, usr, pwd)
    genres = find_genres(records)
    #print('genres: {}'.format(genres))
    profitabalities = calculate_profitablities(records, genres)
    profit_printer(filter_top_ten(profitabalities))


if __name__ == '__main__':
    main()