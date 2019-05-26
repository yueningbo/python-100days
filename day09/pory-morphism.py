from abc import ABCMeta, abstractmethod


# 抽象类，专门用于被继承，不能创建对象
class Pet(object, metaclass=ABCMeta):
    '''宠物'''

    def __init__(self, nickname):
        self._nickname = nickname

    #@abstractmethod,将一个方法包装成抽象方法，需要被具体实现才能调用
    @abstractmethod
    def make_voice(self):
        '''发出声音'''
        pass


class Dog(Pet):
    '''狗'''

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    '''猫'''

    def make_voice(self):
        print('%s: 喵喵喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('来福')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()
