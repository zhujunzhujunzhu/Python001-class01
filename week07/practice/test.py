class TypedProperty(object):

    #  __init__ 是进行初始化的  __new__ 它是构造方法   __new__在__init__ 之前执行  __new__

    def __init__(self, name, type, default=None):
        self.name = "_" + name
        self.type = type
        # 这种写法还是很少见的
        self.default = default if default else type()

    def __get__(self, instance, cls):
        print('__get__ 被执行了的')
        return getattr(instance, self.name, self.default)

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError("Must be a %s" % self.type)
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        raise AttributeError("Can't delete attribute")

    def __new__(cls, name, type, default=None):
        print(cls)
        c = object.__new__(cls)
        print(c)
        return c

    def __getattr__(self,  attr):
        print('__getattr__被执行了的')
        # if not isinstance()

    def __getattribute__(self,  attr):
        print('__getattribute__被执行了的')
        # return getattr(self, attr)
        return object.__getattribute__(self, attr)


# class Foo(object):
#     name = TypedProperty("name", str)
#     num = TypedProperty("num", int, 42)
'''
这里其实是比较好玩的现象的  __new__是构造方法 __init__是初始化方法    __new__比__init__要先执行  但是呢   传参呢是在__init__里面接收的 另一个需要注意的地方
__init__ 与__new__ 都是接收传入的参数的


关于__getattribute__与 __getattr__ 可以看到的是先进__getattribute是先被执行的
这个然后在里面使用 getattr的方式来取的话  会发现进入了死循环的

关于getattr 这个反射方法的使用的话 比点符号要强大的地方在于它是可以进行 取动态的属性的 或者说是 计算属性
关于python 中如何取字典中的动态属性的值 ？getattr
'''
testobj = TypedProperty("name", str)

# 这个是并没有触发__get__方法的
#
name = testobj.name
print(name)
name = getattr(testobj, 'name')
print(name)

# 现在想问的是 __get__ 这个重写的魔术方法什么时候被触发呢


# 关于多继承的问题

class Item1(object):
    def print_info(self, info):
        print('item1', info)


class Item2(object):
    def print_info(self, info):
        print('item1', info)


class Son(Item1, Item2):
    pass


son = Son()
son.print_info('你好')
# 这里会发现一个基本的现象是 对于多继承的话  如果是存在相同的方法的  使用调用顺序最靠前的父类的方法的
# 对类使用mro 方法可以判定一个继承的 方法调用的一个路径的  方法调用的优先级的
print(Son.mro())
