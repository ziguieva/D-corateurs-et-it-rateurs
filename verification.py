def typassert(*type_args):
    """Vérifie les types des arguments d'une fonction selon les types spécifiés dans type_args."""
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Vérification du nombre d'arguments
            if len(args) != len(type_args):
                raise TypeError("Le nombre d'arguments ne correspond pas aux types spécifiés.")

            # Vérification des types
            for i, (arg, expected_type) in enumerate(zip(args, type_args)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"L'argument {i+1} doit être de type {expected_type} mais a reçu {type(arg)}.")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Exemples d'utilisation

@typassert(int)
def f_int(val):
    return f"Valeur entière : {val}"

@typassert(float)
def f_float(val):
    return f"Valeur flottante : {val}"

@typassert(str, (int, float))
def f_str_number(s, number):
    return f"Chaîne : {s}, Nombre : {number}"

class A:
    pass

@typassert(A, A)
def f_A_A(a1, a2):
    return f"Instances de A : {a1}, {a2}"

# Tests des fonctions avec vérification de type
if __name__ == "__main__":
    # Exemples valides
    print(f_int(5))               # OK
    print(f_float(3.14))          # OK
    print(f_str_number("texte", 42))  # OK
    print(f_str_number("texte", 3.14)) # OK
    print(f_A_A(A(), A()))        # OK

    # Exemples invalides (décommentez pour tester les exceptions)
    # f_int("5")                   # Exception (str au lieu de int)
    # f_float(5)                   # Exception (int au lieu de float)
    # f_str_number("texte", "42")  # Exception (str au lieu de int ou float)
    # f_A_A(A(), "not A")          # Exception (str au lieu de instance de A)
