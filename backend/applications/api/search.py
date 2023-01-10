from flask import Blueprint
from flask import request
from itsdangerous import SignatureExpired, BadSignature
from sqlalchemy.ext.serializer import Serializer
from utils.http import success_api, fail_api
from applications.database import connect_database
from utils.create_user import user

search_opt = Blueprint('search_opt', __name__,url_prefix='/api/search')


@search_opt.route('/song',methods=['POST'])
def search_song():
    type = request.get_json().get('searchType')
    text = request.get_json().get('searchText')
    db = connect_database(username=user.username,password=user.password)
    if type == '未关注':
        json_dic = {}
        result = db.execute(f'''
                             SELECT * 
                             FROM songs
                             WHERE sname LIKE '%%{text}%%'
                             ''').fetchall()
        song_list = []
        for i in result:
            song_dic = {}
            song_dic['songName'] = i.sname
            song_dic['bandName'] = i.bname
            song_dic['albumBelong'] = i.aname
            song_dic['isEdit'] = False
            if user.role == 'fan':
                db = connect_database(username=user.username, password=user.password)
                if db.execute(f'''
                             SELECT sname 
                             FROM fan_song_own
                             WHERE sname = '{i.sname}'
                             ''').fetchone():
                    song_dic['isLike'] = True
                else:
                    song_dic['isLike'] = False

            if not song_dic['isLike']:
                song_list.append(song_dic)

        total = len(song_list)
        json_dic['total'] = total
        json_dic['searchSongData'] = song_list
        return success_api(data=json_dic)

    elif type == '已关注':
        json_dic = {}
        db = connect_database(username=user.username, password=user.password)
        result = db.execute(f'''
                             SELECT * 
                             FROM fan_song_own
                             WHERE sname LIKE '%%{text}%%'
                             ''').fetchall()
        song_list = []
        for i in result:
            song_dic = {}
            song_dic['songName'] = i.sname
            song_dic['bandName'] = i.bname
            song_dic['albumBelong'] = i.aname
            song_dic['isEdit'] = False
            song_dic['isLike'] = True
            song_list.append(song_dic)

        total = len(result)
        json_dic['total'] = total
        json_dic['searchSongData'] = song_list
        return success_api(data=json_dic)

    else:
        json_dic = {}
        result = db.execute(f'''
                            SELECT * 
                            FROM songs
                            WHERE sname LIKE '%%{text}%%'
                             ''').fetchall()
        song_list = []
        for i in result:
            song_dic = {}
            song_dic['songName'] = i.sname
            song_dic['bandName'] = i.bname
            song_dic['albumBelong'] = i.aname
            song_dic['isEdit'] = False
            if user.role == 'fan':
                db = connect_database(username=user.username, password=user.password)
                if db.execute(f'''
                                        SELECT sname 
                                        FROM fan_song_own
                                        WHERE sname='{i.sname}'
                                        ''').fetchone():
                    song_dic['isLike'] = True
                else:
                    song_dic['isLike'] = False
            song_list.append(song_dic)

        total = len(result)
        json_dic['total'] = total
        json_dic['searchSongData'] = song_list
        return success_api(data=json_dic)

@search_opt.route('/album',methods=['POST'])
def search_album():
    type = request.get_json().get('searchType')
    text = request.get_json().get('searchText')
    db = connect_database(username=user.username,password=user.password)
    if type == '未关注':
        json_dic = {}
        result = db.execute(f'''
                             SELECT * 
                             FROM albums
                             WHERE aname LIKE '%%{text}%%'
                             ''').fetchall()
        album_list=[]
        for i in result:
            album_dic = {}
            album_dic['albumId'] = i.ID
            album_dic['albumName'] = i.aname
            album_dic['performBand'] = i.bname
            album_dic['releaseTime'] = str(i.release_time)
            album_dic['releaseCompany'] = i.release_company
            album_dic['isEdit'] = False
            if user.role == 'fan':
                db = connect_database(username=user.username, password=user.password)
                if db.execute(f'''
                             SELECT aname 
                             FROM fan_album_own
                             WHERE aname = '{i.aname}'
                             ''').fetchone():
                    album_dic['isLike'] = True
                else:
                    album_dic['isLike'] = False

            if not album_dic['isLike']:
                album_list.append(album_dic)

        total = len(album_list)
        json_dic['total'] = total
        json_dic['searchAlbumData'] = album_list
        return success_api(data=json_dic)

    elif type == '已关注':
        json_dic = {}
        db = connect_database(username=user.username, password=user.password)
        result = db.execute(f'''
                             SELECT * 
                             FROM fan_album_own
                             WHERE aname LIKE '%%{text}%%'
                             ''').fetchall()
        album_list = []
        for i in result:
            album_dic = {}
            album_dic['albumName'] = i.aname
            album_dic['performBand'] = i.bname
            album_dic['releaseTime'] = str(i.release_time)
            album_dic['releaseCompany'] = i.release_company
            album_dic['isEdit'] = False
            album_dic['isLike'] = True
            album_list.append(album_dic)


        total = len(result)
        json_dic['total'] = total
        json_dic['searchAlbumData'] = album_list
        return success_api(data=json_dic)

    else:
        json_dic = {}
        result = db.execute(f'''
                            SELECT * 
                            FROM albums
                            WHERE aname LIKE '%%{text}%%'
                             ''').fetchall()
        album_list = []
        for i in result:
            album_dic = {}
            album_dic['albumId'] = i.ID
            album_dic['albumName'] = i.aname
            album_dic['performBand'] = i.bname
            album_dic['releaseTime'] = str(i.release_time)
            album_dic['releaseCompany'] = i.release_company
            album_dic['isEdit'] = False
            if user.role == 'fan':
                db = connect_database(username=user.username, password=user.password)
                if db.execute(f'''
                                SELECT aname 
                                FROM fan_album_own
                                WHERE aname ='{i.aname}'
                                ''').fetchone():
                    album_dic['isLike'] = True
                else:
                    album_dic['isLike'] = False
            album_list.append(album_dic)

        total = len(album_list)
        json_dic['total'] = total
        json_dic['searchAlbumData'] = album_list
        return success_api(data=json_dic)


@search_opt.route('/concert',methods=['POST'])
def search_concert():
    type = request.get_json().get('searchType')
    text = request.get_json().get('searchText')
    db = connect_database(username=user.username,password=user.password)
    if type == '未关注':
        json_dic = {}
        result = db.execute(f'''
                             SELECT * 
                             FROM concerts
                             WHERE bname LIKE '%%{text}%%'
                             ''').fetchall()
        concert_list = []
        for i in result:
            concert_dic = {}
            concert_dic['concertId'] = i.ID
            concert_dic['holdingTime'] = str(i.begin_time)
            concert_dic['bandName'] = i.bname
            concert_dic['duration'] = i.duration
            concert_dic['holdingPlace'] = i.hold_location
            concert_dic['isEdit'] = False
            acting_list = []
            acting_result = db.execute(f'''
                                        SELECT sheets.*,concerts.begin_time FROM concerts,sheets
                                        WHERE sheets.concert_id = concerts.ID
                                        AND sheets.bname = concerts.bname
                                        AND concerts.bname='{i.bname}'
                                        ''').fetchall()
            for j in acting_result:
                acting_dic = {}
                acting_dic['id'] = j.ID
                acting_dic['holdingTime'] = str(j.begin_time)
                acting_dic['bandName'] = j.bname
                acting_dic['songName'] = j.sname
                acting_dic['songOrder'] = j.song_order
                acting_dic['sheetId'] = j.ID
                acting_dic['concertId'] = j.concert_id
                acting_dic['duration'] = j.duration
                acting_dic['isEdit'] = False
                acting_list.append(acting_dic)

            concert_dic['actingSongData'] = acting_list
            if user.role == 'fan':
                db = connect_database(username=user.username, password=user.password)
                if db.execute(f'''
                             SELECT bname,begin_time 
                             FROM fan_concert_own
                             WHERE bname='{j.bname}' AND begin_time='{str(j.begin_time)}'
                             ''').fetchone():
                    concert_dic['isLike'] = True
                else:
                    concert_dic['isLike'] = False

            if not concert_dic['isLike']:
                concert_list.append(concert_dic)

        total = len(concert_list)
        json_dic['total'] = total
        json_dic['searchConcertData'] = concert_list
        return success_api(data=json_dic)

    elif type == '已关注':
        json_dic = {}
        result = db.execute(f'''
                            SELECT * 
                            FROM concerts
                            WHERE bname LIKE '%%{text}%%'
                            ''').fetchall()
        concert_list = []
        for i in result:
            concert_dic = {}
            concert_dic['concertId'] = i.ID
            concert_dic['holdingTime'] = str(i.begin_time)
            concert_dic['bandName'] = i.bname
            concert_dic['duration'] = i.duration
            concert_dic['holdingPlace'] = i.hold_location
            concert_dic['isEdit'] = False
            acting_list = []
            acting_result = db.execute(f'''
                                               SELECT sheets.*,concerts.begin_time FROM concerts,sheets
                                               WHERE sheets.concert_id = concerts.ID
                                               AND sheets.bname = concerts.bname
                                               AND concerts.bname='{i.bname}'
                                               ''').fetchall()
            for j in acting_result:
                acting_dic = {}
                acting_dic['id'] = j.ID
                acting_dic['holdingTime'] = str(j.begin_time)
                acting_dic['bandName'] = j.bname
                acting_dic['songName'] = j.sname
                acting_dic['songOrder'] = j.song_order
                acting_dic['sheetId'] = j.ID
                acting_dic['concertId'] = j.concert_id
                acting_dic['duration'] = j.duration
                acting_dic['isEdit'] = False
                acting_list.append(acting_dic)

            concert_dic['actingSongData'] = acting_list
            if user.role == 'fan':
                db = connect_database(username=user.username, password=user.password)
                if db.execute(f'''
                                    SELECT bname,begin_time 
                                    FROM fan_concert_own
                                    WHERE bname='{j.bname}' AND begin_time='{str(j.begin_time)}'
                                    ''').fetchone():
                    concert_dic['isLike'] = True
                else:
                    concert_dic['isLike'] = False

            if  concert_dic['isLike']:
                concert_list.append(concert_dic)

        total = len(concert_list)
        json_dic['total'] = total
        json_dic['searchConcertData'] = concert_list
        return success_api(data=json_dic)

    else:
        json_dic = {}
        result = db.execute(f'''
                             SELECT * 
                             FROM concerts
                             WHERE bname LIKE '%%{text}%%'
                             ''').fetchall()
        concert_list = []
        for i in result:
            concert_dic = {}
            concert_dic['concertId'] = i.ID
            concert_dic['holdingTime'] = str(i.begin_time)
            concert_dic['bandName'] = i.bname
            concert_dic['duration'] = i.duration
            concert_dic['holdingPlace'] = i.hold_location
            concert_dic['isEdit'] = False
            acting_list = []
            acting_result = db.execute(f'''
                                        SELECT sheets.*,concerts.begin_time FROM concerts,sheets
                                        WHERE sheets.concert_id = concerts.ID
                                        AND sheets.bname = concerts.bname
                                        AND concerts.bname='{i.bname}'
                                        ''').fetchall()
            for j in acting_result:
                acting_dic = {}
                acting_dic['id'] = j.ID
                acting_dic['holdingTime'] = str(j.begin_time)
                acting_dic['bandName'] = j.bname
                acting_dic['songName'] = j.sname
                acting_dic['songOrder'] = j.song_order
                acting_dic['sheetId'] = j.ID
                acting_dic['concertId'] = j.concert_id
                acting_dic['duration'] = j.duration
                acting_dic['isEdit'] = False
                acting_list.append(acting_dic)

            concert_dic['isLike'] = False
            concert_dic['actingSongData'] = acting_list
            if user.role == 'fan':
                db = connect_database(username=user.username, password=user.password)
                if db.execute(f'''
                             SELECT bname,begin_time 
                             FROM fan_concert_own
                             WHERE bname='{j.bname}' AND begin_time='{str(j.begin_time)}'
                             ''').fetchone():
                    concert_dic['isLike'] = True
                else:
                    concert_dic['isLike'] = False

            concert_list.append(concert_dic)

        total = len(result)
        json_dic['total'] = total
        json_dic['searchConcertData'] = concert_list
        return success_api(data=json_dic)

@search_opt.route('/band',methods=['POST'])
def search_band():
    type = request.get_json().get('searchType')
    text = request.get_json().get('searchText')
    db = connect_database(username=user.username, password=user.password)
    if type == '未关注':
        band_result = db.execute(f'''
                                   SELECT * 
                                   FROM bands 
                                   WHERE bname LIKE '%%{text}%%'
                                ''').fetchall()
        band_list = []
        json_dic = {}
        for i in band_result:
            member_list = []
            band_members = db.execute(f'''
                                       SELECT * 
                                       FROM members 
                                       where bname = '{i.bname}'
                                       ''').fetchall()
            for j in band_members:
                member_dic = {}
                member_dic['memberId'] = j.ID
                member_dic['memberName'] = j.mname
                member_dic['bandName'] = j.bname
                member_dic['memberSex'] = j.sex
                member_dic['memberAge'] = j.age
                member_dic['memberJob'] = j.job
                member_dic['memberPosition'] = j.capacity
                member_dic['joinTime'] = str(j.join_time)
                member_dic['leaveTime'] = str(j.leave_time)
                member_dic['isEdit'] = False
                member_list.append(member_dic)

            album_num = db.execute(f'''
                                  SELECT COUNT(*)
                                  FROM albums
                                  WHERE bname = "{i.bname}"
                                   ''').fetchone()[0]
            band_dic = {}
            band_dic['bandId'] = i.band_id
            band_dic['bandName'] = i.bname
            band_dic['bandLeader'] = i.leader
            band_dic['fundationTime'] = str(i.establish_time)
            band_dic['bandNumber'] = i.num
            band_dic['albumNumber'] = album_num
            band_dic['isEdit'] = False
            band_dic['memberData'] = member_list
            if user.role == 'fan':
                db = connect_database(username=user.username, password=user.password)
                if db.execute(f'''
                             SELECT bname
                             FROM fan_band_own
                             WHERE bname='{i.bname}'
                             ''').fetchone():
                    band_dic['isLike'] = True
                else:
                    band_dic['isLike'] = False
            if not band_dic['isLike']:
                band_list.append(band_dic)
        total = len(band_list)
        json_dic['total'] = total
        json_dic['searchBandData'] = band_list
        return success_api('查询成功', data=json_dic)

    elif type == '已关注':
        band_result = db.execute(f'''
                                  SELECT * 
                                  FROM fan_band_own
                                  WHERE bname LIKE '%%{text}%%'
                                   ''').fetchall()
        band_list = []
        json_dic = {}
        for i in band_result:
            member_list = []
            band_members = db.execute(f'''
                                      SELECT * 
                                      FROM members 
                                      where bname = '{i.bname}'
                                      ''').fetchall()
            for j in band_members:
                member_dic = {}
                member_dic['memberId'] = j.ID
                member_dic['memberName'] = j.mname
                member_dic['bandName'] = j.bname
                member_dic['memberSex'] = j.sex
                member_dic['memberAge'] = j.age
                member_dic['memberJob'] = j.job
                member_dic['memberPosition'] = j.capacity
                member_dic['joinTime'] = str(j.join_time)
                member_dic['leaveTime'] = str(j.leave_time)
                member_dic['isEdit'] = False
                member_list.append(member_dic)

            album_num = db.execute(f'''
                                     SELECT COUNT(*)
                                     FROM albums
                                     WHERE bname = "{i.bname}"
                                      ''').fetchone()[0]
            band_dic = {}
            band_dic['bandName'] = i.bname
            band_dic['bandLeader'] = i.leader
            band_dic['fundationTime'] = str(i.establish_time)
            band_dic['bandNumber'] = i.num
            band_dic['albumNumber'] = album_num
            band_dic['isEdit'] = False
            band_dic['memberData'] = member_list
            band_dic['isLike'] = True
            band_list.append(band_dic)

        total = len(band_result)
        json_dic['total'] = total
        json_dic['searchBandData'] = band_list
        return success_api('查询成功', data=json_dic)

    else :
        band_result = db.execute(f'''
                                  SELECT * 
                                  FROM bands 
                                  WHERE bname LIKE '%%{text}%%'
                                   ''').fetchall()
        band_list = []
        json_dic = {}
        for i in band_result:
            member_list = []
            band_members = db.execute(f'''
                                          SELECT * 
                                          FROM members 
                                          where bname = '{i.bname}'
                                          ''').fetchall()
            for j in band_members:
                member_dic = {}
                member_dic['memberId'] = j.ID
                member_dic['memberName'] = j.mname
                member_dic['bandName'] = j.bname
                member_dic['memberSex'] = j.sex
                member_dic['memberAge'] = j.age
                member_dic['memberJob'] = j.job
                member_dic['memberPosition'] = j.capacity
                member_dic['joinTime'] = str(j.join_time)
                member_dic['leaveTime'] = str(j.leave_time)
                member_dic['isEdit'] = False
                member_list.append(member_dic)

            album_num = db.execute(f'''
                                     SELECT COUNT(*)
                                     FROM albums
                                     WHERE bname = "{i.bname}"
                                      ''').fetchone()[0]
            band_dic = {}
            band_dic['bandName'] = i.bname
            band_dic['bandLeader'] = i.leader
            band_dic['fundationTime'] = str(i.establish_time)
            band_dic['bandNumber'] = i.num
            band_dic['albumNumber'] = album_num
            band_dic['isEdit'] = False
            band_dic['memberData'] = member_list
            if user.role == 'fan':
                db = connect_database(username=user.username, password=user.password)
                if db.execute(f'''
                              SELECT bname
                              FROM fan_band_own
                              WHERE bname='{i.bname}'
                              ''').fetchone():
                    band_dic['isLike'] = True
                else:
                    band_dic['isLike'] = False
            band_list.append(band_dic)

        total = len(band_result)
        json_dic['total'] = total
        json_dic['searchBandData'] = band_list
        return success_api('查询成功', data=json_dic)