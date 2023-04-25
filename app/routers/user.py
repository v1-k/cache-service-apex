from fastapi import status, APIRouter
import oracledb
from .. import util, database, schemas

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate ):
    hashed_password = util.hash(user.password)
    user.password = hashed_password
    
    pool = database.db.get()
    sql = "insert into cache_users (username,password) values(:1,:2)"
    try:
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, [user.email,user.password])
                connection.commit()
                return "Created"
    except oracledb.DatabaseError as e:
        print(f"Error {e.args[0]} occurred.")
        return f"Error {e.args[0]} occurred."
    except Exception as e:
        print("An error occurred:", e)
        return f"An error occurred: {e}"