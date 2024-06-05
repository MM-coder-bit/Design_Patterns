


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            print(f'Foi Criado o Objeto {cls.instance}')
        return cls.instance

sl = Singleton()
print(f'Instância 1: {id(sl)}')

s2 = Singleton()
print(f'Instância 2: {id(s2)}')
