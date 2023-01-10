from applications.database import connect_database

def create_user():
    '''
    创建测试用的数据库用户
    :return:None
    '''
    db = connect_database()
    #创建fan用户并授权
    db.execute("CREATE USER IF NOT EXISTS 'fan1'@'localhost' IDENTIFIED BY'123456'")
    db.execute("GRANT SELECT ON final.* TO 'fan1'@'localhost'")
    db.execute("GRANT UPDATE ON fan_own TO 'fan1'@'localhost'")
    #创建band用户并授权
    db.execute("CREATE USER IF NOT EXISTS 'band1'@'localhost' IDENTIFIED BY'123456'")
    db.execute("GRANT SELECT ON final.* TO 'band1'@'localhost'")
    db.execute(f"GRANT ALL PRIVILEGES ON band_own TO 'band1'@'localhost'")
    db.execute(f"GRANT ALL PRIVILEGES ON band_album TO 'band1'@'localhost'")
    db.execute(f"GRANT ALL PRIVILEGES ON band_concert TO 'band1'@'localhost'")
    db.execute(f"GRANT ALL PRIVILEGES ON band_song TO 'band1'@'localhost'")
    #创建admin用户并授权
    db.execute("CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY'123456'")
    db.execute("GRANT ALL PRIVILEGES ON final.* TO 'admin'@'localhost'")
    return None