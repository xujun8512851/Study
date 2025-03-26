
"""
Python 垃圾回收机制主要有三种方式：引用计数、标记清除、分代回收。
a. 引用计数：Python 中每个对象都有一个引用计数，用来记录有多少引用指向该对象。当引用计数为 0 时，对象被删除。
b. 标记清除：Python 通过标记清除来回收内存。标记清除分为两个阶段：标记阶段和清除阶段。标记阶段遍历所有对象，标记活着的对象。清除阶段遍历所有对象，清除没有标记的对象。
    b1. 主要针对于循环引用的情况。
    b2. 会遍历整个内存空间，效率较低。所以有了 分代回收。
c. 分代回收：Python 通过分代回收来回收内存。Python 将对象分为三代, 每代对象存活时间越长, 回收概率越低。Python 通过检查每代对象的引用计数来回收内存。
"""
import sys
import gc

def reference_count():
    a = 1
    b = a
    print("a的引用计数：", sys.getrefcount(a))
    print("b的引用计数：", sys.getrefcount(b))
    del b
    print("a的引用计数：", sys.getrefcount(a))
    del a

def make_clean():
    print(gc.get_count())
    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]
    lst1.append(lst2)
    lst2.append(lst1)
    del lst1
    del lst2
    print(gc.get_count())
    gc.collect()
    print(gc.get_count())

if __name__ == "__main__":
    reference_count()
    make_clean()