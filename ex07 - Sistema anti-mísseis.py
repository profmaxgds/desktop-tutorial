import sys as sys

def lis(a):
	L = []
	for (k,v) in enumerate(a):
		L.append(max([L[i] for (i,n) in enumerate(a[:k]) if n<v] or [[]], key=len) + [v])
	return max(L, key=len)

def calculate (lista):
    if (len(lista) > 0):
        result = lis(lista)
        print ("Acertos:", len(result))
        for i in range(0, len(result)):
            print(result[i], end="")
            if (i != len(result)):
                print()

def main():
    L = sys.stdin.readlines()
    lista = []
    testes = int(L[0]) + 1
    for i in range(1, len(L)):
        entrada = L[i]
        if (i == len(L) -1):
            num = int(entrada) 
            lista.append(num)

        if ((not entrada[0].isdigit()) or i == len(L) -1):
            testes = testes -1 
            calculate(lista)
            lista = []
            if (testes != 0 and i > 1):
                print()
        else :
            if entrada[0].isdigit(): 
                num = int(entrada) 
                lista.append(num)   
                

if __name__ == "__main__":
    main()