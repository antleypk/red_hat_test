
import data_loader as dl 
import unit_test_util as ut
import config
import mysql.connector
import top_ten_genres as gg
import json

def setup():
    dl.main()

def test_get_data_length():
    host = config.host
    db = config.db
    usr = config.usr
    pwd = config.pwd
    records = gg.get_data('movie_metadata',host, 'rh_test', usr, pwd)
    r_len = len(records)
    expected = 5043
    response = ut.compare(r_len, expected)
    r = {}
    r['name'] ='test_get_data_length'
    r['function'] = 'top_ten_genres.get_data()'
    r['response'] = response
    return r

def get_test_records(): 

    one = {'color': 'Color', 'director_name': 'James Cameron', 'num_critic_for_reviews': 723, 'duration': 178, 'director_facebook_likes': 0, 'actor_3_facebook_likes': 855, 'actor_2_name': 'Joel David Moore', 'actor_1_facebook_likes': 1000, 'gross': 760505847, 'genres': 'Action|Adventure|Fantasy|Sci-Fi', 'actor_1_name': 'CCH Pounder', 'movie_title': 'Avatar\xa0', 'num_voted_users': 886204, 'cast_total_facebook_likes': 4834, 'actor_3_name': 'Wes Studi', 'facenumber_in_poster': 0, 'plot_keywords': 'avatar|future|marine|native|paraplegic', 'movie_imdb_link': 'http://www.imdb.com/title/tt0499549/?ref_=fn_tt_tt_1', 'num_user_for_reviews': 3054, 'movie_language': 'English', 'country': 'USA', 'content_rating': 'PG-13', 'budget': 237000000, 'title_year': 2009, 'actor_2_facebook_likes': 936, 'imdb_score': '7.90', 'aspect_ratio': '1.78', 'movie_facebook_likes': 33000}
 
    two = {'color': 'Color', 'director_name': 'Gore Verbinski', 'num_critic_for_reviews': 302, 'duration': 169, 'director_facebook_likes': 563, 'actor_3_facebook_likes': 1000, 'actor_2_name': 'Orlando Bloom', 'actor_1_facebook_likes': 40000, 'gross': 309404152, 'genres': 'Action|Adventure|Fantasy', 'actor_1_name': 'Johnny Depp', 'movie_title': "Pirates of the Caribbean: At World's End\xa0", 'num_voted_users': 471220, 'cast_total_facebook_likes': 48350, 'actor_3_name': 'Jack Davenport', 'facenumber_in_poster': 0, 'plot_keywords': 'goddess|marriage ceremony|marriage proposal|pirate|singapore', 'movie_imdb_link': 'http://www.imdb.com/title/tt0449088/?ref_=fn_tt_tt_1', 'num_user_for_reviews': 1238, 'movie_language': 'English', 'country': 'USA', 'content_rating': 'PG-13', 'budget': 300000000, 'title_year': 2007, 'actor_2_facebook_likes': 5000, 'imdb_score': '7.10', 'aspect_ratio': '2.35', 'movie_facebook_likes': 0}
 
    three = {'color': 'Color', 'director_name': 'Sam Mendes', 'num_critic_for_reviews': 602, 'duration': 148, 'director_facebook_likes': 0, 'actor_3_facebook_likes': 161, 'actor_2_name': 'Rory Kinnear', 'actor_1_facebook_likes': 11000, 'gross': 200074175, 'genres': 'Action|Adventure|Thriller', 'actor_1_name': 'Christoph Waltz', 'movie_title': 'Spectre\xa0', 'num_voted_users': 275868, 'cast_total_facebook_likes': 11700, 'actor_3_name': 'Stephanie Sigman', 'facenumber_in_poster': 1, 'plot_keywords': 'bomb|espionage|sequel|spy|terrorist', 'movie_imdb_link': 'http://www.imdb.com/title/tt2379713/?ref_=fn_tt_tt_1', 'num_user_for_reviews': 994, 'movie_language': 'English', 'country': 'UK', 'content_rating': 'PG-13', 'budget': 245000000, 'title_year': 2015, 'actor_2_facebook_likes': 393, 'imdb_score': '6.80', 'aspect_ratio': '2.35', 'movie_facebook_likes': 85000}
 
    four = {'color': 'Color', 'director_name': 'Christopher Nolan', 'num_critic_for_reviews': 813, 'duration': 164, 'director_facebook_likes': 22000, 'actor_3_facebook_likes': 23000, 'actor_2_name': 'Christian Bale', 'actor_1_facebook_likes': 27000, 'gross': 448130642, 'genres': 'Action|Thriller', 'actor_1_name': 'Tom Hardy', 'movie_title': 'The Dark Knight Rises\xa0', 'num_voted_users': 1144337, 'cast_total_facebook_likes': 106759, 'actor_3_name': 'Joseph Gordon-Levitt', 'facenumber_in_poster': 0, 'plot_keywords': 'deception|imprisonment|lawlessness|police officer|terrorist plot', 'movie_imdb_link': 'http://www.imdb.com/title/tt1345836/?ref_=fn_tt_tt_1', 'num_user_for_reviews': 2701, 'movie_language': 'English', 'country': 'USA', 'content_rating': 'PG-13', 'budget': 250000000, 'title_year': 2012, 'actor_2_facebook_likes': 23000, 'imdb_score': '8.50', 'aspect_ratio': '2.35', 'movie_facebook_likes': 164000}
 
    five = {'color': '', 'director_name': 'Doug Walker', 'num_critic_for_reviews': None, 'duration': None, 'director_facebook_likes': 131, 'actor_3_facebook_likes': None, 'actor_2_name': 'Rob Walker', 'actor_1_facebook_likes': 131, 'gross': None, 'genres': 'Documentary', 'actor_1_name': 'Doug Walker', 'movie_title': 'Star Wars: Episode VII - The Force Awakens\xa0            ', 'num_voted_users': 8, 'cast_total_facebook_likes': 143, 'actor_3_name': '', 'facenumber_in_poster': 0, 'plot_keywords': '', 'movie_imdb_link': 'http://www.imdb.com/title/tt5289954/?ref_=fn_tt_tt_1', 'num_user_for_reviews': None, 'movie_language': '', 'country': '', 'content_rating': '', 'budget': None, 'title_year': None, 'actor_2_facebook_likes': 12, 'imdb_score': '7.10', 'aspect_ratio': None, 'movie_facebook_likes': 0}

    records = []
    records.append(one)
    records.append(two)
    records.append(three)
    records.append(four)
    records.append(five)

    return records

def test_find_genres(records):
    genres = list(gg.find_genres(records))
    #print(genres)
    expected = ['Action', 'Sci-Fi', 'Thriller', 'Fantasy', 'Adventure', 'Documentary']
    genres.sort()
    expected.sort()
    response = ut.compare(genres, expected)
    r = {}
    r['name'] ='test_find_genres'
    r['function'] = 'top_ten_genres.find_genres()'
    r['response'] = response
    return r

def test_calculate_profitablity():
    gross = 5000
    budget = 4000
    count = 2
    expected = 500
    actual = gg.calculate_profitablity(gross, budget, count)
    response = ut.compare(actual, expected)
    r = {}
    r['name'] ='test_calculate_profitablity'
    r['function'] = 'top_ten_genres.calculate_profitablity()'
    r['response'] = response
    return r

def test_calculate_profitablities(records, genres):
    profitablities = gg.calculate_profitablities(records, genres)

    expected = []
    expected.append({'genre': 'Sci-Fi', 'profitablity': 523505847.0})
    expected.append({'genre': 'Fantasy', 'profitablity': 266454999.5})
    expected.append({'genre': 'Action', 'profitablity': 171528704.0})
    expected.append({'genre': 'Adventure', 'profitablity': 162661391.33333334})
    expected.append({'genre': 'Thriller', 'profitablity': 76602408.5})
    response = ut.compare(profitablities, expected)
    r = {}
    r['name'] ='test_calculate_profitablities'
    r['function'] = 'top_ten_genres.calculate_profitablities()'
    r['response'] = response
    return r

def test_get_movies_by_genre(records):
    genre ='Sci-Fi'
    actual = gg.get_movies_by_genre(genre, records)
    print(actual)
    expected = {'genre': 'Sci-Fi', 'records': [{'color': 'Color', 'director_name': 'James Cameron', 'num_critic_for_reviews': 723, 'duration': 178, 'director_facebook_likes': 0, 'actor_3_facebook_likes': 855, 'actor_2_name': 'Joel David Moore', 'actor_1_facebook_likes': 1000, 'gross': 760505847, 'genres': 'Action|Adventure|Fantasy|Sci-Fi', 'actor_1_name': 'CCH Pounder', 'movie_title': 'Avatar\xa0', 'num_voted_users': 886204, 'cast_total_facebook_likes': 4834, 'actor_3_name': 'Wes Studi', 'facenumber_in_poster': 0, 'plot_keywords': 'avatar|future|marine|native|paraplegic', 'movie_imdb_link': 'http://www.imdb.com/title/tt0499549/?ref_=fn_tt_tt_1', 'num_user_for_reviews': 3054, 'movie_language': 'English', 'country': 'USA', 'content_rating': 'PG-13', 'budget': 237000000, 'title_year': 2009, 'actor_2_facebook_likes': 936, 'imdb_score': '7.90', 'aspect_ratio': '1.78', 'movie_facebook_likes': 33000}]}

    response = ut.compare(actual, expected)
    r = {}
    r['name'] ='test_get_movies_by_genre'
    r['function'] = 'top_ten_genres.get_movies_by_genre()'
    r['response'] = response
    return r

def main():
    setup()
    records = get_test_records()
    genres = ['Action', 'Sci-Fi', 'Thriller', 'Fantasy', 'Adventure', 'Documentary']
    responses = []
    responses.append(test_get_data_length())
    responses.append(test_find_genres(records))
    responses.append(test_calculate_profitablity())
    responses.append(test_calculate_profitablities(records, genres))
    responses.append(test_get_movies_by_genre(records))

    print(' ')
    print('  Results')
    for response in responses:
        ut.printer(response)
    print(' ')


if __name__ == '__main__':
    main()