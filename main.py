import itertools
from menu import Menu
menu = Menu()
teste = menu.teste
k = menu.k

# Força Bruta#####################################################
def forca_bruta(teste, k):
    conjuntos_de_subconjuntos = []
    for i in range(2, len(teste)-1):
        subconjuntos = list(itertools.combinations(teste, i))
        conjuntos_de_subconjuntos.append(subconjuntos[:])
    
    respostas = []
    for conjunto in conjuntos_de_subconjuntos:
        for sub in conjunto:
            res = sum(sub)
            if res == k:
                respostas.append(sub)                

    return respostas


# Backtracking####################################################

# def backtracking(teste,k, resultados:list, subconjuntos:list):
    
#     if len(teste) > 0:
#         if k - teste[0] > 0:
#             subconjuntos.append(teste[0])            
#             resultados.append(backtrackin(teste[1:], k - teste[0], resultados,subconjuntos))

#             # subconjuntos.pop(teste[0])
#             resultados.append(backtrackin(teste[1:], k, resultados, subconjuntos))

#         elif k - teste[0] < 0: # Se a conta der menos que k, algoritimo retorna
#             resultados.append(backtrackin(teste[1:], k, resultados, subconjuntos))
#         else: return subconjuntos.append(teste[0])
#     elif k > 0:
#         return []
#     else: return subconjuntos

#     # return resultados

def backtracking(numbers, target_sum):
    def backtrack(start, current_sum, current_subset):
        if current_sum == target_sum:
            subsets.append(current_subset[:])
            return
        if current_sum > target_sum or start == len(numbers):
            return
        for i in range(start, len(numbers)):
            current_subset.append(numbers[i])
            backtrack(i + 1, current_sum + numbers[i], current_subset)
            current_subset.pop()

    subsets = []
    backtrack(0, 0, [])
    return subsets
             
print(f"{forca_bruta(teste,k)}\n")

print(backtracking(teste, k))

