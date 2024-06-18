class SanidadeCheck:

    # Atributo de classe que armazenará a única instância da classe
    __instance = None

    # Método especial __new__ para controlar a criação de instâncias
    def __new__(cls, *args, **kwargs):
        # Se não houver uma instância existente, cria uma nova instância
        if not SanidadeCheck.__instance:
            SanidadeCheck.__instance = super(SanidadeCheck, cls).__new__(cls, *args, **kwargs)
        # Retorna a instância existente (ou recém-criada)
        return SanidadeCheck.__instance 

    # Método __init__ para inicializar os atributos da instância
    def __init__(self):
        # Inicializa o atributo privado __servidores como um dicionário vazio
        self.__servidores = []

    # Método para checar o status de um servidor específico
    def checar_servidor(self, srv):
        print(f'Checando o {self.__servidores[srv]}')

    # Método para adicionar servidores à lista
    def add_servidor(self):
        self.__servidores.append('Servidor 1')
        self.__servidores.append('Servidor 2')
        self.__servidores.append('Servidor 3')
        self.__servidores.append('Servidor 4')

    # Método para modificar a lista de servidores
    def mudar_servidor(self):
        self.__servidores.pop()
        self.__servidores.append('Servidor 5')

# Criação de duas instâncias da classe SanidadeCheck
sc1 = SanidadeCheck()
sc2 = SanidadeCheck()

# Adiciona servidores à instância sc1
sc1.add_servidor()
print('Cronograma de checagem de sanidade dos servidores A...')

# Checa o status de cada servidor na instância sc1
for srv in range(4):
    sc1.checar_servidor(srv)

# Modifica a lista de servidores na instância sc2
sc2.mudar_servidor()
print('Cronograma de checagem de sanidade dos servidores B...')

# Checa o status de cada servidor na instância sc2
for srv in range(4):
    sc2.checar_servidor(srv)
