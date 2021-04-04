from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException,status
from hashing import Hash

def start():
    return True

def stop():
    return False