import random

n = int(input()) # Ввод размера квадратной матрицы
matrix = []
sum1 = 0 # Сумма чисел главной диагонали
sum2 = 0 # Сумма чисел побочной диагонали

for i in range(n): # Заполнение матрицы рандомными значениями
    matrix.append([])
    for j in range(n):
        matrix[i].append(random.randint(1,100))

for i in range(n): # Вычисление суммы главной диагонали
    sum1 += matrix[i][i]

for j in range(n): # Вычисление суммы побочной диагонали
    sum2 += matrix[j][i]
    i -= 1

for i in range(n):
    print(matrix[i])

if sum1 > sum2:
    print(f"Главная диагональ({sum1}) > Побочная диагональ({sum2})")
elif sum1 < sum2:
    print(f"Главная диагональ({sum1}) < Побочная диагональ({sum2})")
else:
    print(f"Главная диагональ({sum1}) = Побочная диагональ({sum2})")

