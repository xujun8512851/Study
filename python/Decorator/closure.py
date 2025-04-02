"""
	• 闭包：一个内嵌函数引用外部函数作用域的变量，并且返回或者存储了内嵌函数，那么就形成了一个闭包
		○ 保持状态：闭包可以记住它被创建时的环境，即使外部函数已经执行完了。这个状态被记录在__closure__里
		○ 闭包可以实现类似面向对象中的数据封装，有助于隐藏细节，提高代码的模快性和可重用性
        ○ 延迟计算，可以用于延迟计算
"""
def extend_method(x):
    z = x +1
    def inter_method(y):
        nonlocal x
        x = x + y + z
        print(x)
        
    return inter_method

def extend_method_test():
    c =  extend_method(4)
    d = extend_method
    c(5)
    for item in c.__closure__:
        print(item.cell_contents)
    c(10)
    for item in c.__closure__:
        print(item.cell_contents)
    print(d.__closure__)

#循环闭包的陷阱和变量绑定时机问题

def create_func():
    funcs = list()
    
    for i in range(3):
        def func():
            return i
        funcs.append(func)
    return funcs

f1, f2, f3 = create_func()
print(f1(),f2(),f3())
