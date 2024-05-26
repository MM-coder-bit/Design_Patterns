# Importa a classe datetime do módulo datetime para trabalhar com datas e horas
from datetime import datetime

# Define uma classe chamada 'Pessoa'
class Pessoa:
    
    # Método construtor da classe Pessoa. É chamado quando uma nova instância da classe é criada.
    def __init__(self: object, nome: str) -> None:
        # Atributo privado que armazena o nome da pessoa
        self.__nome = nome
        # Atributo privado que armazena a data e hora de nascimento como o momento atual
        self.__nascimento = datetime.now()  # now.year, now.month, now.day, now.hour, now.minute, now.second

    def __str__(self:object) -> str:
        return self.__nome
        
    def __repr__(self:object) -> str:
        return self.__nome

# Define uma classe chamada 'Carro'
class Carro:
    
    # Método construtor da classe Carro. É chamado quando uma nova instância da classe é criada.
    def __init__(self: object, is_sedan: bool = False) -> None:
        # Atributo privado que indica se o carro é um sedan (por padrão é False)
        self.__is_sedan = is_sedan
        # Atributo privado que armazena a velocidade atual do carro (inicialmente 0)
        self.__velocidade = 0
        # Atributo privado que armazena o motorista do carro (inicialmente None)
        self.__motorista = None
    
    def __str__(self:object) -> str:
        if self.__motorista:
            return f"Carro {self.__is_sedan} com motorista {self.__motorista.__nome}"
        else:
            return 'Carro sem motorista'
    
    # Método para dirigir o carro, recebendo um objeto do tipo Pessoa como motorista
    def dirigir(self: object, motorista: Pessoa) -> None:
        # Define o motorista do carro
        self.__motorista = motorista
        # Acelera o carro em 1 unidade de velocidade ao começar a dirigir
        self.acelerar(1)

    # Método para acelerar o carro, incrementando a velocidade em um valor especificado
    def acelerar(self: object, velocidade: int) -> None:
        # Incrementa a velocidade atual do carro pelo valor passado como argumento
        self.__velocidade += velocidade
    
    # Método para parar o carro, definindo a velocidade para 0
    def parar(self: object) -> None:
        # Define a velocidade do carro como 0
        self.__velocidade = 0
