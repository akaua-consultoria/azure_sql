#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 12:46:08 2023

@author: nfamartins
"""

# pacotes
import pyodbc

def drop_table(server, database, username, password, table_name,
                 driver = '{ODBC Driver 18 for SQL Server}', Encrypt = 'yes', TrustServerCertificate ='no',
                 ConnectionTimeout = '30',others=''):
    
    # criando a string de conexão
    conn_str = f"Driver={driver};Server={server};Database={database};Uid={username};Pwd={password};Encrypt={Encrypt};TrustServerCertificate={TrustServerCertificate};Connection Timeout={ConnectionTimeout};{others}"
    
    # Estabelecendo conexão com o banco de dados
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    # query para excluir a tabela
    drop_table_query = f"DROP TABLE {table_name}"
    
    # executnado a consulta para excluir a tabela
    cursor.execute(drop_table_query)
    conn.commit()
    
    # frachando a conexão
    cursor.close()
    conn.close()
    
    print(f"A tabela '{table_name}' foi excluída com sucesso do banco de dados.")




