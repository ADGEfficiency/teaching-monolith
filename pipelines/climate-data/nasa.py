from ftplib import FTP
from datetime import datetime
from pathlib import Path

import pandas as pd
import requests


class UseCase:
    def __init__(self, database, name):
        self.db = database('climate-data/{}'.format(name))
        self.raw = self.db.setup('raw')
        self.clean = self.db.setup('clean')


class NasaTemperature(UseCase):
    def __init__(self, database):
        super().__init__(database, 'temperature')

    def execute(self):
        print('getting NASA temperatures')
        print('NASA Goddard Institute for Space Studies')
        print('https://data.giss.nasa.gov/gistemp/')

        data = {
            'global': 'https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv',
            'north': 'https://data.giss.nasa.gov/gistemp/tabledata_v4/NH.Ts+dSST.csv',
            'south': 'https://data.giss.nasa.gov/gistemp/tabledata_v4/SH.Ts+dSST.csv'
        }

        for name, url in data.items():
            res = requests.get(url)
            raw_file = self.raw / '{}.csv'.format(name)
            with open(raw_file, 'wb') as fi:
                fi.write(res.content)

            data = pd.read_csv(raw_file, header=1, index_col=0)
            data = data.replace("***", 0)
            data = data.iloc[:-1, :]
            data = data.astype(float)
            data.loc[:, 'Year'] = data.index
            data.index = pd.to_datetime(data.index, format='%Y')
            data.to_csv(self.clean / '{}.csv'.format(name))


class Files:
    """ the Unix filesystem """
    def __init__(self, home):
        self.home = Path.home() / home
        self.home.mkdir(exist_ok=True, parents=True)

    def setup(self, name):
        sub = self.home / name
        sub.mkdir(exist_ok=True, parents=True)
        return sub


class NasaCarbonPPM(UseCase):
    def __init__(self, database):
        super().__init__(database, 'carbon')

    def execute(self):
        print('getting NASA carbon')
        ftp = FTP('aftp.cmdl.noaa.gov')
        ftp.login()
        ftp.cwd('products')
        ftp.cwd('trends')
        ftp.cwd('co2')

        csvs = [fi for fi in ftp.nlst('.') if '.csv' in fi]
        for csv in csvs:
            name = csv
            print('getting {}'.format(name))
            with open(self.raw / name, 'wb') as fp:
                ftp.retrbinary('RETR '+name, fp.write)

            with open(self.raw / name, 'r') as fi:
                for num, line in enumerate(fi):
                    if line[0] != '#':
                        break

            data = pd.read_csv(self.raw / name, skiprows=num)
            try:
                data.index = [datetime(y, m, 1) for y, m in zip(data.loc[:, 'year'], data.loc[:, 'month'])]
                print(name)
            except KeyError:
                pass
            data.to_csv(self.clean / name)


if __name__ == '__main__':
    database = Files
    use_cases = [NasaTemperature, NasaCarbonPPM]

    for uc in use_cases:
        uc = uc(database)
        result = uc.execute()
