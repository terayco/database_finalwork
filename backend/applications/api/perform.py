from flask import Blueprint
from flask import request
from utils.http import success_api, fail_api
from applications.database import connect_database
from utils.create_user import user

perform_opt = Blueprint('perform_opt', __name__, url_prefix='/api/perform')

@perform_opt.route('/addPerform',methods=['POST'])
def add_perform():
    bname = request.get_json().get('bandName')
    duration = request.get_json().get('duration')
    begin_time = str(request.get_json().get('holdingTime'))
    hold_lcation = request.get_json().get('holdingPlace')
    db = connect_database()
    try:
        db.execute(f'''
                    INSERT INTO concerts(bname,begin_time,duration,hold_location)
                    VALUES('{bname}','{begin_time}','{duration}','{hold_lcation}')
                    ''')
    except Exception as e:
        print(e)
        return fail_api('该唱演唱会已存在，请确保同一乐队同一时间只有一场演唱会!')
    return success_api('添加成功')

@perform_opt.route('/editPerform',methods=['PUT'])
def edit_perform():
    id = request.get_json().get('concertId')
    bname = request.get_json().get('bandName')
    duration = request.get_json().get('duration')
    begin_time = str(request.get_json().get('holdingTime'))
    hold_lcation = request.get_json().get('holdingPlace')
    db = connect_database()
    try:
        db.execute(f'''
                    UPDATE concerts
                    SET begin_time='{begin_time}',duration='{duration}',bname='{bname}',hold_location='{hold_lcation}'
                    WHERE ID='{id}'
                    ''')
    except Exception as e:
        print(e)
        return fail_api('乐队名错误或该乐队在该时间已安排演唱会!')
    return success_api('修改成功')

@perform_opt.route('/deletePerform',methods=['DELETE'])
def delete_perform():
    id = request.get_json().get('concertId')
    db = connect_database()
    db.execute(f'''
                DELETE FROM concerts
                WHERE ID ='{id}'
                ''')
    return success_api('删除成功')

@perform_opt.route('addSongPerform',methods=['POST'])
def add_sheet_perform():
    concert_id = request.get_json().get('concertId')
    bname = request.get_json().get('bandName')
    sname = request.get_json().get('songName')
    duration = request.get_json().get('duration')
    db = connect_database()
    song_order = db.execute(f'''SELECT COUNT(*)
                            FROM sheets
                            WHERE concert_id='{concert_id}'
                            ''').fetchone()[0] + 1
    try:
        db.execute(f'''
                    INSERT INTO sheets(concert_id,bname,song_order,duration,sname)
                    VALUES
                    ({concert_id},'{bname}',{song_order},'{duration}','{sname}')
                    ''')
    except Exception as e:
        print(e)
        return fail_api('请确保该乐队创作了该歌曲或表演时长值超出范围')
    return success_api('添加成功')

@perform_opt.route('editSongPerform',methods=['PUT'])
def edit_sheet_perform():
    id = request.get_json().get('sheetId')
    concert_id = request.get_json().get('concertId')
    bname = request.get_json().get('bandName')
    sname = request.get_json().get('songName')
    duration = request.get_json().get('duration')
    song_order = int(request.get_json().get('songOrder'))
    db = connect_database()
    total_songs = db.execute(f'''SELECT COUNT(*)
                            FROM sheets
                            WHERE concert_id={concert_id}
                            ''').fetchone()[0]
    if song_order > total_songs:
        return fail_api('修改失败，请确保表演顺序小于等于表演歌曲总数')
    #如果改动顺序，则与原顺序的歌曲交换表演顺序
    original_order = db.execute(f'''SELECT song_order
                                    FROM sheets
                                    WHERE ID={id}
                                    ''').fetchone()[0]
    if song_order != original_order:
        db.execute(f'''
                    UPDATE sheets
                    SET
                    song_order={song_order},duration={duration},sname='{sname}'
                    WHERE ID ={id}
                    ''')
        db.execute(f'''
                    UPDATE sheets
                    SET
                    song_order={original_order}
                    WHERE ID !={id} AND song_order={song_order}
                    ''')
    else:
        try:db.execute(f'''
                    UPDATE sheets
                    SET
                    duration={duration},sname='{sname}'
                    WHERE ID ={id}
                    ''')
        except Exception as e:
            print(e)
            return fail_api('请确保该乐队创作了该歌曲或表演时长超出范围')
    return success_api('修改成功')

@perform_opt.route('/deleteSongPerform',methods=['DELETE'])
def delete_sheet():
    ID = request.get_json().get('sheetId')
    db = connect_database()
    original_order = db.execute(f'''
                SELECT song_order 
                FROM sheets
                WHERE ID ={ID}
                ''').fetchone()[0]
    concert_id = db.execute(f'''
                    SELECT concert_id 
                    FROM sheets
                    WHERE ID ={ID}
                    ''').fetchone()[0]
    db.execute(f'''
                DELETE FROM sheets
                WHERE ID ={ID}
                ''')
    #删除后把songorder重置，即在这之后的歌曲表演顺序都减1
    db.execute(f'''
                UPDATE sheets
                SET song_order=song_order-1
                WHERE concert_id={concert_id}
                AND song_order>{original_order}
                ''')
    return success_api('删除成功')
