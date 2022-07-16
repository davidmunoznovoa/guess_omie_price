# -*- coding: utf-8 -*-
from guess_omie_price.utils import download_mibgas_component_on_date
import logging
import zipfile


def download_pmc_on_date(today, zone='es'):
    """
    Downloads PMC data from MIBGAS
    :param today: datetime
    :param zone: str, must be in ('es', 'pt')
    :return: list of dict
    """
    logger = logging.getLogger('MIBGAS')
    logger.info(f'Descargando precios PMC para la fecha {today}.')

    year = today.year

    if year < 2019:
        sheet_number = 6
    else:
        sheet_number = 7

    try:
        base_url = f'https://www.mibgas.es/es/file-access/'
        file_url = f'MIBGAS_Data_{year}.xlsx?path=AGNO_{year}/XLS'

        return download_mibgas_component_on_date(base_url, file_url, sheet_number, zone=zone)

    except IndexError:
        logger.info(f'No se han podido descargar los precios PMC en fecha {today}.')
        return []
    except zipfile.BadZipFile:
        logger.info(f'No se han podido descargar los precios PMC en fecha {today}.')
        return []
