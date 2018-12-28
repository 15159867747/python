import redis
from proxypool.error import PoolEmptyError
from proxypool.setting import HOST, PORT, PASSWORD


class RedisClient(object):
    def __init__(self, host=HOST, port=PORT):
        if PASSWORD:
            self._db = redis.Redis(host=host, port=port, password=PASSWORD)
        else:
            self._db = redis.Redis(host=host, port=port)

    def get(self, count=1):
        """
        get proxies from redis
        """
        proxies = self._db.lrange("proxies", 0, count - 1)#从队列左侧拿出多少个内容并返回出来
        self._db.ltrim("proxies", count, -1)#把时间久的代理拿出来放到左侧，新的代理放到右侧
        return proxies

    def put(self, proxy):
        """
        add proxy to right top
        """
        self._db.rpush("proxies", proxy)#将检测完可用的代理插入到队列的右侧

    def pop(self):
        """
        get proxy from right.
        """
        try:
            return self._db.rpop("proxies").decode('utf-8')#从队列右边拿出可用代理
        except:
            raise PoolEmptyError

    @property
    def queue_len(self): #获取队列长度
        """
        get length from queue.
        """
        return self._db.llen("proxies")

    def flush(self):#刷新代理
        """
        flush db
        """
        self._db.flushall()


if __name__ == '__main__':
    conn = RedisClient()
    print(conn.pop())
