def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix
n = int(input())
m = int(input())
value = int(input())
print(get_matrix(n,m,value))