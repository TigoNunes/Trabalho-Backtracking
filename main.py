from menu import Menu
menu = Menu()
teste = menu.teste
k = menu.k

# Força Bruta#####################################################
def forca_bruta(teste, k):
    # TODO: Colocar marcadores de tempo
    for i in range(len(teste) - 1):
        for j in range(i+1, len(teste)):
            save = j
            res = teste[i] + teste[j]
            sub_teste = [teste[i], teste[j]]
            while res < k:
                j += 1
                try:
                    res += teste[j]
                    sub_teste.append(teste[j])
                except IndexError:
                    res = 10000
                

            if res > k:
                print(f"falha\t{sub_teste}")
            else:
                print(f"ACHADO\t{sub_teste}")
                
            j = save

# Backtracking####################################################

def backtrackin(teste,k):
    # TODO: Fazer o código 
    # TODO: Marcadores de tempo
    pass

forca_bruta(teste,k)
