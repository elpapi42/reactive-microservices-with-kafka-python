from fastapi import FastAPI

from source.infrastructure.databases import postgres_database
from source.adapters.controllers import router


app = FastAPI()

app.include_router(router)

@app.on_event('startup')
async def startup():
    await postgres_database.connect()

@app.on_event('shutdown')
async def shutdown():
    await postgres_database.disconnect()
