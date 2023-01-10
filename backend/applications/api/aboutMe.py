from flask import Blueprint
from flask import request
from utils.http import success_api, fail_api
from applications.database import connect_database

from utils.create_user import user
aboutMe_opt = Blueprint('aboutMe_opt', __name__, url_prefix='/api/aboutMe')


@aboutMe_opt.route('/info',methods=['GET'])
def get_info():
    db = connect_database(username=user.username,password=user.password)
    result = db.execute(f'''
                        SELECT * FROM 
                        fan_own
                        ''').fetchone()
    my_dic = {"fanId":result[0],"fanName":result[1],"fanSex":result[2],
                                     "fanAge":result[3],"fanCareer":result[4]}
    aboutMedata = [my_dic]
    return success_api('查询成功',data={"aboutMeData":aboutMedata})

@aboutMe_opt.route('/editMyInfo',methods=['PUT'])
def edit_info():
    fan_id = request.get_json().get('fanId')
    fname = request.get_json().get('fanName')
    sex = request.get_json().get('fanSex')
    career = request.get_json().get('fanCareer')
    age = request.get_json().get('fanAge')
    db = connect_database(username=user.username,password=user.password)
    db.execute(f'''UPDATE fan_own
                SET fname='{fname}',sex='{sex}',occupation='{career}',age='{age}'
                WHERE fan_id='{fan_id}'
                ''')
    return success_api('修改成功')

@aboutMe_opt.route('/addMyLike',methods=['POST'])
def add_mylike():
    db = connect_database()
    table = request.get_json().get('table')
    mainkey = request.get_json().get('mainKey')
    if table == 'bands':
        db.execute(f'''
                    INSERT INTO fan_band(fan_id,bname)
                    VALUES('{user.username}','{mainkey}')
                    ''')
        return success_api('添加成功')
    elif table == 'albums':
        db.execute(f'''
                    INSERT INTO fan_album(fan_id,aname)
                    VALUES('{user.username}','{mainkey}')
                    ''')
        return success_api('添加成功')
    else:
        bname = request.get_json().get('plusKey')
        db.execute(f'''
                    INSERT INTO fan_song(fan_id,sname,bname)
                    VALUES('{user.username}','{mainkey}','{bname}')
                    ''')
        return success_api('添加成功')

@aboutMe_opt.route('/disLike',methods=['DELETE'])
def dis_mylike():
    db = connect_database()
    table = request.get_json().get('table')
    mainkey = request.get_json().get('mainKey')
    if table == 'bands':
        db.execute(f'''
                    DELETE
                    FROM fan_band
                    WHERE fan_id='{user.username}' AND bname='{mainkey}'
                    ''')
        return success_api('删除成功')
    elif table == 'albums':
        db.execute(f'''
                    DELETE
                    FROM fan_album
                    WHERE fan_id='{user.username}' AND aname='{mainkey}'
                    ''')
        return success_api('删除成功')
    else:
        bname = request.get_json().get('plusKey')
        db.execute(f'''
                    DELETE
                    FROM fan_song
                    WHERE fan_id='{user.username}' AND sname='{mainkey}' AND bname='{bname}'
                    ''')
        return success_api('删除成功')

@aboutMe_opt.route('/addMyAttending',methods=['POST'])
def add_myconcert():
    time = request.get_json().get('plusKey')
    bname = request.get_json().get('mainKey')
    try:
        db = connect_database()
        db.execute(f'''
                    INSERT INTO fan_concert(fan_id,bname,begin_time)
                    VALUES('{user.username}','{bname}','{time}')
                    ''')
        return success_api('添加成功')
    except Exception as e:
        print(e)
        return fail_api('该场演唱会不存在')

@aboutMe_opt.route('/disMyAttending',methods=['DELETE'])
def delete_myconcert():
    time = request.get_json().get('plusKey')
    bname = str(request.get_json().get('mainKey'))
    db = connect_database()
    db.execute(f'''
                DELETE FROM fan_concert
                WHERE fan_id='{user.username}' AND 
                begin_time='{time}'
                ''')
    return success_api('删除')

@aboutMe_opt.route('/getMyLike',methods=['GET'])
def get_mylike():
    query = request.args.get('likeThing')
    db = connect_database(username=user.username,password=user.password)
    if query == 'band':
        likeband_data = []
        my_like_bands = db.execute(f'''
                                    SELECT * FROM fan_band_own
                                    ''').fetchall()
        for i in my_like_bands:
            mydic = {}
            mydic["bandName"] = i.bname
            mydic["bandLeader"] = i.leader
            mydic["fundationTime"] = str(i.establish_time)
            mydic["bandNumber"] = i.num
            mydic["isLike"] = True
            mydic["isEdit"] = False
            album_num = db.execute(f'''
                                   SELECT COUNT(*)
                                   FROM albums
                                   WHERE bname = "{i.bname}"
                                    ''').fetchone()[0]
            mydic["albumNumber"] = album_num
            likeband_data.append(mydic)
        return success_api('查询成功',data={"likeBandData":likeband_data})

    if query == 'album':
        likealbum_data = []
        my_like_albums = db.execute(f'''
                                    SELECT * FROM fan_album_own
                                    ''').fetchall()
        for i in my_like_albums:
            mydic = {}
            mydic["albumName"] = i.aname
            mydic["performBand"] = i.bname
            mydic["releaseTime"] = str(i.release_time)
            mydic["releaseCompany"] = i.release_company
            mydic["isLike"] = True
            mydic["isEdit"] = False
            likealbum_data.append(mydic)

        return success_api('查询成功',data={"likeAlbumData":likealbum_data})

    if query == 'song':
        likesong_data = []
        my_like_songs = db.execute(f'''
                                    SELECT * FROM fan_song_own
                                    ''').fetchall()
        for i in my_like_songs:
            mydic = {}
            mydic["albumBelong"] = i.aname
            mydic["creator"] = i.bname
            mydic["songName"] = i.sname
            mydic["isLike"] = True
            mydic["isEdit"] = False
            likesong_data.append(mydic)

        return success_api('查询成功', data={"likeMusicData": likesong_data})

    return fail_api('请检查请求参数是否正确')

@aboutMe_opt.route('/getMyAttending',methods=['GET'])
def get_my_attending():
    my_attending_list = []
    db = connect_database(username=user.username,password=user.password)
    my_attedings = db.execute(f'''
                                SELECT * FROM fan_concert_own
                                ''').fetchall()
    for i in my_attedings:
        mydic = {}
        mydic["bandName"] = i.bname
        mydic["duration"] = i.duration
        mydic["holdingTime"] = str(i.begin_time)
        mydic["holdingPlace"] = db.execute(f'''
                                            SELECT hold_location 
                                            FROM concerts
                                            WHERE bname='{i.bname}' AND begin_time='{i.begin_time}'
                                            ''').fetchone()[0]
        mydic["isLike"] = True
        mydic["isEdit"] = False
        my_attending_list.append(mydic)

    return success_api('查询成功', data={"concertData": my_attending_list})