import os
import random
from tkinter.constants import END

# Global variable

matriz = []
sele = []
k = 3

#Game

def machine(): # backtracking: evaluation all posivilitys.
    for i in range(0,9):
        if move(i, 2):
            if win(2):
                return i
            matriz[i] = 0
            sele.append(i)
    
    for i in range(0,9):
        if move(i, 1):
            if win(1):
                matriz[i] = 2
                return i
            matriz[i] = 0
            sele.append(i)
    
    
    i = random.choice(sele)
    if move(i, 2): # if don't see any win movemet, move aleatority. 
        return i

def move(i, jugador): # see if the movement is correct.
    if matriz[i] == 0: 
        matriz[i] = jugador
        sele.remove(i)
        return True
    else:
        return False
   
def win(player):  # Evaluate the move, and see if  it is winner.
    for i in range(0,k):
        # rows
        cont = 0
        for j in range(0,k):
            if matriz[(i*k)+j] == player:
                cont += 1
        if cont == k:
            return True
        # columns
        cont = 0
        for j in range(0,k):
            if matriz[i+(j*k)] == player:
                cont += 1
        if cont == k:
            return True
    #Diagonal 1
    cont = 0
    for j in range(0,k):
        if matriz[j*(k+1)] == player:
            cont += 1
    if cont == k:
        return True
    # Diagonal 2
    cont = 0
    for j in range(0,k):
        if matriz[k-1 + j*(k-1)] == player:
            cont += 1
    if cont == k:
        return True
    
    return False

def again(): # Reset all global variables
    global matriz, sele
    matriz.clear()
    sele.clear()
    for i in range(0,k*k):
        matriz.append(0)
        sele.append(i)



