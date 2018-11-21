import numpy as np

def enumeration(matrix):
    print("\nЭффективные по Парето:", end=' ')
    for row in matrix:
            for elem in row:
                if Pareto(matrix, elem):
                    print(elem, end=' ')
    print("\nУстойчивые по Нэшу:", end=' ')
    for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if Nash(matrix, i, j):
                    print(matrix[i][j], end=' ')


def Pareto(matrix, strategy):
    for row in matrix:
        for elem in row:
            if strategy[0] < elem[0] and strategy[1] < elem[1]:
                return False
    return True

def Nash(matrix, i, j):
    for k in range(len(matrix)):
        if matrix[k][j][0] > matrix[i][j][0]:
            return False
    for k in range(len(matrix[0])):
        if matrix[i][k][1] > matrix[i][j][1]:
            return False
    return True

def printpretty(matrix):
    for row in matrix:
        for elem in row:
            print("({0: 3d}/{1: 3d})".format(elem[0], elem[1]) , end=' ')
        print()

prison = np.array([[[-1,-1], [-10,0]], 
                    [[0,-10], [-5,-5]]])

family = np.array([[[1,4], [0,0]], 
                    [[0,0], [4,1]]])

zadaca = np.array([[[0,1], [11,4]], 
                    [[7,8], [6,3]]])

zadacaA = np.array([[0,11],
                    [7,6]])

zadacaB = np.array([[1,4],
                    [8,3]])

np.set_printoptions(precision=3, linewidth=np.nan)
array = np.random.randint(-50, 50, size=(10, 10, 2))

print("Дилемма заключённого.")
printpretty(prison)
enumeration(prison)

print("\n\n\nСемейный спор.")
printpretty(family)
enumeration(family)

print("\n\n\nСлучайная матрица.")
printpretty(array)
enumeration(array)

print("\n\n\nВторая часть.")
printpretty(zadaca)
enumeration(zadaca)

u = np.array([1, 1])
# @ - оператор умножения матриц (работает в python 3.5 и выше)
x = u @ np.linalg.inv(zadacaB) / (u @ np.linalg.inv(zadacaB) @ u.transpose())
y = np.linalg.inv(zadacaA) @ u.transpose() / (u @ np.linalg.inv(zadacaA) @ u.transpose())
print("\n\nx={0} y={1}".format(x,y))
print("v1={0:.3f} v2={1:.3f}".format(1 / (u @ np.linalg.inv(zadacaA) @ u.transpose()),1 / (u @ np.linalg.inv(zadacaB) @ u.transpose())))