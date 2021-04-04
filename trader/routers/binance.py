from fastapi import APIRouter,Depends,status, HTTPException
from sqlalchemy.orm import Session
import schemas, database, models, oauth2
from repository import binance
import socket
import time
from typing import Optional
import threading
from binance.client import Client
from binance.enums import *

this = False
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 1234
POWER = True
API_KEY = "TO BE ADDED:"
API_SC = "TO BE ADDED"

def binance_login(API_KEY, API_SC):
    client = Client(API_KEY,
                    API_SC)

def buy(client):
    order = client.order_market_buy(
        symbol='BTCUSDT',
        quantity=0.001)

def pre_process_klines(klines, ticks_no= None):
    if ticks_no:
        return [klines[tick][4] for tick in range(ticks_no)]
    else:
        return [kline[4] for kline in klines ]

def EMA(preprocess_klines, ticks_no, count):
    if ticks_no == 0:
        return preprocess_klines[0]
    else:
        K = 2 / (count + 1)
        return (preprocess_klines[ticks_no-1] * K) + (EMA(preprocess_klines[ticks_no-1], ticks_no-1, count+1) * (1 - K))
def moving_avg(klines, ticks_no):
    data = pre_process_klines(klines)
    data = [klines[i][4] for i in range(0, ticks_no)]
    return sum(data)/ticks_no

def check_indicator(client):
    klines = client.get_historical_klines("BTCUSDT",
                                          Client.KLINE_INTERVAL_15MINUTE,
                                          "1 day ago UTC")

    return True

def bot_trading():

    lastTime = time.time()
    client = binance_login(API_KEY, API_SC)

    while True:
        if POWER == False:
            break

        if time.time() > lastTime+30 and this:
            if check_indicator()
            lastTime = time.time()

x = threading.Thread(target=bot_trading, args=())
x.start()


router = APIRouter(
    prefix="/trader",
    tags=['Trader']
)

get_db = database.get_db

#TODO: send socket packets to another python file to start running bot trade
@router.get('/start')
def start_trade():
    global this
    this = True
    return "OK"


#TODO send data via socket lib to stop bot trade
@router.get('/stop')
def stop_trade():
    global this
    this= False
    return "OK"

@router.get('/shutdown')
def shutdown_trade():
    global POWER
    POWER = False