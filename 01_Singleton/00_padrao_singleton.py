
class Singleton(object):
    # Método especial __new__ é chamado antes de __init__
    def __new__(cls):
        # Verifica se a classe já possui um atributo 'instance'
        if not hasattr(cls, 'instance'):
            # Se não houver 'instance', cria um novo objeto da classe Singleton
            cls.instance = super(Singleton, cls).__new__(cls)
            print(f'Foi Criado o Objeto {cls.instance}')
        # Retorna a instância única
        return cls.instance

# Cria a primeira instância de Singleton
sl = Singleton()
print(f'Instância 1: {id(sl)}')

# Cria a segunda instância de Singleton
s2 = Singleton()
print(f'Instância 2: {id(s2)}')

