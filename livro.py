from item_biblioteca import Itembiblioteca 

class Livro(Itembiblioteca):
    def __init__(self, codigo, titulo, ano,autor, num_paginas):
        super().__init__(codigo, titulo, ano)
        self.__autor = autor
        self.__num_paginas = num_paginas

    def get_autor(self):
        return self.__autor
    
    def get_num_paginas(self):
        return self.__num_paginas
    
    def set_autor(self, novo_autor):
        if novo_autor:
            self.__autor = novo_autor
        else:
            raise ValueError("O nome do autor não pode ficar vazio")
    
    def set_num_paginas(self, novo_num_paginas):
        if novo_num_paginas:
            self.__num_paginas = novo_num_paginas
        else:
            raise ValueError("O número de paginas tem que ser maior que zero")
    
    def exibir_detalhes(self):
        status = "Disponível" if self.get_disponivel() else "Emprestado"
        print(f"[Livro] Código: {self.get_codigo()} | Título: {self.get_titulo()} | "
              f"Ano: {self.get_ano()} | Autor: {self.__autor} | "
              f"Páginas: {self.__num_paginas} | Status: {status}")