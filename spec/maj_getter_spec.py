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

            expected_prices = [65.15, 71.2, 75.17, 79.26, 79.26, 80.64, 78.92, 70.75,
                               61.39, 56.04, 52.07, 48.4, 46.15, 45.45, 44.08, 44.79,
                               46.28, 48.08, 50.65, 53.53, 55.5, 56.54, 57.69, 64.11]

            res_prices = [x['value'] for x in prices]

            assert res_prices == expected_prices

        with it('Does not fail execution for an invalid datetime'):
            d = datetime(2022, 5, 14)
            prices = download_maj_on_date(d)
            assert len(prices) == 0
            assert prices == []

            d = datetime(2023, 5, 1)
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
