import unit_test_util as ut
import config
import mysql.connector
import top_imdb_pairs as ii


def test_get_data(): 
    records = ii.get_data()
    response = False

    if len(records) == 15:
        if records[0]['pair'] == 'Director: Frank Darabont, Actor: Morgan Freeman':
            response = True
    r = {}
    r['name'] ='test_get_data'
    r['function'] = 'top_imdb_pairs.get_data()'
    r['response'] = response
    return r    

def get_records():
    records = []
    records.append({'pair': 'Director: Quentin Tarantino, Actor: Bruce Willis', 'imdb_score': '8.90'})
    records.append({'pair': 'Director: Peter Jackson, Actor: Bernard Hill', 'imdb_score': '8.90'})
    records.append({'pair': 'Director: Peter Jackson, Actor: Billy Boyd', 'imdb_score': '8.80'})
    records.append({'pair': 'Director: Irvin Kershner, Actor: Kenny Baker', 'imdb_score': '8.80'})
    records.append({'pair': 'Director: Robert Zemeckis, Actor: Siobhan Fallon Hogan', 'imdb_score': '8.80'})
    records.append({'pair': 'Director: Christopher Nolan, Actor: Leonardo DiCaprio', 'imdb_score': '8.80'})
    records.append({'pair': 'Director: David Fincher, Actor: Meat Loaf', 'imdb_score': '8.80'})
    records.append({'pair': 'Director: Robert Zemeckis, Actor: Tom Hanks', 'imdb_score': '8.80'})
    records.append({'pair': 'Director: David Fincher, Actor: Brad Pitt', 'imdb_score': '8.80'})
    records.append({'pair': 'Director: Christopher Nolan, Actor: Joseph Gordon-Levitt', 'imdb_score': '8.80'})
    records.append({'pair': 'Director: Robert Zemeckis, Actor: Sam Anderson', 'imdb_score': '8.80'})
    records.append({'pair': 'Director: Peter Jackson, Actor: Orlando Bloom', 'imdb_score': '8.80'})
    records.append({'pair': 'Director: Christopher Nolan, Actor: Tom Hardy', 'imdb_score': '8.80'})
    records.append({'pair': 'Director: David Fincher, Actor: Eugenie Bondurant', 'imdb_score': '8.80'})
    records.append({'pair': 'Director: Irvin Kershner, Actor: Harrison Ford', 'imdb_score': '8.80'})
    records.append({'pair': 'Director: Irvin Kershner, Actor: Anthony Daniels', 'imdb_score': '8.80'})
    records.append({'pair': 'Director: Peter Jackson, Actor: Christopher Lee', 'imdb_score': '8.80'})
    records.append({'pair': 'Director: Martin Scorsese, Actor: Mike Starr', 'imdb_score': '8.70'})
    records.append({'pair': 'Director: George Lucas, Actor: Peter Cushing', 'imdb_score': '8.70'})
    records.append({'pair': 'Director: George Lucas, Actor: Harrison Ford', 'imdb_score': '8.70'})
    records.append({'pair': 'Director: Martin Scorsese, Actor: Paul Sorvino', 'imdb_score': '8.70'})
    return records


def test_filter_records(records):
    f_records = ii.filter_records(records)
    lcl_records = []
    for f in f_records:
        lcl_records.append(f['pair'])
    
    h_records = []
    h_records.append("Director: Quentin Tarantino, Actor: Bruce Willis")
    h_records.append("Director: Peter Jackson, Actor: Bernard Hill")
    h_records.append("Director: Peter Jackson, Actor: Billy Boyd")
    h_records.append("Director: David Fincher, Actor: Brad Pitt")
    h_records.append("Director: David Fincher, Actor: Meat Loaf")
    h_records.append("Director: Robert Zemeckis, Actor: Siobhan Fallon Hogan")
    h_records.append("Director: Irvin Kershner, Actor: Kenny Baker")
    h_records.append("Director: Christopher Nolan, Actor: Joseph Gordon-Levitt")
    h_records.append("Director: Robert Zemeckis, Actor: Tom Hanks")
    h_records.append("Director: Christopher Nolan, Actor: Leonardo DiCaprio")
    lcl_records.sort()
    h_records.sort()
    response = ut.compare(lcl_records, h_records)
    r = {}
    r['name'] ='test_filter_records_genre'
    r['function'] = 'top_imdb_pairs.filter_records()'
    r['response'] = response
    return r


def machine():
    records = get_records()
    responses = []
    responses.append(test_get_data())
    responses.append(test_filter_records(records))
    return responses


def main():
    responses = machine()

    print(' ')
    print('  Results')
    for response in responses:
        ut.printer(response)


if __name__ == '__main__':
    main()