# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from guess_omie_price.pbc_getter import download_pbc_on_date
from mamba import context, description, it

with description('PMD'):
    with context('PMD getter'):
        with it('Downloads prices for a valid datetime'):
            d = datetime(2022, 6, 15)
            prices = download_pbc_on_date(d)
            assert len(prices) == 24

            expected_prices = [194.07, 183.50, 177.67, 173.02, 173.18, 180.03, 175.56, 178.91,
                               178.91, 165.56, 154.85, 153.21, 154.55, 155.40, 153.00, 144.17,
                               148.00, 145.99, 145.00, 157.07, 178.91, 180.03, 175.56, 148.00]

            res_prices = [x['value'] for x in prices]

            assert res_prices == expected_prices

        with it('Does not fail execution for an invalid datetime'):
            d = datetime.today() + timedelta(days=2)
            prices = download_pbc_on_date(d)
            assert len(prices) == 0
            assert prices == []
