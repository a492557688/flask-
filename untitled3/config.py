import  redis

class  Config(object):
    SECRET_KEY='XZQ'
    #数据库配置
    SQLALCHEMY_DATABASE_URL='mysql://root:a13736784065@127.0.0.1:3306/test'
    SQLALCHEMY_TRACK_MODIFCATIONS=True
    #redis
    REDIS_HOST='127.0.0.1'
    REDIS_PORT=6379
    #flask_session配置
    SESSION_TYPE='redis'
    SESSION_REDIS=redis.StrictRedis(REDIS_HOST,port=REDIS_PORT) #必须是redis实例
    SESSION_USE_SIGNER=True #对cookie中的session进行隐藏
    PERMANENT_SESSION_FILETIME=3600*24#session数据有效期 单位秒


class Dev(Config):
    #开发环境
    DEBUG=True

class  Product(Config):
    #生产环境配置信息
    pass

config_map={
    "dev":Dev,
    "product":Product,
}