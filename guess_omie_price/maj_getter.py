# -*- coding: utf-8 -*-
from datetime import timedelta
from guess_omie_price.headers import MAJ_HEADER
from guess_omie_price.utils import LOCAL_TZ, UTC_TZ
from io import StringIO
import logging
import pandas as pd
import requests


def download_maj_on_date(today):
    """
    Downloads MAJ data from OMIE
    :param today: datetime
    :return: list of dict
    """
    logger = logging.getLogger('OMIE')
    logger.info(f'Descargando precios MAJ para la fecha {today}.')

    year = str(today.year)
    month = str(today.month).zfill(2)
    day = str(today.day).zfill(2)

    try:
        base_url = 'https://www.omie.es/sites/default/files/dados/'
        file_url = f'AGNO_{year}/MES_{month}/TXT/INT_MAJ_EV_H_{day}_{month}_{year}_{day}_{month}_{year}.TXT'
        url = base_url + file_url
        r = requests.get(url)
        io = StringIO(r.content.decode('ISO-8859-1'))
        df = pd.read_csv(io, sep=';', decimal=',', skiprows=[0, 1, 2, -1], encoding='ISO-8859-1',
                         names=MAJ_HEADER, index_col=False)
        io.close()
        values = list(df.iloc[0])

        current_utc_timestamp = today.astimezone(UTC_TZ) + timedelta(hours=1)

        res = []
        for val in values[1:]:
            register = {}
            local_timestamp = LOCAL_TZ.normalize(current_utc_timestamp.astimezone(LOCAL_TZ))
            utc_timestamp = current_utc_timestamp
            register['local_timestamp'] = local_timestamp.strftime('%Y-%m-%d %H:%M:%S')
            register['utc_timestamp'] = utc_timestamp.strftime('%Y-%m-%d %H:%M:%S')
            register['value'] = val

            res.append(register)

        res = sorted(res, key=lambda d: d['utc_timestamp'])
        return res

    except IndexError:
        logger.info(f'No se han podido descargar los precios MAJ en fecha {today}.')
        return []
