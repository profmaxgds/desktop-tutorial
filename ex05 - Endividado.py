# o comando Read_in (faz a captura dos dados e dispõe em lista)
import sys
def read_in():
    L = sys.stdin.readlines()
    for i in range(len(L)):
        L[i] = L[i].replace("\n", "")
    return L
#V = visitas
#M = quantidade de museus visitados
#P= preços praticados
#x= preço em lista
#T=visitas de Taurino e Ada
#A=Valor acumulado ao longo das visitas
def main():
    V = read_in()
    i=0
    while i<len(V):
        M=int(V[i])
        if M>0:
            P=[int(x) for x in V[i+1].split(" ")]
            T=0
            A=0
            for x in P:
                A=A+int(x)
                if A%100==0:
                    T=T+1
            print(T)
            i+=2
        else:
            break
if __name__ == "__main__":
    main()