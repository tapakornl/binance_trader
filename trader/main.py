
from fastapi import FastAPI
import  models
from database import engine
from routers import user, authentication, binance

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(binance.router)