"""
元类是创建类的模版，就像类是创建实例的模版一样，type是所有类的默认元类。所有类的元类都可以通过查看__class__属性
使用场景：
    1. 需要控制类的创建过程
    2. 需要在类的创建过程中自动的修改或者验证类
    3. 实现框架级别的功能
    4. 需要注册所有子类或者实现插件系统
"""
from collections import OrderedDict

class MyMeta(type):
    # @classmethod
    # def __prepare__(cls, name , bases):
    #     print(f" Preparing namespace for {name}")
    #     return OrderedDict()
    
    def __new__(cls, name , bases, namespace):
        print(type(namespace))
        print(f"Creating class {name}")
        for key, value in namespace.items():
            print(f"{key} : {value}")
        return super().__new__(cls,name,bases,namespace)
    def __init__(cls, name ,bases,namespace):
        print(f"Initializing class {name}")
        super().__init__(name ,bases ,namespace)

class Test(metaclass=MyMeta):
    required_attr = 43
    def method(self):
        return "Hello"
    
    @property
    def property(self):
        return "property"

class TestA(Test):
    required_attr_a =44

t = TestA()