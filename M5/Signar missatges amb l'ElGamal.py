"""
Dos usuaris A i B, s'intercanvien missatges amb el sistema de clau pública ElGamal sobre el grup multiplicatiu normal
nombres enters subíndex 211 fi subíndex elevat a producte asterisco amb alfa igual 195. L'usuari A envia a B el missatge m=32.

La clau privada de A és a=47 i la clau pública és alfa elevat a a=133. Per tal d'enviar el missatge, A ha escollit a l'atzar h=151.

Quina és la signatura [r,s] que rebrà B?

Nota: Respecteu el format indicat per a donar la solució. És a dir, doneu els dos valors en una llista: [r,s] .

"""
h = 151
x = 195
p = 211

r = pow(x, h, p)

m = 32
d = 47  # clau privada

p = p - 1
s = (m - d * r) % p
s = s * pow(h, -1, p) % p
txt = "[{r},{s}]".format(r=r, s=s)
# print(txt)

"""
Dos usuaris A i B, s'intercanvien missatges amb el sistema de clau pública ElGamal sobre el grup multiplicatiu normal 
nombres enters subíndex 269 fi subíndex elevat a producte asterisco amb alfa igual 111. 
L'usuari A envia a B el missatge m=141. La clau privada de A és a=214 i la clau pública és alfa elevat a a=164. 
Per tal d'enviar el missatge, A ha escollit a l'atzar h=243.
Quina és la signatura [r,s] que rebrà B?
Nota: Respecteu el format indicat per a donar la solució. És a dir, doneu els dos valors en una llista: [r,s] .
"""

h = 243
x = 111
p = 269

r = pow(x, h, p)

m = 141
d = 214

p = p - 1

s = (m - d * r) % p
s = s * pow(h, -1, p) % p
txt = "[{r},{s}]".format(r=r, s=s)
# print(txt)

"""
# pàg 20 M5
s1 = (424242 - 807878087 * 1675101370) % 3725468626
print(s1 * pow(249, -1, 3725468626) % 3725468626)
"""

h = 243
x = 111
p = 269
m = 141
d = 214


def signaturaElGamal(h, x, p, m, d):
    r = pow(x, h, p)

    p = p - 1

    s = (m - d * r) % p
    s = s * pow(h, -1, p) % p

    return [r, s]


# print(signaturaElGamal(h, x, p, m, d))

"""
Dos usuaris A i B, s'intercanvien missatges amb el sistema de clau pública ElGamal sobre el grup multiplicatiu normal 
nombres enters subíndex 67 fi subíndex elevat a producte asterisco amb alfa=11. L'usuari A envia a B el missatge m= 41.
La clau privada de A és a= 58 i la clau pública és alfa elevat a a=60.
Quina (o quines) de les següents signatures són signatures vàlides del missatge m realitzades per l'usuari A?
Nota: Les signatures són parells de valors, [r,s] .
"""
m = 41
p = 67
x = 11
d = 58
alfa = 60

r = 11
s = 63

a = pow(alfa, r, p)
print(a * pow(r, s, p) % p)
print(pow(x, m, p))
