from . import rd_client
QBUY_KEY = 'qbuy_active'  # hash

def is_qbuyble():
    return rd_client.hdel(QBUY_KEY) < 5

def exist_qbuy(user_id):
    # 验证用户是否已抢购
    return rd_client.hexists(QBUY_KEY, user_id)

def add_qbuy(user_id, goods_id):
    rd_client.hset(QBUY_KEY, user_id, goods_id)

def get_qbuy(user_id):
    return rd_client.hget(QBUY_KEY, user_id)