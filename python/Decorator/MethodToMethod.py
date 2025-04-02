def decorator_func(func):
    """
    func函数会被调用两次， 所以如果只是想在函数前 添加下行为， 可以使用 单个方法实现装饰器
    """
    print("before func")
    func()
    print("after func")

    return func

def decorator_funct(func):
    """
    装饰器如果用单一函数实现，会导致初始化调用装饰器的函数的时候就会执行， 所以需要用内嵌函数来实现
    """
    def wapper():
        print("before decorator_func1")
        func()
        print("after decorator_func1")
    
    return wapper

def decorator_funct1(func):
    """
    装饰器如果用单一函数实现，会导致初始化调用装饰器的函数的时候就会执行， 所以需要用内嵌函数来实现
    """
    def wapper(*args, **kwargs):
        print("before decorator_func1")
        func(*args, **kwargs)
        print("after decorator_func1")
    
    return wapper

def decorator_funct2(str):
    """
    装饰器的第一层函数用来接受， 引用装饰器时的参数
    第二层函数用来接受 引用装饰器的函数方法名
    第三层函数用来接受引用装饰器的函数方法的参数
    """
    print(str)
    def test(func):
        """
        装饰器如果用单一函数实现，会导致初始化调用装饰器的函数的时候就会执行， 所以需要用内嵌函数来实现
        """
        def wapper(*args, **kwargs):
            print("before decorator_func3")
            func(*args, **kwargs)
            print("after decorator_func3")
        
        return wapper
  
    return test

@decorator_func
def test_decorator_func():
    print("test_decorator_func")

@decorator_funct
def test_decorator_func1():
    print("test_decorator_func1")

@decorator_funct1
def test_decorator_func2(str):
    print("test_decorator_func1")

@decorator_funct2("jun")
def test_decorator_func3(str):
    print("test_decorator_func3")

if __name__ == "__main__":
    test_decorator_func3("1")