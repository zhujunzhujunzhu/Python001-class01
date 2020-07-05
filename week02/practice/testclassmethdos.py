'''
@Description 
@Autor 朱俊
@Date 2020-07-05 11:05:48
@LastEditors 朱俊
@LastEditTime 2020-07-05 11:48:15
'''
'''
这里我看到了u 此前还看到了f  r
目前我只对于f 格式化是很清晰的
u 是进行unicode的编码的  如果不使用的话 可能中文就是乱码的
r 是关于一些转译字符的正常的输出
'''


class A(object):
    def foo(self, x):
        print(u"A类下函数foo的参数：", x)

    @classmethod  # 类方法
    def class_foo(cls, x):
        print(u"A类下函数class_foo的参数：", x)

    @staticmethod
    def static_method(x):
        print(u"A类下函数static_foo的参数：", x)


# print(r"input\ninput")
# print("input\ninput")
# # 目前在这里似乎是没有差别的
# print(u"关于u的测试")
# print("关于u的测试")
# a = A()
# a.foo("w")
# a.class_foo("e")
# a.static_method("r")

# # A.foo("t")报错
# A.static_method("Y")
# A.class_foo("U")
# 这里其实我想测试的是调用了类方法后 再进入初始化的方法是不是将类方法的结果就抛给了__init__


class B:
    def __init__(self, name):
        print(name)

    @classmethod
    def create_name(cls, name):
        return name

    @classmethod
    def test_name(cls, name):
        return cls(name)


# b = B('test1')

# # 调用类方法会触发类的初始化吗  应该不会的
# name = B.create_name('classmethods test')
# # 下面的却因为缺少参数没有办法运行的
# # 并不是所谓的自动进行的
# B(name)


# 那么现在看 from_setting  from_scrawl 这些类方法 关于调用肯定是已经 固定好的
# 现在的问题是  如果没有写这个类方法 就不让它执行
# 如何在python中判断有类中有没有相应的方法？  hasattr   dir

# print(hasattr(B, "create_name"))
# # 关于内置的属性或者方法也是可以判断出的
# print(hasattr(B, "__init__"))
# print(dir(B))

# if hasattr(B, "create_name"):
#     name1 = B.create_name("hello world")
#     B(name1)


# 可以进一步去看下  from_setting from_scrawl

# 会发现其实是有一个cls 代表类本身 可以在类方法中直接进行类的实例化的

B.test_name('你好  世界')
