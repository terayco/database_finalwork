from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from flask_cors import CORS
from applications.init_user import create_user
from applications.api.user import user_opt
from applications.api.get_info import info_opt
from applications.api.band import band_opt
from applications.api.album import album_opt
from applications.api.song import song_opt
from applications.api.perform import perform_opt
from applications.api.fan import fan_opt
from applications.api.aboutMe import aboutMe_opt
from applications.api.search import search_opt


#创建测试用的fan和band用户
create_user()
#创建app对象
app  = Flask(__name__)
# 设置跨域
CORS(app, resources=r'/*', supports_credentials=True)
#设置路由

app.register_blueprint(user_opt)
app.register_blueprint(info_opt)
app.register_blueprint(band_opt)
app.register_blueprint(album_opt)
app.register_blueprint(song_opt)
app.register_blueprint(perform_opt)
app.register_blueprint(fan_opt)
app.register_blueprint(aboutMe_opt)
app.register_blueprint(search_opt)
#启用调试模式
app.debug=True
#配置秘钥和json解码方式，秘钥随便输入什么都行
app.config['SECRET_KEY'] = 'hmhn'
app.config['JSON_AS_ASCII'] = False


if __name__ == '__main__':
    app.run(port=4000)