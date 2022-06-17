"""
El protocol de tres passos de Shamir permet establir una comunicació segura entre dues persones sense cap intercanvi de claus previ.
 Tot i que es pot fer servir Vernam com a funció de xifratge per a executar aquest protocol (ja que té les propietats requerides), el seu ús no n'és gens recomanable.

En Julian i en Bradley fan servir el protocol de tres passos de Shamir amb Vernam per tal d'enviar-se un missatge M de forma segura (o això creuen).
La NSA, fent ús de la xarxa ECHELON, aconsegueix interceptar els 3 missatges intercanviats:

J -> B : 39E23021F8F64F0
B -> J : B86672F75C2DED0
J -> B : 622C64F5538D5C6

Els analistes de la NSA no tarden gaire en descobrir el missatge M que en Julian ha enviat a en Bradley.
Però no cal disposar de tot el poder de còmput de la NSA per trobar aquest missatge, no? Quin és el missatge que ha enviat en Julian a en Bradley amb l'execució del protocol de 3 passos de Shamir?

Nota: Els valors mostrats són cadenes hexadecimals. Entreu el valor del missatge M també com a una cadena de valors hexadecimals, per exemple 8A5EF0 (feu servir majúscules per a les lletres).
"""


def hex2bin(string):
    output = ''
    for i in range(len(string)):
        h = string[i]
        h_size = len(h) * 4
        output += (bin(int(h, 16))[2:]).zfill(h_size)

    return output


def xor(str1, str2):
    xor = ""
    for i in range(len(str1)):
        xor += str(int(str1[i]) ^ int(str2[i]))

    return xor


def atac_a_tres_passos_de_Shamir(message):

    m = xor(xor(hex2bin(message[0]), hex2bin(message[1])), hex2bin(message[2]))
    m = hex(int(m, 2)).upper()
    m = m[2:]
    return m


message = ['39E23021F8F64F0', 'B86672F75C2DED0', '622C64F5538D5C6']
print('message:', atac_a_tres_passos_de_Shamir(message))  # La resposta correcta és: E3A82623F756FE6

"""
J -> B : 7550D823E9DAE32
B -> J : E69E3D40C00FCB1
J -> B : 2B9325D830888F0
"""
message = ['7550D823E9DAE32', 'E69E3D40C00FCB1', '2B9325D830888F0']
print('message:', atac_a_tres_passos_de_Shamir(message))  # La resposta correcta és: E3A82623F756FE6

"""
J -> B : B7B796DA8DF9562
B -> J : 1371768E13CC59A
J -> B : E53E9F8DB351B20
"""

message = ['B7B796DA8DF9562', '1371768E13CC59A', 'E53E9F8DB351B20']
print('message:', atac_a_tres_passos_de_Shamir(message))  # La resposta correcta és: 41F87FD92D64BD8
