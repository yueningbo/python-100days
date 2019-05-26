class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    def watch_av(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情动作片.' % self.name)

def main():
    # 创建学生并指定名字
    stu1 = Student("Pao", 25)
    # 学习
    stu1.study('Python程序设计')
    stu1.watch_av()
    stu2 = Student("rourou", 16)
    stu2.study("思想品德")
    stu2.watch_av()


if __name__ == '__main__':
    main()

