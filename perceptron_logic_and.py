import math

def produto_escalar(vetor_1, vetor_2):
    
    vetor_resultado = []
    for i in range(len(vetor_1)):
        vetor_resultado.append((vetor_1[i]*vetor_2[i]))


    return vetor_resultado

def somatorio(vetor):
    s = 0 
    for i in vetor:
        s = s+i
    
    return s

def funcao_ativacao(valor):

    tangente_hiperbolica = lambda x: (1-math.exp(-2*x))/(1+math.exp(-2*x))
    
    return tangente_hiperbolica(valor)

def perceptron(entrada, pesos, bias):

    produto = produto_escalar(entrada,pesos)
    soma = somatorio(produto)

    valor_final = soma+bias

    return funcao_ativacao(valor_final)


pesos = [0.5, 0.6]
bias = -0.3

entrada = [1,1]

prob = perceptron(entrada, pesos, bias)

if prob>0.5:
    print("Verdadeiro, resultado:", prob)

else:
    print("Falso, resultado:", prob)