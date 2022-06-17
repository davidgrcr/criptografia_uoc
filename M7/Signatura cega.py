"""
Suposem que els usuaris A i B volen executar el protocol de signatura cega amb RSA que es descriu en l'apartat 3.1 de mòdul 7 de l'assignatura.
L'usuari A vol que B li signi el missatge m=9058 sense que conegui el contingut del missatge.
Per a fer-ho, utilitzen el protocol de signatura cega amb l'RSA.
La clau pública d'A és (nA=37627, eA=10067) i la seva clau privada és dA=4243. La clau pública de B és (nB=22733, eB=20711)
i la seva clau privada és dB=13415.
L'usuari A tria en el pas 1 del protocol el valor r=4407.
Indiqueu quin és el valor que l'usuari B li envia a l'usuari A en el segon pas del protocol.
La resposta correcta és: 4430
"""
r = 4407
n = 22733
e = 20711
t = pow(r, e, n)
m = 9058
d = 13415

m_ = m * t % n
s_ = pow(m_, d, n)
print(s_)

"""
Suposem que els usuaris A i B volen executar el protocol de signatura cega amb RSA que es descriu en l'apartat 3.1 de mòdul 7 de l'assignatura. 
L'usuari A vol que B li signi el missatge m=23845 sense que conegui el contingut del missatge. 
Per a fer-ho, utilitzen el protocol de signatura cega amb l'RSA. 
La clau pública d'A és (nA=40301, eA=18493) i la seva clau privada és dA=34957. 
La clau pública de B és (nB=26219, eB=8081) i la seva clau privada és dB=8585. 
L'usuari A tria en el pas 1 del protocol el valor r=24719. Indiqueu quin és el valor que l'usuari B li envia a l'usuari A en el segon pas del protocol.
La resposta correcta és: 9391
"""

r = 24719
n = 26219
e = 8081
t = pow(r, e, n)
m = 23845
d = 8585

m_ = m * t % n
s_ = pow(m_, d, n)
print(s_)


"""
Suposem que els usuaris A i B volen executar el protocol de signatura cega amb RSA que es descriu en l'apartat 3.1 de mòdul 7 de l'assignatura.
L'usuari A vol que B li signi el missatge m=8071 sense que conegui el contingut del missatge. 
Per a fer-ho, utilitzen el protocol de signatura cega amb l'RSA. La clau pública d'A és (nA=19879, eA=6959) i la seva clau privada és dA=4559. 
La clau pública de B és (nB=19939, eB=16573) i la seva clau privada és dB=18349. 
L'usuari A tria en el pas 1 del protocol el valor r=12616. 
Indiqueu quin és el valor que l'usuari B li envia a l'usuari A en el segon pas del protocol.
"""

r = 12616
n = 19939
e = 16573
t = pow(r, e, n)
m = 8071
d = 18349

m_ = m * t % n
s_ = pow(m_, d, n)
print(s_)

"""
Suposem que els usuaris A i B volen executar el protocol de signatura cega amb RSA que es descriu en l'apartat 3.1 de mòdul 7 de l'assignatura. 
L'usuari A vol que B li signi el missatge m=14365 sense que conegui el contingut del missatge. 
Per a fer-ho, utilitzen el protocol de signatura cega amb l'RSA. La clau pública d'A és (nA=16867, eA=12023) i la seva clau privada és dA=1487. 
La clau pública de B és (nB=16637, eB=1213) i la seva clau privada és dB=14557.
L'usuari A tria en el pas 1 del protocol el valor r=3900. Indiqueu quin és el valor que l'usuari B li envia a l'usuari A en el segon pas del protocol.
"""

r = 3900
n = 16637
e = 1213
t = pow(r, e, n)
m = 14365
d = 14557

m_ = m * t % n
s_ = pow(m_, d, n)
print('PAC 5: ', s_)
