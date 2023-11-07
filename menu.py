from leitor import Leitor

class Menu:
    def __init__(self):
        self.k:int
        self.teste:list
        self.opcoes()
    
    def opcoes(self):
        escolha = input("Qual teste executar:\n1) Teste 1\n2) Teste 2\n3) Teste 3\n> ")
        match int(escolha):
            case 1: leitor = Leitor("teste1")                
            case 2: leitor = Leitor("teste2") 
            case 3: leitor = Leitor("teste3") 
        
        self.teste = leitor.teste
        self.k = leitor.k

    
    