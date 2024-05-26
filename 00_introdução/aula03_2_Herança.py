from typing import List, Tuple

# Define uma classe chamada 'Pessoa'
class Pessoa:

    # Método construtor da classe Pessoa. É chamado quando uma nova instância da classe é criada.
    def __init__(self: object, nome: str) -> None:
        # Atributo privado que armazena o nome da pessoa
        self.__nome = nome

    # Método da classe Pessoa que imprime uma mensagem indicando que a pessoa está andando
    def andar(self: object) -> None:
        print('Estou andando...')


# Define uma classe chamada 'Aluno' que herda da classe 'Pessoa'
class Aluno(Pessoa):

    # Método construtor da classe Aluno. É chamado quando uma nova instância da classe é criada.
    def __init__(self: object, nome: str, matricula: str) -> None:
        # Chama o construtor da classe base (Pessoa) para inicializar o atributo 'nome'
        super().__init__(nome)
        # Atributo privado que armazena a matrícula do aluno
        self.__matricula = matricula


# Cria uma instância da classe Aluno com nome 'Felicity' e matrícula '12345'
felicity = Aluno('Marques', '12345')

# Chama o método 'andar' na instância de Aluno 'felicity'
felicity.andar()

print(felicity.__dict__)