from flask import Blueprint
from flask import request
from utils.http import success_api, fail_api
from applications.database import connect_database

from utils.create_user import user
band_opt = Blueprint('band_opt', __name__, url_prefix='/api/band')


@band_opt.route('/addBand',methods=['POST'])
def add_band_post():
    # 添加乐队
    # 获取输入框内容
    # 把用户名和密码注册到数据库中
    band_id = request.get_json().get('bandId')
    bname = request.get_json().get('bandName')
    password = request.get_json().get('bandPwd')
    leader = request.get_json().get('bandLeader')
    num = request.get_json().get('bandNumber')
    fund_time = request.get_json().get('fundationTime')
    memberdata = request.get_json().get('memberData')[0]
    join_time = memberdata['joinTime']
    age = memberdata['memberAge']
    job = memberdata['memberJob']
    name = memberdata['memberName']
    capacity = memberdata['memberPositon']
    sex = memberdata['memberSex']
    try:
        db = connect_database()
        db.execute(f"CREATE USER '{band_id}'@'localhost' IDENTIFIED BY '{password}'")
        try:
            db.execute(f"INSERT INTO bands VALUES('{band_id}','{bname}','{leader}','{fund_time}',{num})")
            db.execute(f'''INSERT INTO members(mname,sex,age,bname,job,capacity,join_time,leave_time)
                             VALUES('{name}','{sex}',{age},'{bname}','{job}','{capacity}','{join_time}',null)
                        ''')
        except Exception as e:
            print(e)
            return fail_api('年龄不合法，请输入12-99岁之间的年龄!')
    except Exception as e:
        print(e)
        return fail_api('添加失败，该乐队已存在')
    return success_api('添加成功')

@band_opt.route('/editBand',methods=['PUT'])
def update_band():
    band_id = request.get_json().get('bandId')
    bname = request.get_json().get('bandName')
    leader = request.get_json().get('bandLeader')
    fund_time = request.get_json().get('fundationTime')
    db = connect_database()
    query1 = db.execute(f'''
                    SELECT mname
                    FROM members
                    WHERE mname = '{leader}'
                    ''').fetchone()

    if query1 is None:
        return fail_api('该队长在成员列表中不存在，请重新输入正确的队长名称!')

    query2 = db.execute(f'''
                           SELECT leave_time IS  NULL AND bname = '{bname}'
                           FROM members
                           WHERE mname = '{leader}' 
                        ''').fetchone()[0]
    if query2 == 1:
        try:
            if user.role == "band":
                band_id = user.username
            db.execute(f'''UPDATE BANDS
                            SET bname = '{bname}',leader = '{leader}',establish_time = '{fund_time}'
                            WHERE band_id = '{band_id}'
                        ''')
            db.execute(f'''UPDATE members
                            SET capacity = '队员'
                            WHERE bname = '{bname}' AND capacity = '队长'
                            ''')
            db.execute(f'''UPDATE members
                            SET capacity = '队长'
                            WHERE bname = '{bname}' AND mname = '{leader}'
                            ''')
            return success_api('修改成功')
        except Exception as e:
            print(e)
            return fail_api('该乐队已存在，不能使用这个乐队名!')
    else:
        return fail_api('指定队长不是本乐队的成员或已离队!')

@band_opt.route('/deleteBand',methods=['DELETE'])
def delete_band():
    ID = request.get_json().get('bandId')
    db = connect_database()
    db.execute(f'''
                    DELETE 
                    FROM bands
                    WHERE band_id = '{ID}'
                ''')
    db.execute(f'''
                DROP USER'{ID}'@'localhost'
                ''')
    return success_api('删除成功!')

@band_opt.route('/addMember',methods=['POST'])
#前端对年龄作了输入范围限制，在这里后端不做判断了，下同
def add_member():
    db = connect_database()
    bname = request.get_json().get('bandName')
    join_time = str(request.get_json().get('joinTime'))
    leave_time = str(request.get_json().get('leave_time'))
    age = request.get_json().get('memberAge')
    job = request.get_json().get('memberJob')
    name = request.get_json().get('memberName')
    capacity = request.get_json().get('memberPosition')
    sex = request.get_json().get('memberSex')
    if leave_time == 'None':
        try:
            db.execute(f'''
                        INSERT INTO members(mname,sex,age,bname,job,capacity,join_time,leave_time)
                        VALUES('{name}','{sex}',{age},'{bname}','{job}','{capacity}','{join_time}',null)
                        ''')
        except Exception as e:
            print(e)
            return fail_api('添加失败，请确保该队员所在乐队存在!')
    else:
        try:
            db.execute(f'''
                        INSERT INTO members(mname,sex,age,bname,job,capacity,join_time,leave_time)
                        VALUES('{name}','{sex}',{age},'{bname}','{job}','{capacity}','{join_time}','{leave_time}')
                        ''')
        except Exception as e:
            print(e)
            return fail_api('添加失败，请确保该队员所在乐队存在!')
    return success_api('添加成功')

@band_opt.route('/editMember',methods=['PUT'])
def edit_member():
    db = connect_database()
    ID = request.get_json().get('memberId')
    bname = request.get_json().get('bandName')
    join_time = str(request.get_json().get('joinTime'))
    leave_time = str(request.get_json().get('leave_time'))
    age = request.get_json().get('memberAge')
    job = request.get_json().get('memberJob')
    name = request.get_json().get('memberName')
    capacity = request.get_json().get('memberPosition')
    sex = request.get_json().get('memberSex')
    print(capacity)
    if capacity == '队长':
        #如果是修改队长，则将本队原来的队长先修改成队员，再将此人修改为队长(如果原队长和此人是同一个人仍有效)
        db.execute(f'''
                    UPDATE members
                    SET capacity='队员'
                    WHERE bname='{bname}' AND capacity='队长'
                    ''')
        db.execute(f'''
                    UPDATE members
                    SET capacity='队长'
                    WHERE bname='{bname}' AND ID={ID}
                    ''')
    #如果离开时间为null执行下面语句
        if leave_time == 'None':
            try:
                db.execute(f'''
                            UPDATE members
                            SET mname='{name}',sex='{sex}',age={age},job='{job}',join_time='{join_time}',leave_time=null
                            WHERE ID = {ID};
                            ''')
            except Exception as e:
                print(e)
                return fail_api('请输入12-99岁之间的年龄')
        else:
            try:
                db.execute(f'''
                            UPDATE members
                            SET mname='{name}',sex='{sex}',age={age},job='{job}',join_time='{join_time}',leave_time='{leave_time}'
                            WHERE ID = {ID};
                            ''')
            except Exception as e:
                print(e)
                return fail_api('请输入12-99岁之间的年龄')
    #职位为队员的修改语句
    else:
        if leave_time == 'None':
            try:
                db.execute(f'''
                            UPDATE members
                            SET mname='{name}',sex='{sex}',age={age},job='{job}',capacity='{capacity}',
                            join_time='{join_time}',leave_time=null
                            WHERE ID = {ID};
                            ''')
            except Exception as e:
                print(e)
                return fail_api('请输入12-99岁之间的年龄')
        else:
            try:
                db.execute(f'''
                            UPDATE members
                            SET mname='{name}',sex='{sex}',age={age},job='{job}',capacity='{capacity}',
                            join_time='{join_time}',leave_time='{leave_time}'
                            WHERE ID = {ID};
                            ''')
            except Exception as e:
                print(e)
                return fail_api('请输入12-99岁之间的年龄')
    return success_api('修改成功')

@band_opt.route('/deleteMember',methods=['DELETE'])
def delete_member():
    id = request.get_json().get('memberId')
    db = connect_database()
    db.execute(f'''
                DELETE 
                FROM members
                WHERE ID = {id}
                ''')
    return success_api('删除成功')

@band_opt.route('/getFanOverLook',methods=['GET'])
def get_fan_overlook():
    db = connect_database(username=user.username,password=user.password)
    fan_num_reult = db.execute(f'''
                                SELECT * FROM 
                                band_age''').fetchall()
    total_fan = db.execute(f'''
                            SELECT * FROM 
                            band_total_fans''').fetchone()[0]
    total_man_fans = db.execute(f'''
                                SELECT * FROM 
                                band_total_manfans''').fetchone()[0]
    total_woman_fans = db.execute(f'''
                                SELECT * FROM 
                                band_total_womanfans''').fetchone()[0]
    band_most_favorite_song = db.execute(f'''
                                        SELECT * FROM 
                                        band_favorite''').fetchone().sname
    fanAgeData = []
    for i in fan_num_reult:
        fanage1 = {'value':int(i.age1),'name':'6~18岁'}
        fanage2 = {'value': int(i.age2), 'name': '19~30岁'}
        fanage3 = {'value':int(i.age3), 'name': '31~50岁'}
        fanage4 = {'value': int(i.age4), 'name': '50岁以上'}

    fanAgeData.append(fanage1)
    fanAgeData.append(fanage2)
    fanAgeData.append(fanage3)
    fanAgeData.append(fanage4)

    fanGenderData = []
    fan_man = {'value':total_man_fans,'name':"男"}
    fan_woman = {'value':total_woman_fans,'name':"女"}
    fanGenderData.append(fan_man)
    fanGenderData.append(fan_woman)
    return success_api('查询成功',data={"fanNum":total_fan,"mostLikeSong":band_most_favorite_song,
                                        "fanGenderData":fanGenderData,"fanAgeData":fanAgeData})