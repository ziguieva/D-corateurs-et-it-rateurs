from typing import Iterable, Iterator, Tuple

# 1. Générateur group_by_pairs
def group_by_pairs(iterable: Iterable) -> Iterator[Tuple]:
    """Retourne les éléments de l'itérable groupés par paires avec chevauchement."""
    it = iter(iterable)
    prev = next(it)
    for current in it:
        yield (prev, current)
        prev = current

# 2. Générateur biz_generator
def biz_generator(iterable: Iterable) -> Iterator[int]:
    """
    Retourne uniquement les entiers entre 1 et 10, selon les règles suivantes :
    - L'itérable en entrée doit avoir au moins 3 éléments.
    - Ignorer le premier élément.
    - Retourner un multiple de 3 seulement s'il est précédé par un nombre pair.
    - Retourner un multiple de 4 seulement s'il est suivi par un nombre impair.
    """
    it = iter(iterable)
    buffer = []

    # Vérifier qu'il y a au moins 3 éléments et ignorer le premier
    try:
        next(it)  # Ignore le premier élément
        buffer = [next(it), next(it)]
    except StopIteration:
        return  # Fin si moins de 3 éléments

    # Parcours de l'itérable
    for current in it:
        if isinstance(buffer[1], int) and 1 <= buffer[1] <= 10:
            # Retourner un multiple de 3 s'il est précédé d'un nombre pair
            if buffer[1] % 3 == 0 and buffer[0] % 2 == 0:
                yield buffer[1]
            # Retourner un multiple de 4 s'il est suivi par un nombre impair
            elif buffer[1] % 4 == 0 and isinstance(current, int) and current % 2 != 0:
                yield buffer[1]
            # Retourner les entiers standards entre 1 et 10 qui ne sont ni multiples de 3 ni de 4
            elif buffer[1] % 3 != 0 and buffer[1] % 4 != 0:
                yield buffer[1]

        # Avancer la fenêtre de 2 éléments
        buffer[0], buffer[1] = buffer[1], current

# Exemples d'utilisation des générateurs
if __name__ == "__main__":
    # Exemple pour group_by_pairs
    print("Résultat de group_by_pairs:")
    for pair in group_by_pairs(range(5)):
        print(pair)  # Résultat attendu: (0, 1), (1, 2), (2, 3), (3, 4)

    # Exemple pour biz_generator
    print("\nRésultat de biz_generator:")
    for val in biz_generator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]):
        print(val)  # Filtrage selon les règles de biz_generator
