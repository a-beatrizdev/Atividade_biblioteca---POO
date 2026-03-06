# Classe base da biblioteca 
# Ela será herdada por Livro e Revista

class Itembiblioteca:
    def __init__(self, codigo: int, titulo: str, ano: int):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__disponivel = True
