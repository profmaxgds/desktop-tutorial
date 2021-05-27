import sys
def read_in():
    linhas = sys.stdin.readlines()
    for i in range(len(linhas)):
        linhas[i] = linhas[i].replace("\n", "")
    return linhas
#Buscar lista de planetas, conforme digita.
def main():
    linhas = read_in()
    i = 0
    while linhas[i] != "0":
        if len(linhas[i]) == 1:
            numPlanetas = int(linhas[i])
            listaplanetas = {}
            for j in range(i + 1, i + 1 + numPlanetas):
                planeta, anos, totalanoss = linhas[j].split()
                listaplanetas[planeta] = int(anos) - int(totalanoss)
            escolhaplanetas = dict(sorted(listaplanetas.items(), key=lambda item: item[1]))
            print(next(iter(escolhaplanetas)))
            i += numPlanetas + 1
if __name__ == "__main__":
    main()