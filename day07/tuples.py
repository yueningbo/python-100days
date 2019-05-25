import sys

def main():
    t = ('pao', 25, True, '湖南')
    print(t)
    print(t[0])

    for i in t:
        print(i)

    t = ('dachui', 20, True, 'kupsl')
    print(t)

    person = list(t)

    person[0] = 'lixiaolong'

    tuple_1 = tuple(person)

    print(person)
    print(tuple_1)

    print(sys.getsizeof(person))
    print(sys.getsizeof(tuple_1))


if __name__ == '__main__':
    main()
