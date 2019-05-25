def main():
    str = "hello, world!"
    print(len(str))
    print(str.capitalize())

    print(str.upper())

    print(str.find('or'))

    print(str.find('shit'))

    print(str.index('or'))
    # print(str.index('shit'))

    print(str.startswith('he'))
    print(str.startswith('He'))

    print(str.endswith('ld!'))

    print(str.center(50, '*'))

    print(str.rjust(50, ' '))

    str2 = 'abc123456'

    print(str2[2])

    print(str2[2:5])

    print(str2[2:])

    print(str2[2::2])

    print(str2[::2])

    print(str2[::-1])

    print(str2[-3:-1])

    print(str.isdigit())

    print(str.isalpha())

    print(str2.isalnum())

    str3 = '   jackfrued@126.com '
    print(str3)
    print(str3.strip())


if __name__ == "__main__":
    main()
