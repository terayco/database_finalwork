from flask import Blueprint
from flask import request
from utils.http import success_api, fail_api
from applications.database import connect_database
from utils.create_user import user

song_opt = Blueprint('song_opt', __name__, url_prefix='/api/song')


@song_opt.route('/addSong',methods=['POST'])
def add_song():
    sname = request.get_json().get('songName')
    bname = request.get_json().get('bandName')
    aname = request.get_json().get('albumBelong')
    try:
        db = connect_database()
        db.execute(f'''
                    INSERT INTO songs(sname,bname,aname)
                    VALUES
                    ('{sname}','{bname}','{aname}')
                    ''')
    except Exception as e:
        print(e)
        return fail_api('所属专辑不存在或已存在该歌曲!')
    return success_api('添加成功')

@song_opt.route('/editSong',methods=['PUT'])
def edit_song():
    ID = request.get_json().get('songId')
    sname = request.get_json().get('songName')
    bname = request.get_json().get('bandName')
    aname = request.get_json().get('albumBelong')
    try:
        db = connect_database()
        db.execute(f'''
                    UPDATE songs
                    SET sname='{sname}',bname='{bname}',aname='{aname}'
                    WHERE ID ='{ID}'
                    ''')
    except Exception as e:
        print(e)
        return fail_api('该歌曲已存在或所属专辑不存在!')
    return success_api('修改成功')

@song_opt.route('/deleteSong',methods=['DELETE'])
def delete_song():
    ID = request.get_json().get('bandId')
    db = connect_database()
    db.execute(f'''
                DELETE FROM songs
                WHERE ID ='{ID}'
                ''')
    return success_api('删除成功')

