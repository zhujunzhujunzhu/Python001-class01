
import abc


class Animal(metaclass=abc.ABCMeta):
    def __init__(self, type, shape, nature):
        self.type = type
        self.shape = shape
        self.nature = nature


class Cat(Animal):
    def __init__(self, name, shape, nature, shout):
        super().__init__('Cat', shape, nature)
        self.name = name
        # 是否适合做宠物
        self.is_suit_pet = True


class Zoo(object):
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    # 使用__getattr__ 拦截不存在的属性
    def __getattr__(self, type):
        flag = False
        for aniaml in self.animals:
            if aniaml.type == type:
                flag = True
                break

        return flag


if __name__ == '__main__':
    # a = Animal(1, 2, 3)
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
    print(have_cat)
