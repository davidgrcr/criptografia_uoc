"""
Algorisme de xifratge ElGamal
A partir d’un missatge en clar m i la clau pública del destinatari k_pub = (p, α , β ),
es calcula el missatge xifrat c:
1) Es tria un nombre aleatori v i es calcula c1 = α^v mod p.
2) Es recupera la clau pública del receptor i es calcula c 2 = m · β v mod p.
3) S’envia el missatge xifrat (c 1 ,c 2 ).
"""

"""
Dos usuaris A i B, s'intercanvien missatges amb el sistema de clau pública ElGamal
sobre el grup multiplicatiu normal nombres enters subíndex 317 fi subíndex elevat a
producte asterisc amb alfa igual 300. L'usuari A envia a B el missatge m=185. La clau
privada de B és b=159 i la clau pública és alfa elevat a b igual 17.
Per tal d'enviar el missatge, A ha escollit a l'atzar v=226.
Si el missatge xifrat que B rebrà és c=(c subíndex 1,c subíndex 2). Quin és el valor c subíndex 2?
"""

m = 185
x = 300
d = 159
p = 317
v = 226

# β = α^d mod p
β = pow(x, d, p)

c2 = (m * pow(β, v, p) % p)
# print(c2)

"""
Dos usuaris A i B, s'intercanvien missatges amb el sistema de clau pública ElGamal sobre el grup multiplicatiu normal 
nombres enters subíndex 47 fi subíndex elevat a producte asterisco amb alfa igual 31. L'usuari A envia a B el missatge m=31. 
La clau privada de B és b=35 i la clau pública és alfa elevat a b igual 43. Per tal d'enviar el missatge, A ha escollit a l'atzar v=20. 
Si el missatge xifrat que B rebrà és c=(c subíndex 1,c subíndex 2). Quin és el valor c subíndex 2?
"""

m = 31
x = 31
d = 35
p = 47
v = 20

# β = α^d mod p
β = pow(x, d, p)

c2 = (m * pow(β, v, p) % p)
print(c2)

"""
Dos usuaris A i B, s'intercanvien missatges amb el sistema de clau pública ElGamal sobre el grup multiplicatiu normal
nombres enters subíndex 337 fi subíndex elevat a producte asterisco amb alfa igual 194. 
L'usuari A envia a B el missatge m=160. La clau privada de B és b=42 i la clau pública és alfa elevat a b igual 111. 
Per tal d'enviar el missatge, A ha escollit a l'atzar v=315. 
Si el missatge xifrat que B rebrà és c=(c subíndex 1,c subíndex 2). Quin és el valor c subíndex 2?
"""
m = 160
x = 194
d = 42
p = 337
v = 315

# β = α^d mod p
β = pow(x, d, p)

c2 = (m * pow(β, v, p) % p)
# print(c2)

m = 185
x = 300
d = 159
p = 317
v = 226


"""
Dos usuaris A i B s'intercanvien missatges amb el sistema de clau pública ElGamal, 
sobre un grup multiplicatiu normal nombres enters subíndex 13 fi subíndex elevat a producte asterisco . La clau privada de B és b=2. 
Quina és la clau pública de l'usuari B si alfa=11? (de la terna (p, alfa, β), només cal indicar el valor β)
"""
x = 11
p = 13
d = 2

# β = α^d mod p
# print(pow(x, d, p))
