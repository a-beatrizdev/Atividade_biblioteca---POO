# Classe base da biblioteca 
# Ela será herdada por Livro e Revista

class Itembiblioteca:
    def __init__(self, codigo: int, titulo: str, ano: int):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__disponivel = True

    def get_codigo(self):
        return self.__codigo
    
    def get_titulo(self):
        return self.__titulo
    
    def get_ano(self):
        return self.__ano
    
    def get_disponivel(self):
        return self.__disponivel 
    
    def set_codigo(self, novo_codigo):
        if novo_codigo:
            self.__codigo = novo_codigo
        else:
            raise ValueError("Código inválido")
        
    def set_titulo(self, novo_titulo):
        if novo_titulo.strip():
            self.__titulo = novo_titulo
        else:
            raise ValueError("Titulo não pode ser vazio")
        
    def set_ano(self, novo_ano):
        if novo_ano > 0:
            self.__ano = novo_ano
        else:
            raise ValueError("Ano deve ser maior que zero")
    
    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            print(f"ITem {self.__titulo} emprestado com sucesso. ")
        else:
            print(f"Item {self.__titulo} não encontrado")

    def devolver(self):
        self.__disponivel = True
        print(f"Item {self.__titulo} devolvido com sucesso.")

    def exibir_detalhes(self):
            raise NotImplementedError("Este método deve ser sobrescrito.")