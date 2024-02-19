

def ordenacaoTopologicaKahn(listaAdj):
    grauEntrada = [0] * len(listaAdj)

    for i in range(len(listaAdj)):
        for j in listaAdj[i]:
            grauEntrada[j] += 1

    fila = [i for i in range(len(grauEntrada)) if grauEntrada[i] == 0]

    ordenacaoTopologica = []

    while fila:
        v = fila.pop(0)

        ordenacaoTopologica.append(v)

        for i in listaAdj[v]:
            grauEntrada[i] -= 1

            if grauEntrada[i] == 0:
                fila.append(i)

    if len(ordenacaoTopologica) == len(listaAdj):
        print(ordenacaoTopologica) 

    else:
        print("NÃO DAG")