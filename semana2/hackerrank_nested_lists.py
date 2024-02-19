if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        l.append([name, score])

    #     second_lowest =
    l.sort(key=lambda elem: elem[1])
    lowest = l[0][1]

    for elem in l:
        if elem[1] != lowest:
            lowest = elem[1]
            break

    solution = []
    for elem in l:
        if elem[1] == lowest:
            solution.append(elem[0])

    solution.sort()

    for x in solution:
        print(x)