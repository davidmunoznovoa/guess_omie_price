# guess_omie_price

:snake: :zap: :moneybag:

![](https://github.com/davidmunoznovoa/guess_omie_price/actions/workflows/python3.10-app.yml/badge.svg)
![](https://github.com/davidmunoznovoa/guess_omie_price/actions/workflows/python3.10-app.yml)
![](https://github.com/davidmunoznovoa/guess_omie_price/actions/workflows/python3.9-app.yml/badge.svg)
![](https://github.com/davidmunoznovoa/guess_omie_price/actions/workflows/python3.9-app.yml)
![](https://github.com/davidmunoznovoa/guess_omie_price/actions/workflows/python3.8-app.yml/badge.svg)
![](https://github.com/davidmunoznovoa/guess_omie_price/actions/workflows/python3.8-app.yml)
![](https://github.com/davidmunoznovoa/guess_omie_price/actions/workflows/python3.7-app.yml/badge.svg)
![](https://github.com/davidmunoznovoa/guess_omie_price/actions/workflows/python3.7-app.yml)

- Herramienta para tratar de predecir el precio de mercado de OMIE a futuros.
- También permite descargar distintos ficheros a tener en cuenta para las predicciones, como por ejemplo los siguientes:
  - El precio horario del mercado diario desde OMIE.
  - El precio horario de ajuste a los consumidores en el mercado desde OMIE.
  - El precio marginal de compra del gas desde MIBGAS.

## Ejemplos de uso

- Descargar `Precio horario del mercado diario`

```python
from datetime import datetime
from guess_omie_price.pbc_getter import download_pbc_on_date

d = datetime(2022, 4, 13)
prices = download_pbc_on_date(d)

print(*prices, sep='\n')
```

# Resultado
```
{'local_timestamp': '2022-04-13 01:00:00', 'utc_timestamp': '2022-04-12 23:00:00', 'value': 242.75, 'zone': 'es'}
{'local_timestamp': '2022-04-13 02:00:00', 'utc_timestamp': '2022-04-13 00:00:00', 'value': 229.77, 'zone': 'es'}
{'local_timestamp': '2022-04-13 03:00:00', 'utc_timestamp': '2022-04-13 01:00:00', 'value': 220.0, 'zone': 'es'}
{'local_timestamp': '2022-04-13 04:00:00', 'utc_timestamp': '2022-04-13 02:00:00', 'value': 201.85, 'zone': 'es'}
{'local_timestamp': '2022-04-13 05:00:00', 'utc_timestamp': '2022-04-13 03:00:00', 'value': 190.9, 'zone': 'es'}
{'local_timestamp': '2022-04-13 06:00:00', 'utc_timestamp': '2022-04-13 04:00:00', 'value': 212.32, 'zone': 'es'}
{'local_timestamp': '2022-04-13 07:00:00', 'utc_timestamp': '2022-04-13 05:00:00', 'value': 248.74, 'zone': 'es'}
{'local_timestamp': '2022-04-13 08:00:00', 'utc_timestamp': '2022-04-13 06:00:00', 'value': 257.02, 'zone': 'es'}
{'local_timestamp': '2022-04-13 09:00:00', 'utc_timestamp': '2022-04-13 07:00:00', 'value': 260.0, 'zone': 'es'}
{'local_timestamp': '2022-04-13 10:00:00', 'utc_timestamp': '2022-04-13 08:00:00', 'value': 254.25, 'zone': 'es'}
{'local_timestamp': '2022-04-13 11:00:00', 'utc_timestamp': '2022-04-13 09:00:00', 'value': 242.75, 'zone': 'es'}
{'local_timestamp': '2022-04-13 12:00:00', 'utc_timestamp': '2022-04-13 10:00:00', 'value': 234.99, 'zone': 'es'}
{'local_timestamp': '2022-04-13 13:00:00', 'utc_timestamp': '2022-04-13 11:00:00', 'value': 227.67, 'zone': 'es'}
{'local_timestamp': '2022-04-13 14:00:00', 'utc_timestamp': '2022-04-13 12:00:00', 'value': 208.0, 'zone': 'es'}
{'local_timestamp': '2022-04-13 15:00:00', 'utc_timestamp': '2022-04-13 13:00:00', 'value': 201.18, 'zone': 'es'}
{'local_timestamp': '2022-04-13 16:00:00', 'utc_timestamp': '2022-04-13 14:00:00', 'value': 196.0, 'zone': 'es'}
{'local_timestamp': '2022-04-13 17:00:00', 'utc_timestamp': '2022-04-13 15:00:00', 'value': 200.47, 'zone': 'es'}
{'local_timestamp': '2022-04-13 18:00:00', 'utc_timestamp': '2022-04-13 16:00:00', 'value': 221.2, 'zone': 'es'}
{'local_timestamp': '2022-04-13 19:00:00', 'utc_timestamp': '2022-04-13 17:00:00', 'value': 219.28, 'zone': 'es'}
{'local_timestamp': '2022-04-13 20:00:00', 'utc_timestamp': '2022-04-13 18:00:00', 'value': 242.36, 'zone': 'es'}
{'local_timestamp': '2022-04-13 21:00:00', 'utc_timestamp': '2022-04-13 19:00:00', 'value': 254.0, 'zone': 'es'}
{'local_timestamp': '2022-04-13 22:00:00', 'utc_timestamp': '2022-04-13 20:00:00', 'value': 259.0, 'zone': 'es'}
{'local_timestamp': '2022-04-13 23:00:00', 'utc_timestamp': '2022-04-13 21:00:00', 'value': 250.0, 'zone': 'es'}
{'local_timestamp': '2022-04-14 00:00:00', 'utc_timestamp': '2022-04-13 22:00:00', 'value': 231.94, 'zone': 'es'}
```

- Descargar `Precio horario de ajuste a los consumidores en el mercado`

```python
from datetime import datetime
from guess_omie_price.maj_getter import download_maj_on_date

d = datetime(2022, 6, 15)
prices = download_maj_on_date(d)

print(*prices, sep='\n')
```

# Resultado
```
{'local_timestamp': '2022-06-15 01:00:00', 'utc_timestamp': '2022-06-14 23:00:00', 'value': 65.22, 'zone': 'es'}
{'local_timestamp': '2022-06-15 02:00:00', 'utc_timestamp': '2022-06-15 00:00:00', 'value': 71.27, 'zone': 'es'}
{'local_timestamp': '2022-06-15 03:00:00', 'utc_timestamp': '2022-06-15 01:00:00', 'value': 75.24, 'zone': 'es'}
{'local_timestamp': '2022-06-15 04:00:00', 'utc_timestamp': '2022-06-15 02:00:00', 'value': 79.33, 'zone': 'es'}
{'local_timestamp': '2022-06-15 05:00:00', 'utc_timestamp': '2022-06-15 03:00:00', 'value': 79.33, 'zone': 'es'}
{'local_timestamp': '2022-06-15 06:00:00', 'utc_timestamp': '2022-06-15 04:00:00', 'value': 80.71, 'zone': 'es'}
{'local_timestamp': '2022-06-15 07:00:00', 'utc_timestamp': '2022-06-15 05:00:00', 'value': 79.0, 'zone': 'es'}
{'local_timestamp': '2022-06-15 08:00:00', 'utc_timestamp': '2022-06-15 06:00:00', 'value': 70.84, 'zone': 'es'}
{'local_timestamp': '2022-06-15 09:00:00', 'utc_timestamp': '2022-06-15 07:00:00', 'value': 61.46, 'zone': 'es'}
{'local_timestamp': '2022-06-15 10:00:00', 'utc_timestamp': '2022-06-15 08:00:00', 'value': 56.1, 'zone': 'es'}
{'local_timestamp': '2022-06-15 11:00:00', 'utc_timestamp': '2022-06-15 09:00:00', 'value': 52.13, 'zone': 'es'}
{'local_timestamp': '2022-06-15 12:00:00', 'utc_timestamp': '2022-06-15 10:00:00', 'value': 48.45, 'zone': 'es'}
{'local_timestamp': '2022-06-15 13:00:00', 'utc_timestamp': '2022-06-15 11:00:00', 'value': 46.2, 'zone': 'es'}
{'local_timestamp': '2022-06-15 14:00:00', 'utc_timestamp': '2022-06-15 12:00:00', 'value': 45.5, 'zone': 'es'}
{'local_timestamp': '2022-06-15 15:00:00', 'utc_timestamp': '2022-06-15 13:00:00', 'value': 44.08, 'zone': 'es'}
{'local_timestamp': '2022-06-15 16:00:00', 'utc_timestamp': '2022-06-15 14:00:00', 'value': 44.82, 'zone': 'es'}
{'local_timestamp': '2022-06-15 17:00:00', 'utc_timestamp': '2022-06-15 15:00:00', 'value': 46.32, 'zone': 'es'}
{'local_timestamp': '2022-06-15 18:00:00', 'utc_timestamp': '2022-06-15 16:00:00', 'value': 48.12, 'zone': 'es'}
{'local_timestamp': '2022-06-15 19:00:00', 'utc_timestamp': '2022-06-15 17:00:00', 'value': 50.7, 'zone': 'es'}
{'local_timestamp': '2022-06-15 20:00:00', 'utc_timestamp': '2022-06-15 18:00:00', 'value': 53.55, 'zone': 'es'}
{'local_timestamp': '2022-06-15 21:00:00', 'utc_timestamp': '2022-06-15 19:00:00', 'value': 55.4, 'zone': 'es'}
{'local_timestamp': '2022-06-15 22:00:00', 'utc_timestamp': '2022-06-15 20:00:00', 'value': 56.44, 'zone': 'es'}
{'local_timestamp': '2022-06-15 23:00:00', 'utc_timestamp': '2022-06-15 21:00:00', 'value': 57.79, 'zone': 'es'}
{'local_timestamp': '2022-06-16 00:00:00', 'utc_timestamp': '2022-06-15 22:00:00', 'value': 64.2, 'zone': 'es'}
```

- Descargar `Precio marginal de compra de MIBGAS`

```python
from datetime import datetime
from guess_omie_price.mibgas_getter import download_pmc_on_date

d = datetime(2022, 6, 15)
prices = download_pmc_on_date(d)

print(*prices, sep='\n')
```

# Resultado
```
# Prices are ordered descending 
{'value': 52.7, 'local_timestamp': '2022-01-01 00:00:00', 'utc_timestamp': '2021-12-31 23:00:00', 'zone': 'es'}
{'value': 56.25, 'local_timestamp': '2022-01-02 00:00:00', 'utc_timestamp': '2022-01-01 23:00:00', 'zone': 'es'}
{'value': 79.0, 'local_timestamp': '2022-01-03 00:00:00', 'utc_timestamp': '2022-01-02 23:00:00', 'zone': 'es'}
{'value': 81.72, 'local_timestamp': '2022-01-04 00:00:00', 'utc_timestamp': '2022-01-03 23:00:00', 'zone': 'es'}
{'value': 91.54, 'local_timestamp': '2022-01-05 00:00:00', 'utc_timestamp': '2022-01-04 23:00:00', 'zone': 'es'}
{'value': 95.8, 'local_timestamp': '2022-01-06 00:00:00', 'utc_timestamp': '2022-01-05 23:00:00', 'zone': 'es'}
{'value': 94.67, 'local_timestamp': '2022-01-07 00:00:00', 'utc_timestamp': '2022-01-06 23:00:00', 'zone': 'es'}
{'value': 89.06, 'local_timestamp': '2022-01-08 00:00:00', 'utc_timestamp': '2022-01-07 23:00:00', 'zone': 'es'}
{'value': 88.17, 'local_timestamp': '2022-01-09 00:00:00', 'utc_timestamp': '2022-01-08 23:00:00', 'zone': 'es'}
{'value': 89.43, 'local_timestamp': '2022-01-10 00:00:00', 'utc_timestamp': '2022-01-09 23:00:00', 'zone': 'es'}
{'value': 87.09, 'local_timestamp': '2022-01-11 00:00:00', 'utc_timestamp': '2022-01-10 23:00:00', 'zone': 'es'}
{'value': 82.43, 'local_timestamp': '2022-01-12 00:00:00', 'utc_timestamp': '2022-01-11 23:00:00', 'zone': 'es'}
{'value': 79.02, 'local_timestamp': '2022-01-13 00:00:00', 'utc_timestamp': '2022-01-12 23:00:00', 'zone': 'es'}
{'value': 92.5, 'local_timestamp': '2022-01-14 00:00:00', 'utc_timestamp': '2022-01-13 23:00:00', 'zone': 'es'}
{'value': 91.33, 'local_timestamp': '2022-01-15 00:00:00', 'utc_timestamp': '2022-01-14 23:00:00', 'zone': 'es'}
{'value': 93.55, 'local_timestamp': '2022-01-16 00:00:00', 'utc_timestamp': '2022-01-15 23:00:00', 'zone': 'es'}
{'value': 88.72, 'local_timestamp': '2022-01-17 00:00:00', 'utc_timestamp': '2022-01-16 23:00:00', 'zone': 'es'}
{'value': 82.57, 'local_timestamp': '2022-01-18 00:00:00', 'utc_timestamp': '2022-01-17 23:00:00', 'zone': 'es'}
{'value': 78.53, 'local_timestamp': '2022-01-19 00:00:00', 'utc_timestamp': '2022-01-18 23:00:00', 'zone': 'es'}
{'value': 74.89, 'local_timestamp': '2022-01-20 00:00:00', 'utc_timestamp': '2022-01-19 23:00:00', 'zone': 'es'}
{'value': 76.11, 'local_timestamp': '2022-01-21 00:00:00', 'utc_timestamp': '2022-01-20 23:00:00', 'zone': 'es'}
{'value': 82.38, 'local_timestamp': '2022-01-22 00:00:00', 'utc_timestamp': '2022-01-21 23:00:00', 'zone': 'es'}
{'value': 85.75, 'local_timestamp': '2022-01-23 00:00:00', 'utc_timestamp': '2022-01-22 23:00:00', 'zone': 'es'}
{'value': 89.19, 'local_timestamp': '2022-01-24 00:00:00', 'utc_timestamp': '2022-01-23 23:00:00', 'zone': 'es'}
{'value': 91.24, 'local_timestamp': '2022-01-25 00:00:00', 'utc_timestamp': '2022-01-24 23:00:00', 'zone': 'es'}
{'value': 93.3, 'local_timestamp': '2022-01-26 00:00:00', 'utc_timestamp': '2022-01-25 23:00:00', 'zone': 'es'}
{'value': 93.03, 'local_timestamp': '2022-01-27 00:00:00', 'utc_timestamp': '2022-01-26 23:00:00', 'zone': 'es'}
{'value': 93.53, 'local_timestamp': '2022-01-28 00:00:00', 'utc_timestamp': '2022-01-27 23:00:00', 'zone': 'es'}
{'value': 94.99, 'local_timestamp': '2022-01-29 00:00:00', 'utc_timestamp': '2022-01-28 23:00:00', 'zone': 'es'}
{'value': 96.47, 'local_timestamp': '2022-01-30 00:00:00', 'utc_timestamp': '2022-01-29 23:00:00', 'zone': 'es'}
{'value': 89.38, 'local_timestamp': '2022-01-31 00:00:00', 'utc_timestamp': '2022-01-30 23:00:00', 'zone': 'es'}
{'value': 81.67, 'local_timestamp': '2022-02-01 00:00:00', 'utc_timestamp': '2022-01-31 23:00:00', 'zone': 'es'}
...
# Note: File continues till last publish price for specified year
```