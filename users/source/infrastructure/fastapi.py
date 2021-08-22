from fastapi import FastAPI

from source.infrastructure.databases import postgres_database
#from source.adapters.controllers import router as users_router


app = FastAPI()

#app.include_router(users_router, prefix='/users', tags=['users'])

@app.on_event('startup')
async def startup():
    await postgres_database.connect()

@app.on_event('shutdown')
async def shutdown():
    await postgres_database.disconnect()
