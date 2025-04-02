def change_all_methods(cls):
    def wapper():
        for name, method in vars(cls).items():
            if callable(method):
                def change(method):
                    print("before ",method)
                    method()
                    print("after ", method)
                setattr(cls,name,change(method))
        return cls
    return wapper

@change_all_methods
class Test():
    def __init__(self):
        pass

    def api(self):
        print("API")
    
    def api1(self):
        print("API1")

if __name__ == "__main__":
    t= Test()
    t.api()
    t.api1()


