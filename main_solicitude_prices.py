from import_crypto_data import import_data


# Get data
data=import_crypto_data.import_data("NEO/ETH",'Binance','1m')
print(data)
#data = exchange.fetch_ohlcv(args.symbol, args.timeframe)
#data_new=exchange.fetch_tickers(args.symbol)
#header = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
#header_2=['symbol','info','timestamp','datetime','high','low','bid','bidVolume','ask','askVolume','vwap','open','close','last','previousClose','change','percentage','average','baseVolume','quoteVolume']
#df = pd.DataFrame(data, columns=header).set_index('Timestamp')
#print(data_new)
#new_data_frame=pd.DataFrame(data_new, columns=header_2)
#print(new_data_frame)
# Save it
#symbol_out = args.symbol.replace("/","")
#filename = '{}-{}-{}.csv'.format(args.exchange, symbol_out,args.timeframe)
#df.to_csv(filename)