from flask import Blueprint
from flask import request
from itsdangerous import SignatureExpired, BadSignature
from sqlalchemy.ext.serializer import Serializer
from utils.http import success_api, fail_api
from applications.database import connect_database

from utils.create_user import user
user_opt = Blueprint('user_opt', __name__,url_prefix='/api/user')


@user_opt.route('/register/fan',methods=['POST'])
# 获取注册请求及处理
def register_add_fan():
    # 把用户名和密码注册到数据库中
    # 获取输入框内容
    username = request.get_json().get('username')
    password = request.get_json().get('password')
    fname = request.get_json().get('fname')
    sex = request.get_json().get('sex')
    age = request.get_json().get('age')
    career = request.get_json().get('career')
    try:
        db = connect_database()
        db.execute(f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}'")
        try:
            db.execute(f"INSERT INTO fans VALUES('{username}','{fname}','{sex}',{age},'{career}')")
            db.execute(f"GRANT SELECT ON final.* TO '{username}'@'localhost'")
            db.execute(f"GRANT UPDATE ON fan_own TO '{username}'@'localhost'")
        except Exception as e:
            print(e)
            db.execute(f"DROP USER '{username}'@'localhost'")
            return fail_api('请输入6-120岁之间的年龄!')
    except Exception as e:
        print(e)
        return fail_api('注册失败，账号已存在!')
    return success_api('注册成功!')

@user_opt.route('/register/band',methods=['POST'])
# 获取注册请求及处理
def register_add_band():
    # 把用户名和密码注册到数据库中
    # 获取输入框内容
    band_id = request.get_json().get('band_id')
    bname = request.get_json().get('bandName')
    password = request.get_json().get('bandPwd')
    leader = request.get_json().get('bandLeader')
    num = request.get_json().get('bandNumber')
    fund_time = request.get_json().get('fundationTime')
    memberdata = request.get_json().get('memberData')[0]
    join_time = memberdata['joinTime']
    age = int(memberdata['memberAge'])
    job = memberdata['memberJob']
    name = memberdata['memberName']
    capacity = memberdata['memberPosition']
    sex = memberdata['memberSex']
    try:
        db = connect_database()
        db.execute(f"CREATE USER '{band_id}'@'localhost' IDENTIFIED BY '{password}'")
        try:
            db.execute(f"INSERT INTO bands VALUES('{band_id}','{bname}','{leader}','{fund_time}',{num})")
            db.execute(f'''INSERT INTO members(mname,sex,age,bname,job,capacity,join_time,leave_time)
                                VALUES('{name}','{sex}',{age},'{bname}','{job}','{capacity}','{join_time}',null)
                        ''')
            db.execute(f"GRANT SELECT ON band_age TO '{band_id}'@'localhost'")
            db.execute(f"GRANT SELECT ON band_fans TO '{band_id}'@'localhost'")
            db.execute(f"GRANT SELECT ON band_favorite TO '{band_id}'@'localhost'")
            db.execute(f"GRANT SELECT ON band_total_fans TO '{band_id}'@'localhost'")
            db.execute(f"GRANT SELECT ON band_total_manfans TO '{band_id}'@'localhost'")
            db.execute(f"GRANT SELECT ON band_total_womanfans TO '{band_id}'@'localhost'")
            db.execute(f"GRANT ALL PRIVILEGES ON band_own TO '{band_id}'@'localhost'")
            db.execute(f"GRANT ALL PRIVILEGES ON band_album TO '{band_id}'@'localhost'")
            db.execute(f"GRANT ALL PRIVILEGES ON band_concert TO '{band_id}'@'localhost'")
            db.execute(f"GRANT ALL PRIVILEGES ON band_song TO '{band_id}'@'localhost'")
        except Exception as e:
            print(e)
            db.execute(f"DROP USER '{band_id}'@'localhost'")
            return fail_api('请输入12-99岁之间的年龄!')
    except Exception as e:
        print(e)
        return fail_api('添加失败，该乐队已存在!')
    return success_api('添加成功')

@user_opt.route('/login',methods=['POST'])
# 获取登录请求及处理
def login_post():
    username = request.get_json().get('username')
    password = request.get_json().get('password')
    user.username = username
    user.password = password
    print('收到一个登录请求')
    try:
        db = connect_database()
        # token = user.create_token()
        query = db.execute(f"SELECT band_id FROM bands WHERE band_id = '{username}'").fetchone()
        if query is not None:
            role = 'band'
            user.role = role
            band_name = db.execute(f"SELECT bname FROM bands WHERE band_id = '{username}'").fetchone()[0]
            connect_database(username,password)
            return success_api('登录成功!',data={"role":role,"bandName":band_name})
        elif username == 'admin':
            role = 'admin'
            user.role = role
            connect_database()
            return success_api('登录成功!', data={"role": role})
        else:
            connect_database(username,password)
            role = 'fan'
            user.role = role
            return success_api('登录成功!',data={"role":role})
    except Exception as e:
        print(e)
        return fail_api('账号或密码错误!')


@user_opt.route('/verify',methods=['POST'])
def check_login():
    token = request.get_json().get('accessToken')
    username = user.verify_token(token)
    if not username:
        return fail_api('token无效!')
    return success_api('token认证成功!',username)

@user_opt.route('/logout',methods=['POST'])
def logout():
    # g.user = None
    # token = request.get_json().get('accessToken')
    # username = user.verify_token(token)
    if user.username is None:
        return fail_api('已经退出登录了!')
    else:
        user.username = None
        return success_api('成功退出登录!')



# @auth.error_handler
# def unauthorized():
#     return fail_api('未授权!')