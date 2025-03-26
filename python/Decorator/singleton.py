"""
利用装饰器实现单例模式
"""
from threading import Lock

def singleton(cls):
    instances = {}

    def wapper(*args, **kgargs):

        if cls not in instances:
            instances[cls] = cls(*args, **kgargs)
        
        return instances[cls]

    return wapper

def singleton1(cls):
    """
    利用线程锁 + 双重检查来实现线程安全的单例模式
    """
    instances = {}
    lock = Lock()

    def wapper(*args, **kgargs):

        if cls not in instances:
            with lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kgargs)
        
        return instances[cls]

    return wapper

@singleton
class Test:
    def __init__(self):
        print("init")


if __name__ == "__main__":
    test1 = Test()
    test2 = Test()
    print(id(test1), id(test2))