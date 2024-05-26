from typing import List, Tuple

# Define uma classe chamada 'Curso'
class Curso:

    # Método construtor da classe Curso. É chamado quando uma nova instância da classe é criada.
    def __init__(self: object, nome: str = 'Curso Padrão', carga_horaria: int = 45):
        # Atributo privado que armazena o nome do curso, com valor padrão 'Curso Padrão'
        self.__nome = nome
        # Atributo privado que armazena a carga horária do curso, com valor padrão 45
        self.__carga_horaria = carga_horaria

# Cria uma instância da classe Curso com valores padrão
curso1: Curso = Curso()
# Cria uma instância da classe Curso com um nome específico e carga horária padrão
curso2: Curso = Curso(nome='Padrões de Projetos em Python')
# Cria uma instância da classe Curso com um nome específico e uma carga horária específica
curso3: Curso = Curso(nome='Orquestração de Containers com Kubernetes', carga_horaria=23)

# Imprime o dicionário interno (__dict__) do objeto curso1
print(curso1.__dict__)
# Imprime o dicionário interno (__dict__) do objeto curso2
print(curso2.__dict__)
# Imprime o dicionário interno (__dict__) do objeto curso3
print(curso3.__dict__)

# ---------------------------------------------------------- #
# Atribui uma string ao nome 'nome'
nome: str = 'Mateus Marques'

# Atribui uma tupla de inteiros ao nome 'tupla'
tupla: Tuple = (1, 2, 3, 4, 5)

# Atribui uma lista de inteiros ao nome 'lista'
lista: List = [1, 2, 3, 4, 5]

# Imprime os primeiros 4 elementos de cada variável
print(nome[:4], tupla[:4], lista[:4])

# ---------------------------------------------------------- #