from fastapi import  FastAPI, status, HTTPException,  APIRouter, Depends
from pydantic import BaseModel

from ..cache import lookup
from .. import oauth2
class SetCache(BaseModel):
    key: str
    values: dict

router = APIRouter(
    prefix="/cache",
    tags=['Cache']
)

@router.get("/{key}")
def get_cache(key, current_user: int = Depends(oauth2.get_current_user)):
    response = lookup.lookup.get(key)
    print("current_user",current_user)
    if not response :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Key {key} not found ")
    return response

@router.post("",status_code=status.HTTP_201_CREATED)
#def post_cache(payload: dict = Body(...)):
def set_cache(body: SetCache, current_user: int = Depends(oauth2.get_current_user)):
    print("current_user",current_user)
    key = body.key
    response = lookup.lookup.set(key,body.values)
    
    if not response :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Key {key} not found ")
    return response