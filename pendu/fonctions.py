from donnees import *
import random

scores = {}

"""
    Choisit un mot au hasard dans la list de mots possibles    
"""
def pick_word(dic):
    global mot, a
    a = random.randint(0, len(dic)-1)
    mot = dic[a]
    a = list(mot.strip())
    #print(mot)
    return mot, a

def user_input(mot):
    global guess
    guess = input("Entrez une lettre : ")

def check():
    if guess in a:
        print("Trouvé !")
        return guess, True, a
    else :
        return guess, False, a

def show_word(a):
    w = []
    false_letters = []
    global coups

    for i in range(len(a)):
        w.append("_")
    #print(w)
    while "_" in w:
        user_input(mot)
        if check()[1] == True:
            index = [pos for pos, char in enumerate(mot) if char == guess]
            print("Position de la ou des lettres trouvée(s) : {0}" .format(index))
            for j in range(len(index)):
                w[index[j]] = guess
                j+=1
            print(w)
        else:
            false_letters.append(guess)
            coups = coups - 1
            f = [pos for pos, char in enumerate(false_letters) if char == guess]
            if coups==0:
                print(" ==========Y= ")
            if coups<=1:
                print(" ||/       |  ")
            if coups<=2:
                print(" ||        0  ")
            if coups<=3:
                print(" ||       /|\ ")
            if coups<=4:
                print(" ||       /|  ")
            if coups<=5:                    
                print(" ||           ")
            if coups<=6:                    
                print("/||           ")
            if coups<=7:
                print("==============\n")
            if len(f) > 1:
                del false_letters[-1]
                coups+=1
                print("Vous avez déjà essayer cette lettre !, il vous reste {0} erreurs possibles" .format(coups))
            print("Les lettres fausses déjà entrées sont : {0}" .format(false_letters))
            if coups == 0 :
                print("Vous avez perdus :( ")
                exit (0)
    print("Félicitations, vous avez gagner ! Le mot à trouver était {0}" .format(mot))
    name = str(input("Entrez votre pseudo : "))
    register(coups, name)
    

    
def register(coups, name):

    scores[name] = coups
    print("{0} a scorer {1} points !" .format(name, coups))

def main():
    pick_word(dic)
    show_word(a)
