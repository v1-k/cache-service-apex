from fastapi import FastAPI, status, HTTPException, Body
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from .cache import lookup

class SetCache(BaseModel):
    key: str
    values: dict

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Cache Service Home"}

@app.get("/cache/{key}")
def get_cache(key):
    response = lookup.lookup.get(key)
    
    if not response :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Key {key} not found ")
    return response

@app.post("/cache",status_code=status.HTTP_201_CREATED)
#def post_cache(payload: dict = Body(...)):
def set_cache(body: SetCache):
    key = body.key
    response = lookup.lookup.set(key,body.values)
    
    if not response :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Key {key} not found ")
    return response