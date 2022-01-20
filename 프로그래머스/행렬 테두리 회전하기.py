def solution(rows, columns, queries):
    matrix = [list(range(i, i + rows)) for i in range(1, rows * rows + 1, rows)]
    result = []
    # for query in queries:
    #     x1, y1, x2, y2 = map(lambda x: x-1, query)
    #         rotate_num = matrix[x1][y1:y2+1]
    #         for x in range(x1+1, x2+1):
    #             rotate_num.append(matrix[x][y2])
    #         rotate_num.extend(matrix[x2][y1:y2+1])
    #         for x in range(x1+2, x2+1):
    #             rotate_num.append(matrix[x][y1])
    #         rotate_num.insert(0, matrix[x1+1][y1])
    #         print(rotate_num)

    #         result.append(min(rotate_num))
    #         matrix[x1][y1:y2+1] = rotate_num[:x2-x1]
    #         p = x2-x1
    # for x in range(x1+1, x2+1):
    #     matrix[x][y2] = rotate_num[p]
    #     p += 1
    # matrix[x2][y1:y2+1] = rotate_num[p:p+x2-x1]
    # p = p+x2-x1
    # for x in range(x1+1, x2+1):
    #     matrix[x][y1] = rotate_num[p]
    #     p += 1
    # print(matrix)
    #         xl = x2-x1+1
    #         yl = y2-y1+1
    #         rotate_num = [0 for _ in range(xl * yl)]
    #         rotate_num[1:xl-1] = matrix[x1][y1:y2+1]
    #         rotate_num[xl+y1+2:2*xl+y1] = matrix[x2][y1:y2+1]
    #         print(rotate_num)
    #         i = xl+1
    #         for x in range(x1+1, x2+1):
    #             rotate_num[i] = matrix[x][y2]
    #             rotate_num[i+xl] = matrix[x2-x][y2]

    #         print(rotate_num)

    for query in queries:
        x1, y1, x2, y2 = map(lambda x: x - 1, query)
        min_num = 1e9
        move = matrix[x1][y1]
        for y in range(y1 + 1, y2 + 1):
            min_num = min(min_num, move)
            tmp = matrix[x1][y]
            matrix[x1][y] = move
            move = tmp

        for x in range(x1 + 1, x2 + 1):
            min_num = min(min_num, move)
            tmp = matrix[x][y2]
            matrix[x][y2] = move
            move = tmp
        print(matrix)
        for y in range(y2 - 1, y1 - 1, -1):
            min_num = min(min_num, move)
            tmp = matrix[x2][y]
            matrix[x2][y] = move
            move = tmp
        print(matrix)
        for x in range(x2, x1 - 1, -1):
            min_num = min(min_num, move)
            tmp = matrix[x][y2]
            matrix[x][y2] = move
            move = tmp
        print(matrix)
        matrix[x1][y1] = move
        min_num = min(min_num, move)
        print(matrix)
        print(min_num)
        result.append(min_num)

    return result