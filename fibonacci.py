"""
la suite de fibonacci
"""

# on optimise

# si cache ne fonctionne pas, remplacez par lru_cache
from functools import cache

@cache
def fibo_cached(n):
    """
    en cachant les résultats on arrive
    à une complexité linéaire
    """
    if n <= 1:
        return n
    else:
        return fibo_cached(n-1) + fibo_cached(n-2)
this is a new modification