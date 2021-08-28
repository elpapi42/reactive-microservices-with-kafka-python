from fastapi import FastAPI

#from source.infrastructure.kafka import subscriber
#from source.adapters.controllers import router


app = FastAPI()

#app.include_router(router)

@app.on_event('startup')
async def startup():
    #await subscriber.start()
    #subscriber.subscribe()
    pass

@app.on_event('shutdown')
async def shutdown():
    #await subscriber.stop()
    pass
