def main():
    set1 = {1, 2, 2, 3, 3, 2}
    print(set1)
    print('Lenth = ', len(set1))
    set2 = set(range(10))
    print(set2)
    set1.add(4)
    set1.add(5)
    set2.update([11, 12])
    print(set1)
    print(set2)
    set2.discard(5)
    print(set2)

    if 4 in set2:
        set2.remove(4)
    print('set2 = ', set2)

    for elem in set2:
        print(elem ** 2, end=' ')
    print()

    set3 = set((1, 1, 2, 3, 3, 2))
    print(set3.pop())
    print(set3.pop())
    print(set3)

    print('set1 = ', set1)
    print('set2 = ', set2)
    print('set1 & set2 = ', set1 & set2) # 交集
    print('set1 | set2 = ', set1 | set2) # 并集
    print('set1 - set2 = ', set1 - set2) # 差集
    print('set1 ^ set2 = ', set1 ^ set2)  # 对称差

    print("set2 <= set1:", set2 <= set1)
    print("set2.issubset(set1):", set2.issubset(set1))
    print("set3 <= set1:", set3 <= set1)
    print("set3.issubset(set1):", set3.issubset(set1))
    print("set1 <= set2:", set1 <= set2)
    print("set1.issubset(set2):", set1.issubset(set2))
    print("set1 <= set3:", set1 <= set3)
    print("set1.issubset(set3):", set1.issubset(set3))


if __name__ == '__main__':
    main()
