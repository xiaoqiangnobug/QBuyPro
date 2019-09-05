from redis import Redis

config = {
    'host': 'xm.imzhangao.com',
    'port': 6379,
    'db': '9',
    'decode_responses': True
}

rd_client = Redis(**config)
