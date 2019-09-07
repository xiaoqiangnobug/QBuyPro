# 配置数据库， 将数据存入redis数据库
from redis import Redis

config = {
    'host': 'xm.imzhangao.com',
    'port': 6379,
    'db': '27',
    'decode_responses': True
}

rd_client = Redis(**config)
