'''
三种员工：
部门经理: 15000
程序员: 150 * 工作时间
销售员: 1200 + 销售额 * 5 %
'''
from abc import abstractmethod, ABCMeta

class Employee(object, metaclass=ABCMeta):
    '''员工'''

    def __init__(self, name):
        '''初始化'''
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        '''
        获得月薪
        :return: 月薪
        '''
        pass


class Manager(Employee):
    '''部门经理'''

    def get_salary(self):
        return 15000.0

class Programmer(Employee):
    '''程序员'''
    def __init__(self, name, work_hour=0):
        super().__init__(name)
        self._work_hour = work_hour

    @property
    def work_hour(self):
        return self._work_hour

    @work_hour.setter
    def work_hour(self, work_hour):
        self._work_hour = work_hour if work_hour > 0 else 0

    def get_salary(self):
        return 150 * self._work_hour


class Salesman(Employee):
    '''销售员'''

    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200 + self._sales * 0.05


def main():
    emps = [
        Manager('刘备'), Programmer('诸葛亮'),
        Manager('曹操'), Salesman('荀彧'),
        Salesman('吕布'), Programmer('张辽'),
        Programmer('赵云')
    ]

    for emp in emps:
        if isinstance(emp, Programmer):
            emp.work_hour = int(input('请输入%s本月工作时间: ' % emp.name))
        elif isinstance(emp, Salesman):
            emp.sales = float(input('请输入本月%s销售额: ' % emp.name))
        print('%s本月工资为: ￥%s元' % (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()
