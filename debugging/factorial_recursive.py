#!/usr/bin/python3
import sys

def factorial(n):
    """
    Fonction qui calcule le factoriel d'un nombre donné de manière récursive.
    
    Paramètres:
    n (int): Le nombre pour lequel le factoriel doit être calculé.
    
    Retours:
    int: Le factoriel de n. Si n est 0, la fonction retourne 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# On récupère l'argument passé en ligne de commande et on le convertit en entier
f = factorial(int(sys.argv[1]))

# On affiche le résultat du calcul du factoriel
print(f)