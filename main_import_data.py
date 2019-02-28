# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import os
import numpy as np
import pandas as pd
#libreria de importación de datos
import quandl
import csv
import pickle
#librerias de gráficos
import plotly.offline as py
import plotly.graph_objs as go
import plotly.figure_factory as ff


"""
importación de datos de quandl
"""
file_directory="D:/Users/Usuario/Documents/Maestría/python_scripts/"
def get_quandl_data(quandl_id):
    cache_path = '{}.pkl'.format(quandl_id).replace('/','-')
    try:
        f = open(cache_path, 'rb')
        df = pickle.load(f)   
        print('Loaded {} from cache'.format(quandl_id))
    except (OSError, IOError) as e:
        print('Downloading {} from Quandl'.format(quandl_id))
        df = quandl.get(quandl_id, returns="pandas")
        df.to_pickle(cache_path)
        print('Cached {} at {}'.format(quandl_id, cache_path))
    return df

#Extracción de datos de Quandl
data_import=get_quandl_data("BCHARTS/KRAKENUSD")
data_currency_data_frame=pd.DataFrame(data_import)
data_currency_data_frame.to_csv(file_directory+"outfile.csv")


exchanges = ['COINBASE','BITSTAMP','ITBIT']

exchange_data = {}

exchange_data['KRAKEN'] ="BCHARTS/KRAKENUSD"
for exchange in exchanges:
    exchange_code = 'BCHARTS/{}USD'.format(exchange)
    btc_exchange_df = get_quandl_data(exchange_code)
    exchange_data[exchange] = btc_exchange_df
    
    
def merge_dfs_on_column(dataframes, labels, col):
    '''Merge a single column of each dataframe into a new combined dataframe'''
    series_dict = {}
    for index in range(len(dataframes)):
        series_dict[labels[index]] = dataframes[index][col]
        
    return pd.DataFrame(series_dict)



btc_usd_datasets = merge_dfs_on_column(list(exchange_data.values()), list(exchange_data.keys()), 'Weighted Price')

btc_usd_datasets.tail()