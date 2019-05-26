from abc import ABCMeta, abstractmethod
from random import randint, randrange
import time


class Fighter(object, metaclass=ABCMeta):
    '''战斗者'''

    #通过__slots__限定对象可以绑定的成员变量
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        '''
        初始化
        :param name: 名称
        :param hp: 生命值
        '''
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        '''
        攻击
        :param other:被攻击的对象
        '''
        pass


class Ultarman(Fighter):
    '''奥特曼'''

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        '''
        究极必杀技
        :param other:被攻击对象
        :return: 成功返回True，否则False
        '''
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        '''
        魔法攻击
        :param self:
        :param others:被攻击的群体
        :return: 成功则返回True
        '''
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        '''回复魔法值'''
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
               '生命值: %d\n' % self._hp + \
               '魔法值: %d\n' % self._mp


class Monster(Fighter):
    '''小怪兽'''

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
               '生命值: %d\n' % self._hp


def is_any_alive(monsters):
    '''判断有没有活的小怪兽'''
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_alive_one(mosters):
    '''选择一只活的小怪兽'''
    mosters_len = len(mosters)
    while True:
        index = randrange(mosters_len)
        monster = mosters[index]
        if monster.alive > 0:
            return monster

def display_info(utm, monsters):
    '''显示奥特曼和小怪兽的情况'''
    print(utm)
    for monster in monsters:
        print(monster)


def main():
    utm = Ultarman('Pao', 1000, 120)
    m1 = Monster('小肥肉', 250)
    m2 = Monster('大肥肉', 500)
    m3 = Monster('超级肥肉', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while utm.alive and is_any_alive(ms):
        print('============第%02d回合============' % fight_round)
        m = select_alive_one(ms) # 选中一只小怪兽
        skill = randint(1, 10) # 通过随机数选择一种技能
        if skill <= 6: # 60%几率使用普通攻击
            print('%s使用了普通攻击击打了%s.' % (utm.name, m.name))
            utm.attack(m)
            print('%s的魔法值回复了%d点.' % (utm.name, utm.resume()))
        elif skill < 9: # 30%几率使用魔法攻击
            if utm.magic_attack(ms):
                print('%s使用了魔法攻击.' % utm.name)
            else:
                print('%s使用魔法攻击失败.' % utm.name)
        else:
            if utm.huge_attack(m):
                print('%s使用究极必杀技暴打%s.' % (utm.name, m.name))
            else:
                print('%s使用普通攻击击打了%s.' % (utm.name, m.name))
                print('%s的魔法值恢复了%d点' % (utm.name, utm.resume()))
        if m.alive > 0:# 小怪兽没死就回击奥特曼
            print('%s回击了%s.' % (m.name, utm.name))
            m.attack(utm)
        display_info(utm, ms) #每回合显示双方情况
        fight_round += 1
        time.sleep(5)

    print('\n============战斗结束============')
    if utm.alive:
        print('%s奥特曼胜利！' % utm.name)
    else:
        print('小怪兽胜利')

if __name__ == '__main__':
    main()
