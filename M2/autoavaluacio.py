import math


def bezout(a, b):
    lamb = 1
    s = 0
    t = 1
    mu = 0
    r = b
    old_r = a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        lamb, s = s, lamb - quotient * s
        mu, t = t, mu - quotient * t
    # --------------------------------

    return (lamb, mu)


def phi_euler(max):
    list = range(0, max)

    order = 0
    for i in list:
        if math.gcd(i, max) == 1:
            order += 1
    return order


# 1. Calcula el màxim comú divisor de 35 i 48.
print('1. ', math.gcd(35, 48))

# 2. Calcula els coeﬁcients de la indentitat de Bézout de 35 i 48.
print('2. ', bezout(35, 48))

# 3. Calcula quin és el valor de ϕ (527).
print('3. ', phi_euler(527))

# 6. Troba l’invers de 7 a Z 37 .
print('4. ', pow(7, -1, 37))

# 7. Realitza els càlculs següents a Z 37 .
# 20 + 20
print('7.1 ', (20 + 20) % 37)
# 20 · 4
print('7.2 ', 20 * 4 % 37)
# 20^2
print('7.3 ', pow(20, 2, 37))
# 20/7
print('7.4 ', 20 * pow(7, -1, 37) % 37)
