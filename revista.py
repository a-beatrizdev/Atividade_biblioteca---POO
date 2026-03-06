from item_biblioteca import Itembiblioteca 

class Revista(Itembiblioteca):
    def __init__(self, codigo, titulo, ano, edicao, mes):
        super().__init__(codigo, titulo, ano)
        self.__edicao = edicao
        self.__mes = mes

    def get_edicao(self):
        return self.__edicao
    
    def get_mes(self):
        return self.__mes
    
    def set_edicao(self, edicao):
        if edicao:
            self.__edicao = edicao
        else:
            raise ValueError("Edição deve ser maior que zero")
    def set_mes(self, mes):
        if mes:
            self.__mes = mes
        else: 
            raise ValueError("O mês não pode ser vazio")
        
    def exibir_detalhes(self):
        status = "Disponível" if self.get_disponivel() else "Emprestado"
        print(f"[Revista] Código: {self.get_codigo()} | Título: {self.get_titulo()} | "
              f"Ano: {self.get_ano()} | Edição: {self.__edicao} | "
              f"Mês: {self.__mes} | Status: {status}")
        