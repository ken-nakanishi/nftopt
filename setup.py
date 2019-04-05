# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='nftopt',
    version='0.0.1',
    description='Nakanishi-Fujii-Todo method for scipy.optimize',
    long_description=readme,
    author='Ken Nakanishi',
    author_email='ikyhn1.ken.n@gmail.com',
    install_requires=['numpy', 'scipy'],
    url='https://github.com/ken-nakanishi/nftopt',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)
