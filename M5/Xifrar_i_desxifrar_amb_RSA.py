"""
Els usuaris A i B es disposen a utilitzar el sistema RSA per intercanviar-se informació.
L'usuari A ha escollit n subíndex A=10057 i e subíndex A=983 ;
l'usuari B ha triat n subíndex B=511 i e subíndex B=329.
L'usuari A desitja enviar la seva edat m=86 xifrada a B. Calculeu el criptograma c que l'usuari A enviarà a l'usuari B.
"""
# c = m^e mod n
# print(pow(86, 329) % 511)  # 277

"""
Els usuaris A i B es disposen a utilitzar el sistema RSA per intercanviar-se informació. 
L'usuari A ha escollit n subíndex A=6059 i e subíndex A=4669 ; l'usuari B ha triat n subíndex B=3737 i e subíndex B=293 .
L'usuari A desitja enviar la seva edat m=88 xifrada a B. Calculeu el criptograma c que l'usuari A enviarà a l'usuari B.
"""
print(pow(88, 293, 3737))  # 1102

"""
Els usuaris A i B es disposen a utilitzar el sistema RSA per intercanviar-se informació. L'usuari A ha escollit n_A=3599, 
format pels primers 61 i 59, i e_A=1547 ; l'usuari B ha triat n_B=341, formats pels primers 31 i 11, i e_B=53.
L'usuari B ha rebut el criptograma c=325 de l'usuari A. Desxifreu el contingut del missatge.
"""

# m = c^d mod n

# Calculem ϕ (n) :
# ϕ (n) = (p – 1)(q – 1)
# ϕn = (31 - 1) * (11 - 1)

# Calculem d: d = e^–1 mod ϕ (n)
# d = pow(53, -1, ϕn)

# m = c^d mod n
# print(pow(325, d, 341))  # 85

"""
Els usuaris A i B es disposen a utilitzar el sistema RSA per intercanviar-se informació.
L'usuari A ha escollit n subíndex A=1081 i e subíndex A=863 ; l'usuari B ha triat n subíndex B=5029 i e subíndex B=3913 .
L'usuari A desitja enviar la seva edat m=99 xifrada a B. Calculeu el criptograma c que l'usuari A enviarà a l'usuari B.
"""

# c = m^e mod n
# print(pow(99, 3913) % 5029)  # 2851

# print(pow(99, 3913) % 5029)  # 2851

"""
Els usuaris A i B es disposen a utilitzar el sistema RSA per intercanviar-se informació.
 L'usuari A ha escollit n subíndex A=793, format pels primers 61 i 13, i e subíndex A=703 ; 
 l'usuari B ha triat n subíndex B=649, formats pels primers 11 i 59, i e subíndex B=577 .
L'usuari B ha rebut el criptograma c=1 de l'usuari A. Desxifreu el contingut del missatge.
"""

# Calculem ϕ (n) :
# ϕ (n) = (p – 1)(q – 1)
# ϕn = (11 - 1) * (59 - 1)

# Calculem d: d = e^–1 mod ϕ (n)
# d = pow(577, -1, ϕn)

# m = c^d mod n
# print(pow(1, d, 649))  # 85

"""
k_pub = (n,e) = (2848299073,1535231195)
k_priv = (d) = (1437751395)

n = 2848299073
e = 1535231195
d = 1437751395
"""

n = 34933
e = 14023
d = 27127

m = 50


c = pow(m, e, n)
# print(pow(c, d, n))
