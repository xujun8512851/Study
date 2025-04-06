"""
mode 有 r， w， a， x。 
+ 表示读写模式，在对文件需要读和写的时候使用
w 模式会删除文件的原内容在写入
x 表示只有在文件不在的时候会创建文件，如果文件在的时候会报错。 这是与w模式的主要区别
"""

with open('test2.txt','x+') as f:
    print(f.readline())
    print(f.write("aThis is a testing"))
