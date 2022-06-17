"""
Els usuaris Alice i Bob es disposen a utilitzar el sistema RSA per signar els missatges que s'envien.
L'Alice té la clau pública (na, ea)=(365, 5) i la clau privada (na,da)=(365,173).
En Bob té la clau pública (nb, eb)=(7171, 6191) i la clau privada (nb,db)=(7171,3911).

L'Alice envia el missatge m=2583 signat a en Bob. Quina és la signatura de l'Alice sobre aquest missatge?
"""
m = 2583
d = 173
n = 365
s = pow(m, d, n)

# print(s)  # 53

"""
Els usuaris Alice i Bob es disposen a utilitzar el sistema RSA per signar els missatges que s'envien. 
L'Alice té la clau pública (na, ea)=(721, 277) i la clau privada (na,da)=(721,517).
En Bob té la clau pública (nb, eb)=(2033, 1049) i la clau privada (nb,db)=(2033,713).
L'Alice envia el missatge m=1601 signat a en Bob. Quina és la signatura de l'Alice sobre aquest missatge?
"""

m = 1601
d = 517
n = 721
s = pow(m, d, n)

# print(s)  # 159

"""
Els usuaris Alice i Bob es disposen a utilitzar el sistema RSA per signar els missatges que s'envien. 
L'Alice té la clau pública (na, ea)=(203, 41) i la clau privada (na,da)=(203,41). 
En Bob té la clau pública (nb, eb)=(793, 463) i la clau privada (nb,db)=(793,367).
L'Alice envia el missatge m=779 signat a en Bob. Quina és la signatura de l'Alice sobre aquest missatge?
"""

m = 779
d = 41
n = 203
s = pow(m, d, n)

print(s)  # 123
