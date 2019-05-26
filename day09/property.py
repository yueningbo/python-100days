class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    # @property可以把方法变成属性
    @property
    def name(self):
        return self._name

    # 访问器
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法（可以检查修改数据）
    # @age.setter把setter方法变成属性赋值
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    print(person.name)
    person.age = 22
    person.play()


if __name__ == '__main__':
    main()
