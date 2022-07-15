# guess_omie_price

:snake: :zap: :moneybag:

![](https://github.com/davidmunoznovoa/guess_omie_price/actions/workflows/python3-app.yml/badge.svg)
![](https://github.com/davidmunoznovoa/guess_omie_price/actions/workflows/python3-app.yml)

- Herramienta para tratar de predecir el precio de mercado de OMIE a futuros.
- También permite descargar distintos ficheros a tener en cuenta para las predicciones.

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
{'local_timestamp': '2022-04-13 01:00:00', 'utc_timestamp': '2022-04-12 23:00:00', 'value': 242.75}
{'local_timestamp': '2022-04-13 02:00:00', 'utc_timestamp': '2022-04-13 00:00:00', 'value': 229.77}
{'local_timestamp': '2022-04-13 03:00:00', 'utc_timestamp': '2022-04-13 01:00:00', 'value': 220.0}
{'local_timestamp': '2022-04-13 04:00:00', 'utc_timestamp': '2022-04-13 02:00:00', 'value': 201.85}
{'local_timestamp': '2022-04-13 05:00:00', 'utc_timestamp': '2022-04-13 03:00:00', 'value': 190.9}
{'local_timestamp': '2022-04-13 06:00:00', 'utc_timestamp': '2022-04-13 04:00:00', 'value': 212.32}
{'local_timestamp': '2022-04-13 07:00:00', 'utc_timestamp': '2022-04-13 05:00:00', 'value': 248.74}
{'local_timestamp': '2022-04-13 08:00:00', 'utc_timestamp': '2022-04-13 06:00:00', 'value': 257.02}
{'local_timestamp': '2022-04-13 09:00:00', 'utc_timestamp': '2022-04-13 07:00:00', 'value': 260.0}
{'local_timestamp': '2022-04-13 10:00:00', 'utc_timestamp': '2022-04-13 08:00:00', 'value': 254.25}
{'local_timestamp': '2022-04-13 11:00:00', 'utc_timestamp': '2022-04-13 09:00:00', 'value': 242.75}
{'local_timestamp': '2022-04-13 12:00:00', 'utc_timestamp': '2022-04-13 10:00:00', 'value': 234.99}
{'local_timestamp': '2022-04-13 13:00:00', 'utc_timestamp': '2022-04-13 11:00:00', 'value': 227.67}
{'local_timestamp': '2022-04-13 14:00:00', 'utc_timestamp': '2022-04-13 12:00:00', 'value': 208.0}
{'local_timestamp': '2022-04-13 15:00:00', 'utc_timestamp': '2022-04-13 13:00:00', 'value': 201.18}
{'local_timestamp': '2022-04-13 16:00:00', 'utc_timestamp': '2022-04-13 14:00:00', 'value': 196.0}
{'local_timestamp': '2022-04-13 17:00:00', 'utc_timestamp': '2022-04-13 15:00:00', 'value': 200.47}
{'local_timestamp': '2022-04-13 18:00:00', 'utc_timestamp': '2022-04-13 16:00:00', 'value': 221.2}
{'local_timestamp': '2022-04-13 19:00:00', 'utc_timestamp': '2022-04-13 17:00:00', 'value': 219.28}
{'local_timestamp': '2022-04-13 20:00:00', 'utc_timestamp': '2022-04-13 18:00:00', 'value': 242.36}
{'local_timestamp': '2022-04-13 21:00:00', 'utc_timestamp': '2022-04-13 19:00:00', 'value': 254.0}
{'local_timestamp': '2022-04-13 22:00:00', 'utc_timestamp': '2022-04-13 20:00:00', 'value': 259.0}
{'local_timestamp': '2022-04-13 23:00:00', 'utc_timestamp': '2022-04-13 21:00:00', 'value': 250.0}
{'local_timestamp': '2022-04-14 00:00:00', 'utc_timestamp': '2022-04-13 22:00:00', 'value': 231.94}
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
{'local_timestamp': '2022-06-15 01:00:00', 'utc_timestamp': '2022-06-14 23:00:00', 'value': 65.22}
{'local_timestamp': '2022-06-15 02:00:00', 'utc_timestamp': '2022-06-15 00:00:00', 'value': 71.27}
{'local_timestamp': '2022-06-15 03:00:00', 'utc_timestamp': '2022-06-15 01:00:00', 'value': 75.24}
{'local_timestamp': '2022-06-15 04:00:00', 'utc_timestamp': '2022-06-15 02:00:00', 'value': 79.33}
{'local_timestamp': '2022-06-15 05:00:00', 'utc_timestamp': '2022-06-15 03:00:00', 'value': 79.33}
{'local_timestamp': '2022-06-15 06:00:00', 'utc_timestamp': '2022-06-15 04:00:00', 'value': 80.71}
{'local_timestamp': '2022-06-15 07:00:00', 'utc_timestamp': '2022-06-15 05:00:00', 'value': 79.0}
{'local_timestamp': '2022-06-15 08:00:00', 'utc_timestamp': '2022-06-15 06:00:00', 'value': 70.84}
{'local_timestamp': '2022-06-15 09:00:00', 'utc_timestamp': '2022-06-15 07:00:00', 'value': 61.46}
{'local_timestamp': '2022-06-15 10:00:00', 'utc_timestamp': '2022-06-15 08:00:00', 'value': 56.1}
{'local_timestamp': '2022-06-15 11:00:00', 'utc_timestamp': '2022-06-15 09:00:00', 'value': 52.13}
{'local_timestamp': '2022-06-15 12:00:00', 'utc_timestamp': '2022-06-15 10:00:00', 'value': 48.45}
{'local_timestamp': '2022-06-15 13:00:00', 'utc_timestamp': '2022-06-15 11:00:00', 'value': 46.2}
{'local_timestamp': '2022-06-15 14:00:00', 'utc_timestamp': '2022-06-15 12:00:00', 'value': 45.5}
{'local_timestamp': '2022-06-15 15:00:00', 'utc_timestamp': '2022-06-15 13:00:00', 'value': 44.08}
{'local_timestamp': '2022-06-15 16:00:00', 'utc_timestamp': '2022-06-15 14:00:00', 'value': 44.82}
{'local_timestamp': '2022-06-15 17:00:00', 'utc_timestamp': '2022-06-15 15:00:00', 'value': 46.32}
{'local_timestamp': '2022-06-15 18:00:00', 'utc_timestamp': '2022-06-15 16:00:00', 'value': 48.12}
{'local_timestamp': '2022-06-15 19:00:00', 'utc_timestamp': '2022-06-15 17:00:00', 'value': 50.7}
{'local_timestamp': '2022-06-15 20:00:00', 'utc_timestamp': '2022-06-15 18:00:00', 'value': 53.55}
{'local_timestamp': '2022-06-15 21:00:00', 'utc_timestamp': '2022-06-15 19:00:00', 'value': 55.4}
{'local_timestamp': '2022-06-15 22:00:00', 'utc_timestamp': '2022-06-15 20:00:00', 'value': 56.44}
{'local_timestamp': '2022-06-15 23:00:00', 'utc_timestamp': '2022-06-15 21:00:00', 'value': 57.79}
{'local_timestamp': '2022-06-16 00:00:00', 'utc_timestamp': '2022-06-15 22:00:00', 'value': 64.2}
```