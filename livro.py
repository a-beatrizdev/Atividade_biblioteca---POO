from item_biblioteca import Itembiblioteca 

class Livro(Itembiblioteca):
    def __init__(self, codigo, titulo, ano,autor, num_paginas):
        super().__init__(codigo, titulo, ano)
        self.__autor = autor
        self.__num_paginas = num_paginas
