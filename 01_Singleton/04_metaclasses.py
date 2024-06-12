# Definindo a metaclasse University que herda de 'type'
class University(type):
    # Sobrescrevendo o método __call__, que é chamado quando uma instância da classe é criada
    def __call__(cls, *args, **kwargs):
        # Imprimindo os argumentos passados para a criação da instância
        print(f'Estes são os argumentos: {args}')
        # Chamando o método __call__ da classe 'type' para continuar a criação da instância
        return type.__call__(cls, *args, **kwargs)

# Definindo a classe Geek que utiliza a metaclasse University
class Geek(metaclass=University):
    # Método inicializador da classe Geek
    def __init__(self, valor1, valor2):
        # Atribuindo os valores recebidos aos atributos da instância
        self.valor1 = valor1
        self.valor2 = valor2

# Criando uma instância da classe Geek
# Isso acionará o método __call__ da metaclasse University
obj = Geek(42, 23)

# Imprimindo a instância criada
print(obj)
