#imprimir elementos de um vetor qualquer
#criando um vetor:
vetor = ["azul","branco","verde", "vermelho"]
for cor in vetor:
    print(cor)

#vamos fazer a mesma coisa
#fazendo de outra forma (caso precise do indice)
for i in range(0,len(vetor)):
    print(f"Elemento {i}: Valor: {vetor[i]}")