import time
import os
import json
import csv
from binance.client import Client
from binance import BinanceSocketManager
#from binance.streams import BinanceSocketManager
from twisted.internet import reactor


binance_api ="APIKEY"
binance_secret ="APISEC" #""
os.environ[binance_api] = "APIKEY"
os.environ[binance_secret] = "APISEC"
api_key = os.environ.get(binance_api)
api_secret = os.environ.get(binance_secret)
client = Client(api_key,api_secret,testnet = False)


timestamp = client._get_earliest_valid_timestamp('ETHUSDT', '1m')

client.get_account()
#ETHquantity  = float(client.get_asset_balance(asset = "LINK",timestamp=timestamp))
#LINKquantity = float(client.get_asset_balance(asset = "ETH",timestamp=timestamp))
print(ETHquantity,"\n",LINKquantity)
LINKETHprice = float(client.get_symbol_ticker(symbol="LINKETH")['price']) #returns >>{'symbol': 'BTCUSDT', 'price': '9678.08000000'}
LINKPrice = float(client.get_symbol_ticker(symbol = "LINKUSDT")['price'])
ETHPrice = float(client.get_symbol_ticker(symbol = "ETHUSDT")['price'])
print(LINKPrice)
print(ETHPrice)
print(LINKETHprice)
#proportionETH = 0.0185 * 2700 
#proportionLink = 0.0185/0.01 * 27 #= 1.85*27

#ETHcost = ETHquantity*ETHPrice
#LINKcost = LINKquantity *LINKPrice
ETHcost = 50  #just test, need to change when we get the asset balance from ETHquantity and LINKquantity
LINKcost =50  #just test

buy_order = client.create_order
sell_order = client.create_order

#selling ETH = buying more LINK/ETH = buyValue 
#buying ETH = selling more LINK/ETH = buyValue 
if  ETHcost> 1.1*LINKcost :
    ref = (ETHcost +LINKcost)/2
    buyValue = (ETHcost - ref)
    quantity = buyValue/LinkPrice
    buy_order(symbol = "LINKETH",
                    side='BUY',
                    type='MARKET',
                    timeInForce='GTC',
                    quantity = round(quantity,2))
elif  ETHcost < 0.9*LINKcost :
    ref = (ETHcost +LINKcost)/2
    sellValue = (LINKcost - ref)
    quantity = sellValue/LinkPrice
    sell_order(symbol = "LINKETH",
                    side='SELL',
                    type='MARKET',
                    timeInForce='GTC',
                    quantity = round(quantity,2))
else :
    print("still 50/50")
