def memoized(func):
    # Dictionnaire pour stocker les résultats déjà calculés
    cache = {}

    def wrapper(*args):
        # Vérifier si le résultat existe déjà pour ces arguments
        if args in cache:
            return cache[args]
        else:
            # Calculer, stocker et retourner le résultat
            result = func(*args)
            cache[args] = result
            return result

    return wrapper

# Test du décorateur avec des fonctions de factorielle et de Fibonacci

# Factorielle sans mémorisation
def factorial_without_memoization(n):
    if n in (0, 1):
        return 1
    return n * factorial_without_memoization(n - 1)

# Factorielle avec mémorisation
@memoized
def factorial_with_memoization(n):
    if n in (0, 1):
        return 1
    return n * factorial_with_memoization(n - 1)

# Fibonacci sans mémorisation
def fibonacci_without_memoization(n):
    if n in (0, 1):
        return n
    return fibonacci_without_memoization(n - 1) + fibonacci_without_memoization(n - 2)

# Fibonacci avec mémorisation
@memoized
def fibonacci_with_memoization(n):
    if n in (0, 1):
        return n
    return fibonacci_with_memoization(n - 1) + fibonacci_with_memoization(n - 2)

# Exemple d'utilisation pour vérifier les performances
if __name__ == "__main__":
    import time

    # Test des performances sans et avec mémorisation pour la factorielle
    N = 35
    start = time.time()
    print(f"Factorielle sans mémorisation: {factorial_without_memoization(N)}")
    print(f"Temps sans mémorisation: {time.time() - start} secondes")

    start = time.time()
    print(f"Factorielle avec mémorisation: {factorial_with_memoization(N)}")
    print(f"Temps avec mémorisation: {time.time() - start} secondes")

    # Test des performances sans et avec mémorisation pour Fibonacci
    M = 35
    start = time.time()
    print(f"Fibonacci sans mémorisation: {fibonacci_without_memoization(M)}")
    print(f"Temps sans mémorisation: {time.time() - start} secondes")

    start = time.time()
    print(f"Fibonacci avec mémorisation: {fibonacci_with_memoization(M)}")
    print(f"Temps avec mémorisation: {time.time() - start} secondes")
