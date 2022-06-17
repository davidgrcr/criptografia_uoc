p = 1097
x = 3
a = 901
b = 476

"""
p = 1277
x = 2
a = 707
b = 1239
# 638
"""

k_pubA = pow(x, a, p)

print(k_pubA)

k_pubB = pow(x, b, p)

print(k_pubB)

k_AB = pow(k_pubB, a, p)

print(k_AB)

k_AB = pow(k_pubA, b, p)

print(k_AB)
