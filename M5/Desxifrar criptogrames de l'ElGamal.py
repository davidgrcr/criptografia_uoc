"""
Dos usuaris A i B s'intercanvien missatges amb el sistema de clau pública ElGamal, sobre un grup multiplicatiu normal
nombres enters elevat a producte asterisco subíndex 211 fi subíndex. L'usuari A envia el missatge m ,
que un cop xifrat queda representat pel parell (182, 203). La clau privada de B és b=142. Quin és el missatge m?
"""
c1 = 182
c2 = 203
d = 142
p = 211

y = pow(c1, d, p)
z = pow(y, -1, p)
# print(z * c2 % p)


"""
Dos usuaris A i B s'intercanvien missatges amb el sistema de clau pública ElGamal,
sobre un grup multiplicatiu normal nombres enters elevat a producte asterisco subíndex 37 fi subíndex. 
L'usuari A envia el missatge m , que un cop xifrat queda representat pel parell (36, 25). 
La clau privada de B és b=26. Quin és el missatge m?
"""
c1 = 36
c2 = 25
d = 26
p = 37

y = pow(c1, d, p)
z = pow(y, -1, p)
# print(z * c2 % p)

"""
# m = c_2 / c^d mod p pàg 16 M5
y = (pow(434020969, 807878087, 3725468627))
print(pow(y, -1, 3725468627))


c1 = 434020969
d = 807878087
p = 3725468627
c2 = 2787237740

y = pow(c1, d, p)
z = pow(y, -1, p)
print(z * c2 % p)
"""

"""
Cosidereu el criptosistema ElGamal, del qual coneixem el fitxer públic calculat a partir de l'element alfa=109 de normal 
nombres enters subíndex 257 fi subíndex. L'usuari A ha construït la seva clau pública com a alfa elevat a 35 fi elevat 
igual 24 espai m o d espai 257 . 
Si sabem que el parell obre parèntesis alfa elevat a v coma c tanca parèntesis igual parèntesi esquerre 50 coma 233 parèntesi dret 
és el resultat de xifrar el missatge m amb la clau pública de l'usuari A. Quin és el missatge original m?
"""

c1 = 50
c2 = 233
d = 35
p = 257

y = pow(c1, d, p)
z = pow(y, -1, p)
print(z * c2 % p)
