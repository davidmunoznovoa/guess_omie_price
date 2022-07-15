# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    requirements = f.readlines()

setup(
    name='guess_omie_price',
    version='1.0.0',
    description="Herramienta para tratar de predecir el precio de mercado de OMIE a futuros.",
    author="Helios",
    provides=['guess_omie_price'],
    packages=find_packages(),
    install_requires=requirements,
    license='GNU General Public License v3.0',
    author_email='heliosthemaster@gmail.com',
    url='https://github.com/davidmunoznovoa/guess_omie_price',
)
