# Importa o módulo ABC e o decorador abstractmethod do módulo abc
from abc import ABC, abstractmethod

# Importa a função uuid4 do módulo uuid
from uuid import uuid4

# Define uma classe abstrata Pessoa que herda de ABC (Abstract Base Class)
class Pessoa(ABC):

    # Método inicializador da classe Pessoa, que recebe o nome como parâmetro
    def __init__(self: object, nome: str):
        self.__nome = nome  # Atributo privado __nome é definido com o valor do parâmetro nome
    
    # Método abstrato que deve ser implementado pelas subclasses de Pessoa
    @abstractmethod
    def ganhar_dinheiro(self: object):
        pass  # Método abstrato não tem implementação

# Define uma classe Aluno que herda da classe abstrata Pessoa
class Aluno(Pessoa):

    # Método inicializador da classe Aluno, que chama o inicializador da classe Pessoa
    def __init__(self: object, nome: str):
        super().__init__(nome)  # Chama o método __init__ da classe Pessoa
        self.__matricula = str(uuid4()).split('-')[0].upper()  # Gera um identificador único para a matrícula e converte para maiúsculas

    # Implementa o método abstrato ganhar_dinheiro da classe Pessoa
    def ganhar_dinheiro(self: object):
        print('Como ganhar dinheiro?')  # Implementação do método que apenas imprime uma mensagem

# Instancia um objeto da classe Aluno com o nome 'Angelina'
aluno1 = Aluno('Angelina')
aluno2 = Aluno('Mateus')
# Imprime o dicionário de atributos do objeto aluno1
print(aluno1.__dict__)
print(aluno2.__dict__)
