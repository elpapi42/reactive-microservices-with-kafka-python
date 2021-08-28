from fastapi import FastAPI

from source.infrastructure.kafka import producer
#from source.adapters.controllers import router


app = FastAPI()

#app.include_router(router)

@app.on_event('startup')
async def startup():
    pass

@app.on_event('shutdown')
async def shutdown():
    pass
