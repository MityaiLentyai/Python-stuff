def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    ret = [[]]
    for row in matrix:
        ret.append(row[::-1])

    return ret[1:]

print(mirror_matrix([[-1,-2],[-3,-4]]))
