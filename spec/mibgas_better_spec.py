# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from guess_omie_price.mibgas_getter import download_pmc_on_date
from mamba import context, description, it

with description('PMC'):
    with context('PMC getter'):
        with it('Downloads prices for a valid datetime'):
            d = datetime(2022, 7, 16)
            prices = download_pmc_on_date(d)

            res_prices = [x['value'] for x in prices]

            expected_price = 106.66
            assert res_prices[197-1] == expected_price  # 2022-07-16 is the year number 197 on 2022

        with it('Does not fail execution for an invalid datetime'):
            d = datetime.today() + timedelta(days=365)  # next year must not be published yet
            prices = download_pmc_on_date(d)
            assert len(prices) == 0
            assert prices == []

        with it('Downloads prices for specified zone (Spain by default)'):
            d = datetime(2022, 7, 16)
            prices = download_pmc_on_date(d)

            res_prices = [x['value'] for x in prices]

            expected_price = 106.66
            assert res_prices[197-1] == expected_price  # 2022-07-16 is the year number 197 on 2022

            d = datetime(2022, 7, 16)
            prices = download_pmc_on_date(d, 'pt')

            res_prices = [x['value'] for x in prices]

            expected_price = 108.20
            assert res_prices[197-1] == expected_price  # 2022-07-16 is the year number 197 on 2022
