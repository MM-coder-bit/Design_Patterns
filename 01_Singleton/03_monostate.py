class Monostate:
    # Atributo de classe que armazena o estado compartilhado
    __estado = {}

    def __new__(cls, *args, **kwargs):
        # Cria uma nova instância da classe
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        # Define o dicionário de atributos da instância para referenciar o estado compartilhado
        obj.__dict__ = cls.__estado
        return obj

# Cria a primeira instância de Monostate
m1 = Monostate()
print(f'M1 ID: {id(m1)}')  # Imprime o ID da instância m1
print(m1.__dict__)  # Imprime o dicionário de atributos da instância m1

# Cria a segunda instância de Monostate
m2 = Monostate()
print(f'M2 ID: {id(m2)}')  # Imprime o ID da instância m2
print(m2.__dict__)  # Imprime o dicionário de atributos da instância m2

# Modifica o estado compartilhado através da instância m1
m1.nome = 'Mateus Marques'

# Imprime o dicionário de atributos das instâncias m1 e m2
print(f'M1: {m1.__dict__}')
print(f'M2: {m2.__dict__}')
