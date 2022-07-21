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

def bubblesort(a):
    n = len(a)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                swapped = True
                (a[j], a[j+1]) = (a[j+1], a[j])
                
            
        if not swapped:
            return

def main():
    """
    Demande à l'utilisateur s'il veut rentrer une liste à la 
    main ou si il veut en générer un dans un ordre aléatoire.
    
    Ensuite la fonction exécute un bubble sur cette même liste.
    """
    print("  ____        _     _     _         _____            _   ")
    print(" |  _ \      | |   | |   | |       / ____|          | |  ")
    print(" | |_) |_   _| |__ | |__ | | ___  | (___   ___  _ __| |_ ")
    print(" |  _ <| | | | '_ \| '_ \| |/ _ \  \___ \ / _ \| '__| __|")
    print(" | |_) | |_| | |_) | |_) | |  __/  ____) | (_) | |  | |_ ")
    print(" |____/ \__,_|_.__/|_.__/|_|\___| |_____/ \___/|_|   \__|")
    print("                                                         ")
    print("                                                       \n")
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
    bubblesort(a)
    end = time.perf_counter()
    elapsed = end - start
    print(f"Liste triée : {a}")
    print(f'Temps de tri : {elapsed:.2}ms \n')
    
    
    
if __name__ =="__main__":
    main()