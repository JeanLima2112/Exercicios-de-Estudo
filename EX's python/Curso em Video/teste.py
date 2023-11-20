def somamatriz(matrix):
    total = 0
    for c in range(len(matrix)):
        for i in matrix[c]:
            total += sum(matrix[c])
    return total


matrix = [[1,2,3,4,23,423],[12,321,3,1],[123,21,123,21,3],[12,3,12,312,3]]
#print(somamatriz(matrix))
print(somamatriz([[1,2],[2,4]]))