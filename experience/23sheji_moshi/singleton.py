# -*-coding:utf-8-*-
# 单例模式


# 使用__metaclass__（元类）的高级python用法,此方法只在Python2中有效,Python3中无效
class Singleton2(type):
    def __init__(cls, name, bases, dict):
        super(Singleton2, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton2, cls).__call__(*args, **kw)
        return cls._instance


class MyClass3(object):
    __metaclass__ = Singleton2


# 使用装饰器(decorator),
# 这是一种更pythonic,更elegant的方法,
# 单例类本身根本不知道自己是单例的,因为他本身(自己的代码)并不是单例的
def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class MyClass4(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


if __name__ == '__main__':
    one3 = MyClass3()
    two3 = MyClass3()

    one4 = MyClass4()
    two4 = MyClass4()

    print(one3 == two3)
    print(one4 == two4)

    two4.a = 3
    print(one4.a)
