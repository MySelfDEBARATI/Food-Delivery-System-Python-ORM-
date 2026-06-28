from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

user = 'root'
password = ''
host = '127.0.0.1'
port = '3366'
database = 'food_db'

database_url = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'


engine = create_engine(database_url, pool_recycle = 3366, pool_pre_ping = True)

session_local = sessionmaker(autocommit = False, autoflush = False, bind = engine)


# try:
#     with engine.connect() as connection:
#         result = connection.execute(text("SELECT 'successfully connected'"))
#         for row in result:
#             print(row[0])

# except Exception as e:
#     print(f"An error occured in database connection {e}")