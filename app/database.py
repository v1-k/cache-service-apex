import oracledb
from .config import settings

class Database:
    def __init__(self):
        self.pool = oracledb.create_pool(
            user=settings.db_user, 
            password=settings.db_password, 
            dsn=settings.db_host, 
            min=settings.db_minpool, 
            max=settings.db_maxpool)
    
    def get(self):
        return self.pool
    
db = Database()