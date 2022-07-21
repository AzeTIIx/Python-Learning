import random
from random import randint
import time


def inputs():
    """
    Fonction qui demande à l'utilisateur quelle est 
    la taille de la liste qu'il veut entrer, ainsi que les membres
    de la liste
    
    Inputs :
        -a[e]
        -l
    Return :
        -a
        -l
    """
    a = []
    l = int(input("Taille de la liste = "))
    for e in range(0, l):
        e = int(input("élément à ajouter : "))
        a.append(e)
    print("fin d'entrée de données")
    return a, l


def rand():
    """
    Fonction qui demande à l'utilisateur la taille de 
    la liste qu'il veut générer.
    
    Inputs : 
        -n 
    Return : 
        -a
    """
    

    n = int(input("Entrez la taille de la liste\n"))
    a = []
    for i in range(0, n):
        e = random.randint(1, n)
        a.append(e)
    print("Liste non triée : {0}\n" .format(a))
    return a


def splitlist(a, low, high):
    """
    Effectue une section de la liste "a" par la droite (pivot = membre 
    de la liste le plus haut)

    Args :
        -a 
        -low
        -high

    Returns :
        -index + 1 
    """
    pivot = a[high]
    i = low-1
    
    for j in range(low, high):
        if a[j]<=pivot:
            i=i+1

            (a[i], a[j]) = (a[j], a[i])   

    (a[i + 1], a[high]) = (a[high], a[i + 1])
    
    return i+1
    

def qsort(a, low, high):
    """
    Effectue un Quick Sort sur la liste a

    Args :
        -a
        -low
        -high 

    Returns :
        -a (sorted)
    """
    
    if low < high:
        pi = splitlist(a, low, high)
        qsort(a, low, pi-1)
        qsort(a, pi+1, high)
        return a

    
        

    

def main():
    """
    Demande à l'utilisateur s'il veut rentrer une liste à la 
    main ou si il veut en générer un dans un ordre aléatoire.
    
    Ensuite la fonction exécute un qsort sur cette même liste.
    """
    print("  ____   _____  ____  _____ _______ \n / __ \ / ____|/ __ \|  __ \__   __|\n| |  | | (___ | |  | | |__) | | |\n| |  | |\___ \| |  | |  _  /  | |\n| |__| |____) | |__| | | \ \  | |\n \___\_\_____/ \____/|_|  \_\ |_|\n")
    ans = input("Vous voulez entrer des nombres (1) ou les générer aléatoirement (2) ?")
    if ans == '1':
        a, l = inputs()
    elif ans =='2':
        start = time.perf_counter()
        a = rand()
        end = time.perf_counter()
        elapsed = end - start
        print(f'Temps de génération : {elapsed:.2}ms \n')
    else :
        print("Entrez une valeure valide (1 ou 2).")
        exit(0)
    low = a[0]
    high = a[-1]
    start = time.perf_counter()
    qsort(a, 0, len(a) - 1)
    end = time.perf_counter()
    elapsed = end - start
    print(f"Liste triée : {a}")
    print(f'Temps de tri : {elapsed:.2}ms \n')
    
    
    
if __name__ =="__main__":
    main()