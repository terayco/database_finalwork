from itsdangerous import Serializer
from flask import current_app

class User():
    def __init__(self, username, password):
        self.password = password
        self.username = username
        self.token = ''

    def create_token(self):
        '''
        生成token
        :param api_user:用户id
        :return: token
        '''
        # api_user = self.username
        # 第一个参数是内部的私钥，这里写在共用的配置信息里了
        # 第二个参数是有效期(秒)
        s = Serializer(current_app.config["SECRET_KEY"], expires_in=3600)
        # 接收用户id转换与编码
        token = s.dumps({"id": self.username}).decode("ascii")
        return token

    def verify_token(self, token):
        '''
        :param token:
        :return: user_id or None
        '''
        # 参数为私有秘钥，跟上面方法的秘钥保持一致
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            # 转换为字典
            data = s.loads(token)
        except Exception:
            return None

        user_id = data.get("id")
        return user_id

#初始化用户对象
user = User('hanxixi','123456')