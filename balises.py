# htmltags.py

# Décorateur pour appliquer la balise <b> (gras)
def html_bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

# Décorateur pour appliquer la balise <i> (italique)
def html_italics(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

# Décorateur pour appliquer la balise <u> (souligné)
def html_underline(func):
    def wrapper(*args, **kwargs):
        return f"<u>{func(*args, **kwargs)}</u>"
    return wrapper

# Décorateur générique pour appliquer une balise HTML spécifiée
def html_tag(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"
        return wrapper
    return decorator

# Tests des décorateurs

@html_bold
def text_bold():
    return "Texte en gras"

@html_italics
@html_bold
def text_bold_italic():
    return "Texte en gras et italique"

@html_underline
@html_italics
def text_italic_underline():
    return "Texte en italique et souligné"

@html_tag("b")
@html_tag("i")
@html_tag("u")
def text_custom_tags():
    return "Texte avec balises personnalisées"

# Exemples d'utilisation
if __name__ == "__main__":
    print(text_bold())                 # <b>Texte en gras</b>
    print(text_bold_italic())          # <i><b>Texte en gras et italique</b></i>
    print(text_italic_underline())     # <u><i>Texte en italique et souligné</i></u>
    print(text_custom_tags())          # <b><i><u>Texte avec balises personnalisées</u></i></b>
