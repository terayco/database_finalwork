from flask import Blueprint
from flask import request
from utils.http import success_api, fail_api
from applications.database import connect_database

from utils.create_user import user
album_opt = Blueprint('album_opt', __name__, url_prefix='/api/album')


@album_opt.route('/addAlbum',methods=['POST'])
def add_album_post():
    album_name = request.get_json().get('albumName')
    perform_band = request.get_json().get('performBand')
    release_company = request.get_json().get('releaseCompany')
    release_time = str(request.get_json().get('releaseTime'))
    try:
        db = connect_database()
        db.execute(f'''
                    INSERT INTO albums(aname,bname,release_time,release_company)
                    VALUES
                    ('{album_name}','{perform_band}','{release_time}','{release_company}')
                    ''')
    except Exception as e:
        print(e)
        return fail_api('该专辑已存在或表演乐队不存在!')
    return success_api('添加成功')

@album_opt.route('/editAlbum',methods=['PUT'])
def update_album_post():
    try:
        album_id = request.get_json().get('albumId')
        album_name = request.get_json().get('albumName')
        perform_band = request.get_json().get('performBand')
        release_company = request.get_json().get('releaseCompany')
        release_time = str(request.get_json().get('releaseTime'))
        db = connect_database()
        db.execute(f'''
                    UPDATE albums
                    SET
                    aname='{album_name}',bname='{perform_band}',release_time='{release_time}',release_company='{release_company}'
                    WHERE ID = {album_id}
                    ''')
        return success_api('修改成功')
    except Exception as e:
        print(e)
        return fail_api('修改失败，请确保发行该专辑的乐队存在')

@album_opt.route('/deleteAlbum',methods=['DELETE'])
def delete_album_post():
    ID = request.get_json().get('albumId')
    db = connect_database()
    db.execute(f'''
                DELETE
                FROM albums
                WHERE ID='{ID}'
                ''')
    return success_api('删除成功')