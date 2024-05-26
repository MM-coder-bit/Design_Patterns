'''
Composição é uma forma de modelar relações "tem um" (has-a) em vez de relações "é um" (is-a).
No caso do Carro, ele "tem um" motor e "tem quatro" pneus.
'''

# Define uma classe chamada 'Motor'
class Motor:

    # Método que simula o motor sendo ligado
    def ligar(self: object):
        print('Motor ligado...')

# Define uma classe chamada 'Pneu'
class Pneu:

    # Método que simula o pneu sendo cheio
    def encher(self: object):
        print('Pneu cheio...')

# Define uma classe chamada 'Carro'
class Carro:

    # Método construtor da classe Carro. É chamado quando uma nova instância da classe é criada.
    def __init__(self: object, modelo: str):
        # Atributo privado que armazena o modelo do carro
        self.__modelo = modelo
        # Atributo privado que armazena uma instância da classe Motor
        self.__motor = Motor()
        # Atributos privados que armazenam instâncias da classe Pneu
        self.__pneu1 = Pneu()
        self.__pneu2 = Pneu()
        self.__pneu3 = Pneu()
        self.__pneu4 = Pneu()

# Cria uma instância da classe Carro com modelo 'Fusca'
fusca = Carro('Fusca')
# Acessa o atributo privado '__motor' da instância 'fusca' e chama o método 'ligar' do motor
fusca._Carro__motor.ligar()
# Acessa o atributo privado '__pneu' da instância 'fusca' e chama o método 'enxer' do pneu
fusca._Carro__pneu1.encher()
fusca._Carro__pneu3.encher()
