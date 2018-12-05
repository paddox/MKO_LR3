import numpy as np
from colorama import init, Fore, Back, Style
init()

def enumeration(matrix):
    #print("\nЭффективные по Парето:", end=' ')
    i = 0
    j = 0
    pareto = []
    nash = []
    for row in matrix:
        j = 0
        for elem in row:
            if Pareto(matrix, elem):
                #print(Fore.RED, elem, end=' ')
                #print(Style.RESET_ALL, end=' ')
                pareto.append((i, j))
            j += 1
        i += 1
    #print("\nУстойчивые по Нэшу:", end=' ')
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if Nash(matrix, i, j):
                #print(Fore.GREEN, matrix[i][j], end=' ')
                #print(Style.RESET_ALL, end=' ')
                nash.append((i, j))
    return (pareto, nash)


def Pareto(matrix, strategy):
    for row in matrix:
        for elem in row:
            if strategy[0] < elem[0] and strategy[1] <= elem[1]:
                return False
            if strategy[1] < elem[1] and strategy[0] <= elem[0]:
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

def printpretty(matrix, opt):
    i = 0
    j = 0
    pareto = opt[0]
    nash = opt[1]
    for row in matrix:
        j = 0
        for elem in row:
            if (i, j) in pareto and (i, j) in nash:
                print("{2}({0: 3d}/{1: 3d})".format(elem[0], elem[1], Fore.YELLOW) , end=' ')
                print(Style.RESET_ALL, end='')
            elif (i, j) in pareto:
                print("{2}({0: 3d}/{1: 3d})".format(elem[0], elem[1], Fore.RED) , end=' ')
                print(Style.RESET_ALL, end='')
            elif (i, j) in nash:
                print("{2}({0: 3d}/{1: 3d})".format(elem[0], elem[1], Fore.GREEN) , end=' ')
                print(Style.RESET_ALL, end='')
            else:
                print("({0: 3d}/{1: 3d})".format(elem[0], elem[1]) , end=' ')
            j += 1
        i += 1
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

most = np.array([[[2,2], [0,4]], 
                [[4,0], [-9,-9]]])

np.set_printoptions(precision=3, linewidth=np.nan)
array = np.random.randint(-50, 50, size=(10, 10, 2))

print("\nЭффективные по Парето выделены", Fore.RED, "красным", Style.RESET_ALL)
print("Устойчивые по Нэшу выделены", Fore.GREEN, "зеленым", Style.RESET_ALL)
print("Эффективные по Парето и устойчивые по Нэшу одновременно выделены", Fore.YELLOW, "жёлтым", Style.RESET_ALL)

print("\nПроезд по мосту.")
printpretty(most, enumeration(most))


print("\nДилемма заключённого.")
printpretty(prison, enumeration(prison))


print("\nСемейный спор.")
printpretty(family, enumeration(family))


print("\nСлучайная матрица.")
printpretty(array, enumeration(array))


print("\nВторая часть.")
printpretty(zadaca, enumeration(zadaca))


u = np.array([1, 1])
# @ - оператор умножения матриц (работает в python 3.5 и выше)
x = u @ np.linalg.inv(zadacaB) / (u @ np.linalg.inv(zadacaB) @ u.transpose())
y = np.linalg.inv(zadacaA) @ u.transpose() / (u @ np.linalg.inv(zadacaA) @ u.transpose())
print("\nВ смешанных стратегиях есть ещё одна ситуация равновесия x={0}, y={1}".format(x,y))
'''
x_0 = (zadacaB[1, 1] - zadacaB[1, 0]) / (zadacaB[0, 0] + zadacaB[1, 1] - zadacaB[1, 0] - zadacaB[0, 1])
x_1 = (zadacaB[0, 0] - zadacaB[0, 1]) / (zadacaB[0, 0] + zadacaB[1, 1] - zadacaB[1, 0] - zadacaB[0, 1])
y_0 = (zadacaA[1, 1] - zadacaA[0, 1]) / (zadacaA[0, 0] + zadacaA[1, 1] - zadacaA[1, 0] - zadacaA[0, 1])
y_1 = (zadacaA[0, 0] - zadacaA[1, 0]) / (zadacaA[0, 0] + zadacaA[1, 1] - zadacaA[1, 0] - zadacaA[0, 1])
print("В смешанных стратегиях есть ещё одна точка равновесия x*=({0:.3f}/ {1:.3f}) y*=({2:.3f}/ {3:.3f})".format(x_0, x_1, y_0, y_1))
'''
print("Равновесные выигрыши v1={0:.3f}, v2={1:.3f}".format(1 / (u @ np.linalg.inv(zadacaA) @ u.transpose()),1 / (u @ np.linalg.inv(zadacaB) @ u.transpose())))