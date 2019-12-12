from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from   config import config_map,Dev,Product
import redis
from flask_session import Session
from flask_wtf import  CSRFProtect


#工厂模式
#数据库方式1 创建db
# db=SQLAlchemy(app)
#数据库2创建db
db=SQLAlchemy()
redis_store=None
def create_app(config_name):
    '''
    根据具体config 返回具体的app
    :param config_name:str 配置参数的名字 （"dev " or "pro"）这个是开发 还是生产
    :return: 返回是生产环境的app 还是开发的app
    '''
    '''专门用来创建一个app'''
    app = Flask(__name__)
    assert config_name in config_map
    config_class=config_map[config_name]
    app.config.from_object(config_class)
    # 创建redis对象
    global  redis_store
    redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)
    db.init_app(app)
    # 为flask 补充csrf防护
    CSRFProtect(app)
    # 利用session将session保留到redis
    Session(app)
    from  ihome import api_v1_0
    app.register_blueprint(api_v1_0.api,url_prefix="/api/v1.0")
    return app