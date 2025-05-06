def somar_numeros(lista):
    total = 0
    for i in lista:
        total += i

    media = total / len(lista)
    return media

numeros = [2, 44, 74, 34, 55, 81]

print(somar_numeros(numeros))