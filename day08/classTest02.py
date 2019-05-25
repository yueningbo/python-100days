class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test._Test__bar()
    # AttributeError: 'Test' object has no attribute '__foo'
    print(test._Test__foo)


if __name__ == '__main__':
    main()
