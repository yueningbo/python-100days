def main():
    list1 = ['orange', 'apple', 'appll', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    print(list2)

    list3 = sorted(list1, reverse=True)

    list4 = sorted(list1, key=len)

    print(list3)
    print(list4)


if __name__ == '__main__':
    main()
