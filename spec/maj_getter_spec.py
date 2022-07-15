# -*- coding: utf-8 -*-
from datetime import datetime
from guess_omie_price.maj_getter import download_maj_on_date
from mamba import context, description, it

with description('MAJ'):
    with context('MAJ getter'):
        with it('Downloads prices for a valid datetime'):
            d = datetime(2022, 6, 15)
            prices = download_maj_on_date(d)
            assert len(prices) == 24

            expected_prices = [65.22, 71.27, 75.24, 79.33, 79.33, 80.71, 79.0, 70.84,
                               61.46, 56.1, 52.13, 48.45, 46.2, 45.5, 44.08, 44.82,
                               46.32, 48.12, 50.7, 53.55, 55.4, 56.44, 57.79, 64.2]

            res_prices = [x['value'] for x in prices]

            assert res_prices == expected_prices

        with it('Does not fail execution for an invalid datetime'):
            d = datetime(2022, 6, 14)
            prices = download_maj_on_date(d)
            assert len(prices) == 0
            assert prices == []

            d = datetime(2023, 6, 1)
            prices = download_maj_on_date(d)
            assert len(prices) == 0
            assert prices == []

        with it('Downloads prices for specified zone (Spain by default)'):
            d = datetime(2022, 7, 14)
            prices = download_maj_on_date(d)
            assert len(prices) == 24

            expected_prices = [165.74, 180.94, 192.07, 207.18, 214.79, 214.58, 205.78, 186.97,
                               168.04, 146.76, 133.99, 125.60, 120.88, 118.01, 116.47, 115.88,
                               112.92, 113.50, 117.78, 123.37, 132.55, 138.14, 138.36, 153.22]

            res_prices = [x['value'] for x in prices]

            assert res_prices == expected_prices

            prices = download_maj_on_date(d, zone='pt')
            assert len(prices) == 24

            expected_prices = [165.74, 180.94, 192.07, 207.18, 214.79, 214.58, 205.78, 186.97,
                               168.04, 146.76, 133.99, 125.60, 120.88, 118.01, 116.47, 115.88,
                               112.92, 113.50, 117.78, 123.37, 132.55, 138.14, 138.36, 153.22]

            res_prices = [x['value'] for x in prices]

            assert res_prices == expected_prices
