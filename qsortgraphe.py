from random import randint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import axes3d
import matplotlib as mp
import numpy as np
import random

def inputs():
    a = []
    l = int(input("Taille de la liste = "))
    for e in range(0, l):
        e = int(input("élément à ajouter : "))
        a.append(e)
    print("fin d'entrée de données")
    return a, l

def splitlist(a, low, high):
    pivot = a[high]
    i = low-1
    
    for j in range(low, high):
        if a[j]<=pivot:
            i=i+1
            #print(i)
            (a[i], a[j]) = (a[j], a[i])   
        
            #print(i)
    (a[i + 1], a[high]) = (a[high], a[i + 1])
    
    return i+1
    

def qsort(a, low, high):
    if low < high:
        pi = splitlist(a, low, high)
        qsort(a, low, pi-1)
        qsort(a, pi+1, high)
        return a
    
def graphe(a, l):
    datasetName ='User Datas'
    
    generator = qsort(a, 0, len(a) - 1)
    algoName = "Quick sort"
    plt.style.use('fivethirtyeight')
    
    data_normalizer = mp.colors.Normalize()
    color_map = mp.colors.LinearSegmentedColormap(
        "my_map",
        {
            "red": [(0, 1.0, 1.0),
                    (1.0, .5, .5)],
            "green": [(0, 0.5, 0.5),
                      (1.0, 0, 0)],
            "blue": [(0, 0.50, 0.5),
                     (1.0, 0, 0)]
        }
    )
    
    fig, ax = plt.subplots()
 
    bar_rects = ax.bar(range(len(a)), a, align ="edge",
                       color = color_map(data_normalizer(range(l))))
 
    ax.set_xlim(0, len(a))
    ax.set_ylim(0, int(1.1 * len(a)))
    ax.set_title("ALGORITHM : "+ algoName + "\n" + "DATA SET : " +
             datasetName, fontdict = {'fontsize': 13, 'fontweight':
                                      'medium', 'color' : '#E4365D'})
    text = ax.text(0.01, 0.95, "", transform = ax.transAxes, color = "#E4365D")
    iteration = [0]
    
    

    def animate(A, rects, iteration):
            for rect, a in zip(rects, A):
    
                rect.set_height(a)
            iteration[0] += 1
            text.set_text("iterations : {}".format(iteration[0]))

    anim = FuncAnimation(fig, func = animate, fargs = (bar_rects, iteration), frames = generator, interval = 50, repeat = False)
    
    plt.show()

    

def main():
    a, l = inputs()
    low = a[0]
    high = a[-1]
    print(low, high)
    qsort(a, 0, len(a) - 1)
    print(f"Liste triée : {a}")
    graphe(a, l)
    
    
if __name__ =="__main__":
    main()
    