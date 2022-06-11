import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os
import numpy as np
from PIL import Image
import random as rd
os.chdir("U:\Downloads\jeu")

rouge = Image.open(r"rouge.png")
jaune = Image.open(r"jaune.png")
board = Image.open(r"tableau.png")



Jeu = np.zeros((6,7))



## fonction insertion
# Fonctionement : en lançant la fonction on insere dans le tableau A un chiffre determiné par l'entier a ici. La fonction va d'abord demander a quelle colonne on veut placer la piece.



def insertion(A,a):
    print("choisir la colonne ou l'on veut placer la pièce")
    n = input()
    n = int(n)
    if A[5,n] == 0:
        A[5,n] = a
        return
    for i in range(6):
        if A[i,n] != 0:
            A[i-1,n] = a
            break

def insertionb(A,a,n):
    n = int(n)
    if A[5,n] == 0:
        A[5,n] = a
        return
    for i in range(6):
        if A[i,n] != 0:
            A[i-1,n] = a
            break


## prérequis pour la fonction gagner
def inversion(A):
    L = []
    for i in range(len(A)):
        L.append(A[len(A)-1-i])
    return(L)

def gagnerligne(A):
    for i in range(6):
        k = 0
        l = 0
        for j in range(6):
            if A[i,j]== A[i,j+1]==1:
                k =k+1
                if k >= 3:
                    return(True,1)
            elif A[i,j]== A[i,j+1]==2:
                l= l+1
                if l>= 3:
                    return((True,2))
            else:
                k = 0
    return((False,False))

def gagnercolonne(A):
    for j in range(6):
        k = 0
        l = 0
        for i in range(5):
            if A[i,j]== A[i+1,j]==1:
                k =k+1
                if k >= 3:
                    return((True,1))
            elif A[i,j]== A[i+1,j]==2:
                l =l+1
                if l >= 3:
                    return((True,2))
            else:
                k = 0
    return((False,False))

def diag1(A):
    K = []
    M = []
    for p in range(7):
        R = []
        r = 0
        while p + r <= 6 and r<6:
            R.append(A[r,p+r])
            r =r +1
        K.append(R)
    for i in range(6):
        R=[]
        j= 0
        while i + j <= 5:
            R.append(A[i+j,j])
            j = j + 1
        M.append(R)
    M=inversion(M)
    M.pop()
    return(M+K)

def diag2(A):
    K =[]
    M=[]
    for p in range(7):
        R = []
        r = 0
        while p + r <= 6 and r<6:
            R.append(A[5-r,p+r])
            r =r +1
        K.append(R)
    for i in range(6):
        R=[]
        j= 0
        while i-j >=0:
            R.append(A[i-j,j])
            j = j + 1
        M.append(R)
    M.pop()
    return(M+K)

def gagnerdiag2(A):
    A = diag2(A)
    for i in range(len(A)):
        k = 0
        l = 0
        for j in range(len(A[i])-1):
            if A[i][j]== A[i][j+1]==1:
                k =k+1
                if k >= 3:
                    return((True,1))
            elif A[i][j]== A[i][j+1]==2:
                l = l+1
                if l >= 3:
                    return((True,2))
    return((False,False))

def gagnerdiag1(A):
    A = diag1(A)
    for i in range(len(A)):
        k = 0
        l = 0
        for j in range(len(A[i])-1):
            if A[i][j]== A[i][j+1]==1:
                k =k+1
                if k >= 3:
                    return((True,1))
            elif A[i][j]== A[i][j+1]==2:
                l = l +1
                if l >= 3:
                    return((True,2))
    return((False,False))

## fonction gagner
# gagner(A) retourne True si on a une situation gagnante False sinon
def gagner(A):
    (a,b) = gagnerligne(A)
    (c,d) = gagnercolonne(A)
    (x,y) = gagnerdiag1(A)
    (w,t) = gagnerdiag2(A)

    if a == True:
        return((True,b))
    elif c == True:
        return((True,d))
    elif x == True:
        return((True,y))
    elif w == True:
        return((True,t))
    else:
        return((False,0))

## fonction affichage

def tracer(A):
    pas = 170
    rouge = Image.open(r"rouge.png")
    jaune = Image.open(r"jaune.png")
    board = Image.open(r"tableau.png")
    for i in range(len(A)):
        for j in range(len(A)):
            if  A[i][j] == 1:
                board.paste(rouge,(66+ (j)*pas,890-(5-i)*pas))
            elif  A[i][j] == 2:
                board.paste(jaune,(66+ j*pas,890-(5-i)*pas))
    plt.imshow(board)
    plt.draw()


## Jeu


def Jeu1v1():
    while gagner(Jeu)==(False,0):
        print("Joueur 1")
        insertion(Jeu,1)
        print(Jeu)
        tracer(Jeu)
        plt.pause(0.01)
        (a,b) = gagner(Jeu)
        if a==True:
            break
        print("Joueur 2")
        insertion(Jeu,2)
        print(Jeu)
        tracer(Jeu)
        plt.pause(0.01)
    a = str("Joueur ") + str(int(gagner(Jeu)[1])) + str(" à gagné")
    return(a)


