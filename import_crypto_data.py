
import ccxt
from datetime import datetime, timedelta, timezone
import math
import argparse
import pandas as pd

class import_crypto_data():
    """docstring for ClassName"""
    def __init__(self, arg):
        print("llegue")
        exchange=""
        
    def import_data(coin_import,exchange_where, time_frame_import):
        
    # Get our Exchange
            try:
                #definición de argmumentos
                args = parse_args(ccxt,Namespace(debug=False, exchange=exchange_where, symbol=coin_import, timeframe=time_frame_import))
                exchange = getattr (ccxt, args.exchange) ()
            except AttributeError:
                print('-'*36,' ERROR ','-'*35)
                print('Exchange "{}" not found. Please check the exchange is supported.'.format(args.exchange))
                print('-'*80)
                quit()

            # Check if fetching of OHLC Data is supported
            if exchange.has["fetchOHLCV"] == False:
                print('-'*36,' ERROR ','-'*35)
                print('{} does not support fetching OHLC data. Please use another exchange'.format(args.exchange))
                print('-'*80)
                quit()

            #Compara si existe las información de los tickers
            if exchange.has["fetchTickers"] == False:
                print('-'*36,' ERROR ','-'*35)
                print('{} does not support fetching fetchTickers data. Please use another exchange'.format(args.exchange))
                print('-'*80)
                quit()

            # Check requested timeframe is available. If not return a helpful error.
            if args.timeframe not in exchange.timeframes:
                print('-'*36,' ERROR ','-'*35)
                print('The requested timeframe ({}) is not available from {}\n'.format(args.timeframe,args.exchange))
                print('Available timeframes are:')
                for key in exchange.timeframes.keys():
                    print('  - ' + key)
                print('-'*80)
                quit()

            # Check if the symbol is available on the Exchange
                exchange.load_markets()
            if args.symbol not in exchange.symbols:
                print('-'*36,' ERROR ','-'*35)
                print('The requested symbol ({}) is not available from {}\n'.format(args.symbol,args.exchange))
                print('Available symbols are:')
                for key in exchange.symbols:
                    print('  - ' + key)
                print('-'*80)
                quit()

            return ""

    def return_data():
        self.import_data()
        data_construct=pd.DataFrame(exchange.fetch_ticker(args.symbol))
        return data_construct
