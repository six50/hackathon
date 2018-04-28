"""
Retrieve datasets required for SixFifty hackathon/modelling work.

Execute this script from repo root (i.e. from `/path/to/repo/hackathon/`):
    $ python retrieve_data.py
"""

from pathlib import Path
import requests


# Config
ROOT_DIR = Path('.')


def get_data(filename, repo_path, url='https://s3-eu-west-1.amazonaws.com/sixfifty/'):
    with open(ROOT_DIR / repo_path / filename, 'wb') as f:
        response = requests.get(url + filename)
        f.write(response.content)
    return True


def main():
    # 2010 GE
    print('Downloading 2010 GE results')
    get_data(filename='ge_2010_results.feather',
             repo_path='data/general_election/electoral_commission/results/')
    get_data(filename='ge_2010_results.csv',
             repo_path='data/general_election/electoral_commission/results/')

    # 2015 GE
    print('Downloading 2015 GE results')
    get_data(filename='ge_2015_results.feather',
             repo_path='data/general_election/electoral_commission/results/')
    get_data(url='https://s3-eu-west-1.amazonaws.com/sixfifty/',
             filename='ge_2015_results.csv',
             repo_path='data/general_election/electoral_commission/results/')

    # 2015 GE modelling dataset
    print('Downloading 2015 GE modelling dataset')
    get_data(filename='model_2015.feather',
             repo_path='data/model/')
    get_data(filename='model_2015.csv',
             repo_path='data/model/')

    # EU Referendum
    print('Downloading EU Referendum data')
    get_data(filename='EU-referendum-result-data.csv',
             repo_path='data/eu_referendum/electoral_commission/results/')

    # Polls
    print('Downloading polling data')
    get_data(filename='polls.json',
             repo_path='data/polls/')
    get_data(filename='polls.csv',
             repo_path='data/polls/')
    get_data(filename='polls.feather',
             repo_path='data/polls/')

    print('Downloading regional polling data')
    get_data(filename='polls_london.json',
             repo_path='data/polls/')
    get_data(filename='polls_london.csv',
             repo_path='data/polls/')
    get_data(filename='polls_london.feather',
             repo_path='data/polls/')

    get_data(filename='polls_scotland.json',
             repo_path='data/polls/')
    get_data(filename='polls_scotland.csv',
             repo_path='data/polls/')
    get_data(filename='polls_scotland.feather',
             repo_path='data/polls/')

    get_data(filename='polls_wales.json',
             repo_path='data/polls/')
    get_data(filename='polls_wales.csv',
             repo_path='data/polls/')
    get_data(filename='polls_wales.feather',
             repo_path='data/polls/')

    get_data(filename='polls_ni.json',
             repo_path='data/polls/')
    get_data(filename='polls_ni.csv',
             repo_path='data/polls/')
    get_data(filename='polls_ni.feather',
             repo_path='data/polls/')

    print('Downloading smoothed polling data')
    get_data(filename='polls_smoothed.json',
             repo_path='data/polls/')
    get_data(filename='polls_smoothed.csv',
             repo_path='data/polls/')
    get_data(filename='polls_smoothed.feather',
             repo_path='data/polls/')

    get_data(filename='polls_london_smoothed.json',
             repo_path='data/polls/')
    get_data(filename='polls_london_smoothed.csv',
             repo_path='data/polls/')
    get_data(filename='polls_london_smoothed.feather',
             repo_path='data/polls/')

    get_data(filename='polls_scotland_smoothed.json',
             repo_path='data/polls/')
    get_data(filename='polls_scotland_smoothed.csv',
             repo_path='data/polls/')
    get_data(filename='polls_scotland_smoothed.feather',
             repo_path='data/polls/')

    get_data(filename='polls_wales_smoothed.json',
             repo_path='data/polls/')
    get_data(filename='polls_wales_smoothed.csv',
             repo_path='data/polls/')
    get_data(filename='polls_wales_smoothed.feather',
             repo_path='data/polls/')

    get_data(filename='polls_ni_smoothed.json',
             repo_path='data/polls/')
    get_data(filename='polls_ni_smoothed.csv',
             repo_path='data/polls/')
    get_data(filename='polls_ni_smoothed.feather',
             repo_path='data/polls/')

    print('Downloading averaged final polls')
    get_data(filename='final_polls_2015.csv',
             repo_path='data/polls/')
    get_data(filename='final_polls_2017.csv',
             repo_path='data/polls/')

    # Model-ready datasets
    print('Downloading model-ready datasets')
    get_data(filename='ge10.csv',
             repo_path='data/model/')
    get_data(filename='ge10.feather',
             repo_path='data/model/')
    get_data(filename='ge15.csv',
             repo_path='data/model/')
    get_data(filename='ge15.feather',
             repo_path='data/model/')


if __name__ == "__main__":
    main()
