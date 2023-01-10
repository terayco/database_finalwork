from sqlalchemy import create_engine

from applications.database import passwrd


def connect_database(username='root',password=passwrd.password,hostname='127.0.0.1',port=3306,database='final'):
    database_URI  = f'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}?charset=utf8mb4'
    #设置echo为false则不打印执行的sql语句，不然太混乱了
    engine = create_engine(database_URI, echo=False)
    db = engine.connect()
    return db