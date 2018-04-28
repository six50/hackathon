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


if __name__ == "__main__":
    main()
