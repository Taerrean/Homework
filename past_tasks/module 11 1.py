import numpy as np


a = np.array([
    [4., 3., 2., 7.],
    [6., 4., 1., 3.],
    [9., 3., 5., 2.]
])

b = np.array([
    [6., 3., 5.],
    [4., 8., 1.],
    [7., 3., 5.],
    [5., 7., 1.]
])

c = np.array([
    [4., 3., 2., 7.],
    [6., 4., 1., 3.],
    [4., 8., 1., 8.],
    [9., 3., 5., 2.]
])

print(f'View of the transposed array a:\n{a.T}\n')
print(f'Array b reshaped to (2, 6):\n{b.reshape(2, 6)}\n')

print(f'Dot product of a * b:\n{a @ b}\n')
print(f'Dot product of b * a:\n{b.dot(a)}\n')

print(f'Transform elements of a to int:\n{a.astype(int)}\n')
print(f'Transform elements of b to str:\n{b.astype(str)}\n')

eig_val, eig_vectors = np.linalg.eig(c)
print(f'Eigenvalues of a square array c:\n{eig_val}\n')
print(f'Eigenvectors of a square array c:\n{eig_vectors}\n')

print(f'The determinant of an array c:\n{np.linalg.det(c)}\n')

d = np.array([5., 2., 9., 1])
print(f'Solution of linear matrix equation cx = d:\n{np.linalg.solve(c, d)}\n')

print(range(1, 10, 2))  # Для сравнения с np.arange()
print(np.arange(1, 10, 2))
print(np.linspace(1, 10, 5))