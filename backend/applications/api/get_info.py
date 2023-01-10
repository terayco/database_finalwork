from flask import Blueprint, request
from applications.database import connect_database
from utils.http import success_api, fail_api
from utils.create_user import user
info_opt = Blueprint('info_opt', __name__, url_prefix='/api/list')



@info_opt.route('',methods=['GET'])
def get_info():
    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))
    type = int(request.args.get('type'))
    db = connect_database()
    #查询乐队及成员信息
    if type == 1:
        info = int(request.args.get('info'))
        if info == 0:
            band_result = db.execute(f'''
                                    SELECT * 
                                    FROM bands 
                                    LIMIT {limit} 
                                    OFFSET {(page-1)*limit}''').fetchall()
            total = db.execute('SELECT COUNT(*) FROM bands').fetchone()[0]
        else:
            band_result = db.execute(f'''
                                    SELECT * 
                                    FROM bands 
                                    WHERE band_id='{user.username}'
                                    ''').fetchall()
            total = len(band_result)
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
            band_list.append(band_dic)
            if user.role == 'fan':
                db = connect_database(username=user.username,password=user.password)
                if db.execute(f'''
                              SELECT bname
                              FROM fan_band_own
                              WHERE bname='{i.bname}'
                              ''').fetchone():
                    band_dic['isLike'] = True
                else:
                    band_dic['isLike'] = False

        json_dic['total'] = total
        json_dic['bandData'] = band_list
        return success_api('查询成功',data=json_dic)

    # 查询专辑信息
    if type == 2:
        info = int(request.args.get('info'))
        json_dic = {}
        if info == 0:
            album_result = db.execute(f'''
                                          SELECT * 
                                          FROM albums 
                                          LIMIT {limit} 
                                          OFFSET {(page - 1) * limit}''').fetchall()
            total = db.execute('SELECT COUNT(*) FROM albums').fetchone()[0]
        else:
            album_result = db.execute(f'''
                                      SELECT albums.* 
                                      FROM albums,bands 
                                      WHERE albums.bname=bands.bname 
                                      AND band_id='{user.username}'
                                      LIMIT {limit} 
                                      OFFSET {(page - 1) * limit}
                                      ''').fetchall()
            total = len(album_result)
        album_list=[]
        for i in album_result:
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
                              WHERE aname='{i.aname}'
                              ''').fetchone():
                    album_dic['isLike'] = True
                else:
                    album_dic['isLike'] = False
            album_list.append(album_dic)


        json_dic['total'] = total
        json_dic['albumData'] = album_list
        return success_api(data=json_dic)

    # 查询歌曲信息
    if type == 3:
        info = int(request.args.get('info'))
        json_dic = {}
        if info == 0:
            result = db.execute(f'''
                                 SELECT * 
                                 FROM songs
                                 LIMIT {limit} 
                                 OFFSET {(page - 1) * limit}''').fetchall()
            total = db.execute('SELECT COUNT(*) FROM songs').fetchone()[0]
        else:
            result = db.execute(f'''
                                  SELECT songs.* 
                                  FROM songs,bands 
                                  WHERE songs.bname=bands.bname 
                                  AND band_id='{user.username}'
                                  LIMIT {limit} 
                                  OFFSET {(page - 1) * limit}''').fetchall()
            total = len(result)
        song_list = []
        for i in result:
            song_dic = {}
            song_dic['songId'] = i.ID
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

        json_dic['total'] = total
        json_dic['songData'] = song_list
        return success_api(data=json_dic)

    # 查询演唱会及歌单信息
    if type == 4:
        info = int(request.args.get('info'))
        json_dic = {}
        if info == 0:
            result = db.execute(f'''
                                 SELECT * 
                                 FROM concerts
                                 LIMIT {limit} 
                                 OFFSET {(page - 1) * limit}''').fetchall()
            total = db.execute('SELECT COUNT(*) FROM concerts').fetchone()[0]
        else:
            result = db.execute(f'''
                                  SELECT concerts.* 
                                  FROM concerts,bands 
                                  WHERE concerts.bname=bands.bname 
                                  AND band_id='{user.username}'
                                  LIMIT {limit} 
                                  OFFSET {(page - 1) * limit}''').fetchall()
            total = len(result)

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
            concert_list.append(concert_dic)

        json_dic['total'] = total
        json_dic['performData'] = concert_list
        return success_api(data=json_dic)

    # 查询粉丝信息
    if type == 5:
        if user.role == 'band':
            db = connect_database(username=user.username, password=user.password)
            json_dic = {}
            result = db.execute(f'''
                                 SELECT * 
                                 FROM band_fans
                                 LIMIT {limit} 
                                 OFFSET {(page - 1) * limit}''').fetchall()
            fan_list = []
            for i in result:
                fan_dic = {}
                fan_dic['fanName'] = i.fname
                fan_dic['fanSex'] = i.sex
                fan_dic['fanAge'] = i.age
                fan_dic['fanCareer'] = i.occupation
                fan_dic['isEdit'] = False
                fan_list.append(fan_dic)

            total = db.execute('SELECT COUNT(*) FROM band_fans').fetchone()[0]
            json_dic['total'] = total
            json_dic['fanData'] = fan_list
            return success_api('查询成功', data=json_dic)

        elif user.role == 'admin':
            db = connect_database()
            json_dic = {}
            result = db.execute(f'''
                                 SELECT * 
                                 FROM fans
                                 LIMIT {limit} 
                                 OFFSET {(page - 1) * limit}''').fetchall()
            fan_list = []
            for i in result:
                fan_dic = {}
                fan_dic['fanId'] = i.fan_id
                fan_dic['fanName'] = i.fname
                fan_dic['fanSex'] = i.sex
                fan_dic['fanAge'] = i.age
                fan_dic['fanCareer'] = i.occupation
                fan_dic['isEdit'] = False
                fan_list.append(fan_dic)

            total = db.execute('SELECT COUNT(*) FROM fans').fetchone()[0]
            json_dic['total'] = total
            json_dic['fanData'] = fan_list
            return success_api('查询成功', data=json_dic)

    return fail_api('查询失败')

