import numpy as np

"""
Tenim un esquema llindar (4 , 6 ) de compartició de secrets polinomial i treballem als enters mòdul 1091.
Els fragments de 5 usuaris són els següents:
obre claudàtors 815 coma 219 tanca claudàtors,
obre claudàtors 542 coma 1009 tanca claudàtors,
obre claudàtors 443 coma 452 tanca claudàtors,
obre claudàtors 632 coma 130 tanca claudàtors,
obre claudàtors 914 coma 976 tanca claudàtors

Si és possible, calcula el valor del secret. En cas contrari escriu "NO" en la resposta.
La resposta correcta és: 528
"""


# S + a_1 · 815 + a_2 · 815^2 + a_3 · 815^3 = 219 (mod 1091)
# S + a_1 · 542 + a_2 · 542^2 + a_3 · 542^3 = 1009 (mod 1091)
# S + a_1 · 443 + a_2 · 443^2 + a_3 · 443^3 = 452 (mod 1091)
# S + a_1 · 632 + a_2 · 632^2 + a_3 · 632^3 = 130 (mod 1091)
# S + a_1 · 914 + a_2 · 914^2 + a_3 · 914^3 = 976 (mod 1091)

def populate(arrayLength, number, modul):
    subarray = []
    for i in range(arrayLength):
        if i > 0:
            subarray.append(pow(number, i, modul))

    return subarray


def fillArray(llindars, modul):
    array = []
    llindarsLen = len(llindars)
    for i in range(len(llindars)):
        subarray = []
        for j in range(len(llindars[i])):
            number = llindars[i][j]
            if j == 0:
                subarray = (populate(llindarsLen, number, modul))
            else:
                subarray.insert(0, number)
                array.append(subarray)

    return np.array(array)


def getDetFromLlindar(llindars, modul):
    mat = fillArray(llindars, modul)
    d = np.linalg.det(mat) % modul
    return round(d)


arr = [[815, 219], [542, 1009], [443, 452], [632, 130]]
modul = 1091
"""
mat = np.array([
    [219, 815, pow(815, 2, 1091), pow(815, 3, 1091)],
    [1009, 542, pow(542, 2, 1091), pow(542, 3, 1091)],
    [452, 443, pow(443, 2, 1091), pow(443, 3, 1091)],
    [130, 632, pow(632, 2, 1091), pow(632, 3, 1091)]
]
)
"""
a = getDetFromLlindar(arr, modul)
"""
mat = np.array([
    [1, 815, pow(815, 2, 1091), pow(815, 3, 1091)],
    [1, 542, pow(542, 2, 1091), pow(542, 3, 1091)],
    [1, 443, pow(443, 2, 1091), pow(443, 3, 1091)],
    [1, 632, pow(632, 2, 1091), pow(632, 3, 1091)]
]
)
"""

arr = [[815, 1], [542, 1], [443, 1], [632, 1]]
b = getDetFromLlindar(arr, modul)

b = pow(b, -1, modul)  # invers

print(a * b % modul)

"""
En un esquema de compartició de secrets polinòmic de Shamir amb llindar (3,6) els par-
ticipants reben els fragments (58,137),(11,48),(50,99),(80,50),(104,33),(39,114). Tenint en
compte que treballen a Z 149 , recupereu el secret.

S + a_1 · 50 + a_2 · 50^2 = 99 (mod 149)
S + a_1 · 80 + a_2 · 80^2 = 50 (mod 149)
S + a_1 · 39 + a_2 · 39^2 = 114 (mod 149)
"""

mat = np.array([[99, 50, 116],
                [50, 80, 142],
                [114, 39, 31]]
               )

D = np.linalg.det(mat) % 149
a = round(D)

mat = np.array([[1, 50, 116],
                [1, 80, 142],
                [1, 39, 31]]
               )

D = np.linalg.det(mat) % 149
b = round(D)
b = pow(b, -1, 149)

print(a * b % 149)

"""
Tenim un esquema llindar (3 , 5 ) de compartició de secrets polinomial i treballem als enters mòdul 397. 
Els fragments de 5 usuaris són els següents: 
obre claudàtors 143 coma 217 tanca claudàtors, 
obre claudàtors 119 coma 108 tanca claudàtors, 
obre claudàtors 126 coma 122 tanca claudàtors, 
obre claudàtors 355 coma 327 tanca claudàtors, 
obre claudàtors 153 coma 214 tanca claudàtors

Si és possible, calcula el valor del secret. En cas contrari escriu "NO" en la resposta.
La resposta correcta és: 226

"""

arr = [[143, 217], [119, 108], [126, 122]]
modul = 397
a = getDetFromLlindar(arr, modul)

arr = [[143, 1], [119, 1], [126, 1]]
b = getDetFromLlindar(arr, modul)

b = pow(b, -1, modul)  # invers

print(a * b % modul)

"""
Tenim un esquema llindar (3 , 5 ) de compartició de secrets polinomial i treballem als enters mòdul 347.
Els fragments de 5 usuaris són els següents: 
obre claudàtors 111 coma 342 tanca claudàtors, 
obre claudàtors 43 coma 174 tanca claudàtors, 
obre claudàtors 307 coma 298 tanca claudàtors, 
obre claudàtors 287 coma 254 tanca claudàtors, 
obre claudàtors 153 coma 298 tanca claudàtors
Si és possible, calcula el valor del secret. En cas contrari escriu "NO" en la resposta.
La resposta correcta és: 327
"""

arr = [[111, 342], [43, 174], [307, 298]]
modul = 347
a = getDetFromLlindar(arr, modul)

arr = [[111, 1], [43, 1], [307, 1]]
b = getDetFromLlindar(arr, modul)

b = pow(b, -1, modul)  # invers

print(a * b % modul)

"""
Tenim un esquema llindar (4 , 6 ) de compartició de secrets polinomial i treballem als enters mòdul 631. 
Els fragments de 5 usuaris són els següents: 
obre claudàtors 237 coma 387 tanca claudàtors, 
obre claudàtors 122 coma 108 tanca claudàtors, 
obre claudàtors 266 coma 430 tanca claudàtors, 
obre claudàtors 283 coma 504 tanca claudàtors, 
obre claudàtors 530 coma 253 tanca claudàtors
Si és possible, calcula el valor del secret. En cas contrari escriu "NO" en la resposta.
"""

arr = [[237, 387], [122, 108], [266, 430], [283, 504]]
modul = 631
a = getDetFromLlindar(arr, modul)

arr = [[237, 1], [122, 1], [266, 1], [283, 1]]
b = getDetFromLlindar(arr, modul)
b = pow(b, -1, modul)  # invers

print('PAC', a * b % modul)

"""
45 + 70 x + 7 x2 + 41 x3
"""
x = 2
modul = 127

for x in range(1, 11):
    x_1 = 70 * x % modul
    x_2 = 7 * pow(x, 2, modul)  % modul
    x_3 = 41 * pow(x, 3, modul) % modul
    print('x', x)
    print('x_1', x_1)
    print('x_2', x_2)
    print('x_3', x_3)
    print("===================")
