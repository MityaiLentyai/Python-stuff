def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    ret = matrix
    for row in matrix:
        ret.append(row[::-1])

print(mirror_matrix([[1,2,3],[4,5,6]]))
