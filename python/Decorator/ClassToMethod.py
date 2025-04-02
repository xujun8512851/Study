"""
总结：类装饰器主要是通过__call__实现的
    1. __init__ 用来接受第一个参数， __call__ 函数用来接收第二个参数，如果需要第三个函数，则需要在__call__里创建一个内置函数接收
    2. 三个参数顺序， 装饰器参数-> 被装饰的对象name -> 被装饰对象的参数
    3. __int__在装饰时执行，即在初始化的时候执行，__call__ 在调用被装饰的对象的时候执行
"""
class func:
    def __init__(self,func):
        self.func = func


    def __call__(self, *args, **kwargs):
        print("before func")
        self.func(*args, **kwargs)
        print("after func")  
        
class func1:
    def __init__(self, *args, **kwargs):
        if len(args)==1 and callable(args[0]):
            self.name = args[0]
            self.flag = False
        else:
            self.flag = True
            self.args = args
            self.kwargs = kwargs



    def __call__(self, *args1):
        if self.flag:
            self.name = args1[0]
        def wapper(*args, **kwargs):
            print("before func")
            self.name(*args, **kwargs)
            print("after func")
        return wapper
       
@func1()
def test():
    print("This is a test")

@func1("jun")
def test1():
    print("This is a test")

@func1()
class Test:
    def __init__(self):
        pass
    
    def value(self):
        print("Test")

@func1("Jun")
class Test1:
    def __init__(self):
        pass
    
    def value(self):
        print("Test1")
if __name__ == "__main__":
    test = Test1()
    test = Test()
