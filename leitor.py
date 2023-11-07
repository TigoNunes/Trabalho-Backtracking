class Leitor:
    def __init__(self, teste:str):
        with open(f"testes/{teste}.txt") as arquivo:
            dados = arquivo.read()
            filtro = dados.splitlines()
            self.teste = filtro[0].split(',')
            self.k = int(filtro[1])
            self.teste = [int(letra) for letra in self.teste]      
    
    