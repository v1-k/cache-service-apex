from fastapi import Depends, APIRouter

from .. import oauth2

router = APIRouter(
    prefix="/protected",
    tags=['Protected']
)

@router.get("/")
def protected_route(depends=Depends(oauth2.verify_secret_key)):
    return {"message": "This route is protected"}
