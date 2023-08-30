#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 14:13:29 2023

@author: nfamartins
"""

# pacotes
import pyodbc

def delete_table(server, database, username, password, table_name,
                 driver = '{ODBC Driver 18 for SQL Server}', Encrypt = 'yes', TrustServerCertificate ='no',
                 ConnectionTimeout = '30',others=''):
    
    # criando a string de conexão
    conn_str = f"Driver={driver};Server={server};Database={database};Uid={username};Pwd={password};Encrypt={Encrypt};TrustServerCertificate={TrustServerCertificate};Connection Timeout={ConnectionTimeout};{others}"
    
    # Estabelece conexão com o banco de dados
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    # query para apagar os dados da tabela
    delete_data_query = f"DELETE FROM {table_name}"
    
    # Executa a consulta para apagar os dados da tabela
    cursor.execute(delete_data_query)
    conn.commit()
    
    # Fecha a conexão
    cursor.close()
    conn.close()
    
    print(f"Os dados da tabela '{table_name}' foram apagados com sucesso.")
