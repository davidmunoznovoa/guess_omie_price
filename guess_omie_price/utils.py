# -*- coding: utf-8 -*-
from datetime import timedelta
from guess_omie_price.headers import ZONE_MAP
from io import StringIO
from pytz import timezone
import pandas as pd
import requests

LOCAL_TZ = timezone('Europe/Madrid')
UTC_TZ = timezone('UTC')


def download_omie_component_on_date(today, base_url, file_url, file_header, zone):
    """
    Downloads component data from OMIE
    :param today: datetime
    :param base_url: str
    :param file_url: str
    :param file_header: list of str
    :param zone: str, must be in ('es', 'pt')
    :return: list of dict
    """
    url = base_url + file_url
    r = requests.get(url)
    io = StringIO(r.content.decode('ISO-8859-1'))

    df = pd.read_csv(io, sep=';', decimal=',', skiprows=[0, 1, 2, -1], encoding='ISO-8859-1',
                     names=file_header, index_col=False)
    io.close()
    index_pos = ZONE_MAP.get(zone)
    values = list(df.iloc[index_pos])

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
        current_utc_timestamp += timedelta(hours=1)

    return res
