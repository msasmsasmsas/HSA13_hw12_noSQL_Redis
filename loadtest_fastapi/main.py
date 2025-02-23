from fastapi import FastAPI
import redis.asyncio as redis
import uvicorn
from pydantic import BaseModel

app = FastAPI()
redis_master = redis.Redis(host='redis-master', port=6379, decode_responses=True)
redis_slave = redis.Redis(host='redis-slave', port=6379, decode_responses=True)

class KeyValue(BaseModel):
    key: str
    value: str

@app.post("/set/")
async def set_value(data: KeyValue):
    await redis_master.set(data.key, data.value)
    return {"message": "Value set successfully"}

@app.get("/get/{key}")
async def get_value(key: str):
    value = await redis_slave.get(key)
    return {"key": key, "value": value}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
