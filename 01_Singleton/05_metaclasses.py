# Definindo a metaclasse MetaSingleton que herda de 'type'
class MetaSingleton(type):
    # Dicionário privado para armazenar instâncias únicas
    __instances = {}

    # Sobrescrevendo o método __call__, que é chamado quando uma instância da classe é criada
    def __call__(cls, *args, **kwargs):
        # Se a classe não tiver uma instância armazenada no dicionário, crie uma nova instância
        if cls not in cls.__instances:
            cls.__instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        # Retorna a instância armazenada, garantindo que sempre será a mesma
        return cls.__instances[cls]

# Definindo a classe Logger que utiliza a metaclasse MetaSingleton
class Logger(metaclass=MetaSingleton):
    pass

# Criando a primeira instância da classe Logger
log1 = Logger()
# Imprimindo o identificador único (endereço na memória) da instância log1
print(f'Log 1: {id(log1)}')

# Criando a segunda instância da classe Logger
log2 = Logger()
# Imprimindo o identificador único (endereço na memória) da instância log2
print(f'Log 2: {id(log2)}')
