s_0 = 22
s_1 = 34
n = 551
e = 19
d = 451
x_0 = 130
x_1 = 525
k = 174

v = (x_0 + pow(k, e, n)) % n
print(v)

k_0 = pow((v-x_0),d,n)
k_1 = pow((v-x_1),d,n)
s_0_ = s_0 + k_0 % n
s_1_ = s_1 + k_1 % n

print('k_0', k_0)
print('k_1', k_1)
print('s_0_', s_0_)
print('s_1_', s_1_)
"""
Els usuaris A i B estan executant el protocol de transferència inconscient 1-2. 
Els secrets que té l'usuari per enviar són s0=10174 i s1=10639. 
La clau pública RSA de l'usuari A és (n=14351e=3305) i la seva clau privada d=7673. 
Tria els valors correctes que s'intercanviaran en cada pas del protocol
"""
s_0 = 10174
s_1 = 10639
n = 14351
e = 3305
d = 7673
k = 174

x_0 = 3274 #3531
x_1 = 4750 #99
k = 174

v = (x_0 + pow(k, e, n)) % n

print(v)


k_0 = pow((v-x_0),d,n)
k_1 = pow((v-x_1),d,n)
s_0_ = (s_0 + k_0) % n
s_1_ = (s_1 + k_1) % n

print('k_0', k_0)
print('k_1', k_1)
print('s_0_', s_0_)
print('s_1_', s_1_)

