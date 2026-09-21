#1 = wall, parede
#0 espaço, space
import random
matrix = [[0 for i in range(10)] for j in range(10)]
def parede(matrixes, i, j):
    matrixes[i][j] = 1
def espaço(matrixes, n, m):
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if random.random() < 0.9:
                parede(matrixes, i, j)
def criar(matrixes):
    for i in range(len(matrixes)):
        for j in range(len(matrixes[0])):
            if matrixes[i][j] == 1:
                print(matrixes[i][j], end= " ")
            else:
                print(matrixes[i][j], end= " ")

criar(matrix)
espaço(matrix, len(matrix), len(matrix[0]))
criar(matrix)
