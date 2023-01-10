from flask import Blueprint
from flask import request
from utils.http import success_api, fail_api
from applications.database import connect_database
from utils.create_user import user

fan_opt = Blueprint('fan_opt', __name__, url_prefix='/api/fan')


@fan_opt.route('/addFan',methods=['POST'])
def add_fan():
    password = request.get_json().get('password')
    fan_id = request.get_json().get('fanId')
    fname = request.get_json().get('fanName')
    sex = request.get_json().get('fanSex')
    career = request.get_json().get('fanCareer')
    age = request.get_json().get('fanAge')
    try:
        db = connect_database()
        db.execute(f'''
            CREATE USER'{fan_id}'@'localhost' IDENTIFIED BY '{password}'
                    ''')
        db.execute(f'''
                    INSERT INTO fans(fan_id,fname,sex,age,occupation)
                    VALUES('{fan_id}','{fname}','{sex}',{age},'{career}')
                    ''')
    except Exception as e:
        print(e)
        return fail_api('添加失败，该用户id已存在!')
    return success_api('添加成功')

@fan_opt.route('/editFan',methods=['PUT'])
def edit_fan():
    fan_id = request.get_json().get('fanId')
    fname = request.get_json().get('fanName')
    sex = request.get_json().get('fanSex')
    career = request.get_json().get('fanCareer')
    age = request.get_json().get('fanAge')
    db = connect_database()
    db.execute(f'''
               UPDATE fans
               SET fname='{fname}',sex='{sex}',occupation='{career}',age={age}
               WHERE fan_id='{fan_id}'
                ''')
    return success_api('修改成功')

@fan_opt.route('/deleteFan',methods=['DELETE'])
def delete_fan():
    fan_id = request.get_json().get('fanId')
    db = connect_database()
    try:
        db.execute(f'''
                    DELETE 
                    FROM fans
                    WHERE fan_id='{fan_id}'
                    ''')
        db.execute(f'''
                    DROP USER'{fan_id}'@'localhost'
                    ''')
    except Exception as e:
        print(e)
        return fail_api('删除失败，该用户不存在!')
    return success_api('删除成功')