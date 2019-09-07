'''
创建工具检查缓存，为抢购实现提供函数方法，
数据在redis中以哈希数据的形式存在，每一次抢购回给该商品抢购的用户列表添加一个用户，
判断该数据的长度来限制抢购数量
'''
# 程序现阶段模拟一种商品抢购，完善应该为每一种被抢购的商品一旦被抢购设定
# BUG点每个用户只能抢一件商品，并且抢不同的商品会覆盖以前抢到的商品，总长度不变。


from . import rd_client
QBUY_KEY = 'qbuy_active'  # hash

# 判断该商品是否已经被抢购完
def is_qbuyble():
    return rd_client.hlen(QBUY_KEY) < 5

# 验证用户是否已抢购，查看缓存中的是否有该用户的id存在
def exist_qbuy(user_id):
    return rd_client.hexists(QBUY_KEY, user_id)

# 如果可以抢购将该商品的存入缓存
def add_qbuy(user_id, goods_id):
    rd_client.hset(QBUY_KEY, user_id, goods_id)

# 获取该用户抢到的商品，
def get_qbuy(user_id):
    return rd_client.hget(QBUY_KEY, user_id)