# Define uma função para gerar a sequência de Fibonacci
def gerar_fibonacci(qtd: int):
    # Verifica se a quantidade de termos solicitada é menor ou igual a 0
    if qtd <= 0:
        print('A quantidade deve ser maior que 0')
    else:
        # Imprime uma mensagem indicando quantos termos da sequência serão gerados
        print(f'A sequência Fibonacci para {qtd} termo(s) é: ')
        # Inicializa o contador de termos
        contador: int = 0
        # Inicializa os dois primeiros termos da sequência de Fibonacci
        aux1: int = 0
        aux2: int = 1
        # Loop para gerar a sequência de Fibonacci até a quantidade especificada de termos
        while contador < qtd:
            # Imprime o próximo termo da sequência
            print(aux1)
            # Calcula o próximo termo da sequência de Fibonacci
            proximo = aux1 + aux2
            # Atualiza os valores dos termos auxiliares para a próxima iteração
            aux1 = aux2
            aux2 = proximo
            # Incrementa o contador de termos
            contador += 1

# Chama a função para gerar a sequência de Fibonacci com 7 termos
# a ideia de abstraão é que o a pessoa que vá usar não necessite saber da 
# complexidade da função
gerar_fibonacci(7)


'''
class Motor:

    def ligar(self: object):
        print('Motor ligado...')

class Pneu:

    def enxer(self: object):
        print('Pneu cheio...')


class Carro:

    def __init__(self: object, modelo: str):
        self.__modelo = modelo
        self.__motor = Motor()
        self.__pneu1 = Pneu()
        self.__pneu2 = Pneu()
        self.__pneu3 = Pneu()
        self.__pneu4 = Pneu()


fusca = Carro('Fusca')
fusca._Carro__motor.ligar()
'''