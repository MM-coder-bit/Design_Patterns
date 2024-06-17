import sqlite3  # Importa o módulo sqlite3 para interagir com bancos de dados SQLite.

# Definição de uma metaclasse Singleton para garantir que apenas uma instância de uma classe seja criada.
class Singleton(type):

    # Dicionário para armazenar instâncias criadas.
    __instances = {}

    # Método especial __call__ para controlar a criação de instâncias.
    def __call__(cls, *args, **kwargs):
        # Verifica se a classe já possui uma instância.
        if cls not in cls.__instances:
            # Se não houver, cria uma nova instância e armazena no dicionário.
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        # Retorna a instância existente.
        return cls.__instances[cls]
    
# Definição da classe Database que usará a metaclasse Singleton.
class Database(metaclass=Singleton):

    # Atributo de classe para armazenar a conexão.
    connection = None

    # Método para conectar ao banco de dados.
    def connect(self):
        # Verifica se já existe uma conexão.
        if self.connection is None:
            print(f'Não temos ainda uma conexão... vamos criá-la...')
            # Cria uma nova conexão ao banco de dados.
            self.connection = sqlite3.connect('my_database.db')
            # Cria um cursor para executar comandos SQL.
            self.cursor = self.connection.cursor()
        # Retorna o cursor da conexão.
        return self.cursor
    
# Cria uma conexão ao banco de dados.
db1 = Database().connect()

# Tenta criar outra conexão ao banco de dados, mas retornará a mesma conexão (singleton).
db2 = Database().connect()
