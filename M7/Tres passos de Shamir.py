def tres_passos_de_Shamir(k_A, k_B, m, p):
    k_D = pow(k_A, -1, p - 1)

    c1 = pow(m, k_A, p)
    c2 = pow(c1, k_B, p)
    c3 = pow(c2, k_D, p)

    return c3

"""
Suposem que els usuaris A i B volen executar el protocol de tres passos de Shamir per compartir el missatge m=457.
Per a fer-ho utilitzen el criptosistema d'exponenciació tal i com es descriu en l'apartat 1.2 del mòdul 7 de l'assignatura.
Utilitzaran com a primer el valor p=659.
Suposem que la clau per a xifrar que té l'usuari A és KAe = 237 i que la clau per a xifrar que té l'usuari B és KBe = 643.
Indiqueu quin és el valor que l'usuari A li envia a l'usuari B en el tercer pas del protocol.
"""
k_A = 237
k_B = 643
m = 457
p = 659

print(tres_passos_de_Shamir(k_A, k_B, m, p))  # La resposta correcta és: 406


"""
Suposem que els usuaris A i B volen executar el protocol de tres passos de Shamir per compartir el missatge m=240. 
Per a fer-ho utilitzen el criptosistema d'exponenciació tal i com es descriu en l'apartat 1.2 del mòdul 7 de l'assignatura. 
Utilitzaran com a primer el valor p=947. 
Suposem que la clau per a xifrar que té l'usuari A és KAe = 91 i que la clau per a xifrar que té l'usuari B és KBe = 923. 
Indiqueu quin és el valor que l'usuari A li envia a l'usuari B en el tercer pas del protocol.
"""

k_A = 91
k_B = 923
m = 240
p = 947

print(tres_passos_de_Shamir(k_A, k_B, m, p))  # La resposta correcta és: 491

"""
Suposem que els usuaris A i B volen executar el protocol de tres passos de Shamir per compartir el missatge m=23.
Per a fer-ho utilitzen el criptosistema d'exponenciació tal i com es descriu en l'apartat 1.2 del mòdul 7 de l'assignatura. 
Utilitzaran com a primer el valor p=787. Suposem que la clau per a xifrar que té l'usuari A és KAe = 61 i que la clau per a xifrar que té l'usuari B és KBe = 463. 
Indiqueu quin és el valor que l'usuari A li envia a l'usuari B en el tercer pas del protocol.
La resposta correcta és: 177
"""
k_A = 61
k_B = 463
m = 23
p = 787

print(tres_passos_de_Shamir(k_A, k_B, m, p))  # La resposta correcta és: 491

"""
Suposem que els usuaris A i B volen executar el protocol de tres passos de Shamir per compartir el missatge m=460. 
Per a fer-ho utilitzen el criptosistema d'exponenciació tal i com es descriu en l'apartat 1.2 del mòdul 7 de l'assignatura. 
Utilitzaran com a primer el valor p=709. Suposem que la clau per a xifrar que té l'usuari A és KAe = 167 i que la clau per a xifrar que té l'usuari B és KBe = 29. 
Indiqueu quin és el valor que l'usuari A li envia a l'usuari B en el tercer pas del protocol.
"""
k_A = 167
k_B = 29
m = 460
p = 709

print('PAC 5: ', tres_passos_de_Shamir(k_A, k_B, m, p))  # La resposta correcta és: 491