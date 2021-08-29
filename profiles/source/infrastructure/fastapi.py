from fastapi import FastAPI

from source.adapters.subscribers import create_profile_subscriber
from source.infrastructure.kafka.producers import producer
#from source.adapters.controllers import router


app = FastAPI()

#app.include_router(router)

@app.on_event('startup')
async def startup():
    await producer.start()
    await create_profile_subscriber.start()
    create_profile_subscriber.subscribe()

@app.on_event('shutdown')
async def shutdown():
    await create_profile_subscriber.stop()
    await producer.stop()
