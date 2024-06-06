
class Singleton:
    # Atributo de classe para armazenar a instância única
    __instance = None

    def __init__(self):
        # Método __init__ é chamado quando uma nova instância é criada
        if not Singleton.__instance:
            # Se __instance ainda não foi criada, imprime esta mensagem
            print('O método __init__ foi chamado...')
        else:
            # Se __instance já foi criada, imprime a instância existente
            print(f'A instância já foi criada: {self.get_instance()}')

    # O decorador @classmethod indica que get_instance é um método de classe
    @classmethod
    def get_instance(cls):
        # Método de classe para obter a instância única
        if not cls.__instance:
            # Se __instance ainda não foi criada, cria uma nova instância
            cls.__instance = Singleton()
        # Retorna a instância única
        return cls.__instance
    
# Cria uma instância de Singleton, o método __init__ será chamado
s1 = Singleton()

# Imprime a instância única obtida através do método get_instance
print(f'O objeto foi criado agora: {Singleton.get_instance()}')

# Cria outra instância de Singleton, mas como a instância já foi criada, o método __init__ não criará uma nova
s2 = Singleton()
