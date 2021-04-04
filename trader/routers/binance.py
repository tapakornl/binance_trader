from fastapi import APIRouter,Depends,status, HTTPException
from sqlalchemy.orm import Session
import schemas, database, models, oauth2
from repository import binance
import socket
import time
from typing import Optional
import threading

this = False
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 1234

def bot_trading():
    while True:
        if this:
            print(1)
            print(this)
            time.sleep(1)
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