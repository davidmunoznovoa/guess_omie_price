# -*- coding: utf-8 -*-
from guess_omie_price.headers import PBC_HEADER
from guess_omie_price.utils import download_omie_component_on_date
import logging


def download_pbc_on_date(today, zone='es'):
    """
    Downloads daily market hourly price data from OMIE
    :param today: datetime
    :param zone: str, must be in ('es', 'pt')
    :return: list of dict
    """
    logger = logging.getLogger('OMIE')
    logger.info(f'Descargando precios OMIE para la fecha {today}.')

    year = str(today.year)
    month = str(today.month).zfill(2)
    day = str(today.day).zfill(2)

    try:
        base_url = 'https://www.omie.es/sites/default/files/dados/'
        file_url = f'AGNO_{year}/MES_{month}/TXT/INT_PBC_EV_H_1_{day}_{month}_{year}_{day}_{month}_{year}.TXT'

        return download_omie_component_on_date(today, base_url, file_url, PBC_HEADER, zone=zone)

    except IndexError:
        logger.info(f'No se han podido descargar los precios OMIE en fecha {today}.')
        return []
