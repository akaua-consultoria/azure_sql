#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 20:07:24 2023

@author: nfamartins
"""

from setuptools import setup, find_packages

setup(
    name="azure_sql",
    version="0.1",
    description="Um pacote para facilitar o create, insert, delete e drop table no Azure SQL",
    author="Nathália Martins",
    author_email="nathalia@akaua.com.br",
    packages=find_packages(),
		install_requires=[
        'pyodbc'
    ],
)
