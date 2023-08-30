#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 11:34:24 2023

@author: nfamartins
"""

# pacotes
import pyodbc

def insert_table(df, server, database, username, password, table_name,
                 driver = '{ODBC Driver 18 for SQL Server}', Encrypt = 'yes', TrustServerCertificate ='no',
                 ConnectionTimeout = '30',others=''):
    
    # criando a string de conexão
    conn_str = f"Driver={driver};Server={server};Database={database};Uid={username};Pwd={password};Encrypt={Encrypt};TrustServerCertificate={TrustServerCertificate};Connection Timeout={ConnectionTimeout};{others}"
    
    # convertendo o dataframe do pandas para uma lista de tuplas
    data_tuples = [tuple(row) for row in df.values]
    
    # criando strings com os nomes das colunas
    col_names = ', '.join(df.columns.tolist()) 
    
    # criando string de interrogações
    values = ','.join(['?']*len(df.columns.tolist())) 
    
    # criando a query para inserir dados em uma tabela
    insert_query = f"INSERT INTO {table_name} ({col_names}) VALUES ({values})" 
    
    # estabelecendo conexão com o banco de dados
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    # executando a inserção dos dados na tabela
    try:
        # primeiro tentando com fast_executemany
        cursor.fast_executemany = True   
        cursor.executemany(insert_query, data_tuples)
        print(f"A tabela '{table_name}' foi inserida com sucesso do banco de dados, usando fast execute many.")
    except:
        # se não for possível, faremos mais lento
        cursor.fast_executemany = False   
        cursor.executemany(insert_query, data_tuples)
        print(f"A tabela '{table_name}' foi inserida com sucesso do banco de dados, não usando fast execute many.")
    finally:
        # confirmando as alterações no banco de dados
        conn.commit()
        
        # fechando a conexão
        cursor.close()
        conn.close()