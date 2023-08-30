#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 12:53:58 2023

@author: nfamartins
"""

# pacotes
import pyodbc

def create_table(server, database, username, password, table_name, column_definitions,
                 driver = '{ODBC Driver 18 for SQL Server}', Encrypt = 'yes', TrustServerCertificate ='no',
                 ConnectionTimeout = '30',others=''):
    
    
    # criando a string de conexão
    conn_str = f"Driver={driver};Server={server};Database={database};Uid={username};Pwd={password};Encrypt={Encrypt};TrustServerCertificate={TrustServerCertificate};Connection Timeout={ConnectionTimeout};{others}"
    
    # estabelecendo conexão com o banco de dados
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    # query para criar a tabela
    create_table_query = f"CREATE TABLE {table_name} ({column_definitions})"
    
    # Executar a consulta para criar a tabela
    cursor.execute(create_table_query)
    conn.commit()
    
    # Fechar a conexão
    cursor.close()
    conn.close()
    
    print(f"A tabela '{table_name}' foi criada com sucesso no banco de dados.")