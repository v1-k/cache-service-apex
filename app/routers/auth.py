from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
import oracledb
from .. import  schemas,  util, oauth2, database

router = APIRouter(tags=['Authentication'])

@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends()):
    user = {}
    pool = database.db.get()
    sql = "select id, username, password from cache_users where username = :username"
    try:
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, [user_credentials.username])
                
                row = cursor.fetchone()
                if row:
                    user['id'] = row[0]
                    user['username'] = row[1]
                    user['password'] = row[2]
                    
    except oracledb.DatabaseError as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials{e.args[0]}")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials{e}")
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not util.verify(user_credentials.password, user['password']):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    access_token = oauth2.create_access_token(data={"user_id": user['id']})

    return {"access_token": access_token, "token_type": "bearer"}