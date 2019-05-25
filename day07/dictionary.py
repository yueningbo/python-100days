import sys


def main():
    scores = {'Pazo': 100, 'Dafeirou': 99, 'lurenwang': 78}
    print(scores['Pazo'])
    print(scores['Dafeirou'])

    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))

    scores['luvu'] = 65
    scores['zhugewanglang'] = 71
    scores.update(feizai=55, rourou=22)
    print(scores)
    if 'wuzetian' in scores:
        print(scores['wuzetian'])
    print(scores.get('wuzetian'))
    print(scores.get('wuzetian', 66))
    print(scores)
    print(scores.popitem())
    print(scores.pop('Pazo', 100))
    scores.clear()
    print(scores)


if __name__ == '__main__':
    main()
