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

def mergesort(a):
    """
    Effectue un Merge Sort sur la liste a

    Args :
        -a

    Returns :
        -a (sorted)
    """
    if len(a)>1:
        mid = len(a)//2
        l = a[:mid]
        r = a[mid:]
        mergesort(l)
        mergesort(r)
        
        i = j = k = 0
        
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                a[k] = l[i]
                i+=1
            else:
                a[k] = r[j]
                j+=1
            k+=1
        
        while i < len(l):
            a[k] = l[i]
            i+=1
            k+=1
        
        while j < len(r):
            a[k] = r[j]
            j+=1
            k+=1

def main():
    """
    Demande à l'utilisateur s'il veut rentrer une liste à la 
    main ou si il veut en générer un dans un ordre aléatoire.
    
    Ensuite la fonction exécute un merge sort sur cette même liste.
    """
    print("     __  __                                      _   ")
    print("    |  \/  |                                    | |  ")
    print("    | \  / | ___ _ __ __ _  ___   ___  ___  _ __| |_ ")
    print("    | |\/| |/ _ \ '__/ _` |/ _ \ / __|/ _ \| '__| __|")
    print("    | |  | |  __/ | | (_| |  __/ \__ \ (_) | |  | |_ ")
    print("    |_|  |_|\___|_|  \__, |\___| |___/\___/|_|   \__|")
    print("                      __/ |                          ")
    print("                     |___/                         \n")
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
    start = time.perf_counter()
    mergesort(a)
    end = time.perf_counter()
    elapsed = end - start
    print(f"Liste triée : {a}")
    print(f'Temps de tri : {elapsed:.2}ms \n')

if __name__ =="__main__":
    main()