# traduction.py
from mtranslate import translate

def traduire_texte(txt, l_source, l_cible):
    try:
        return translate(txt, l_cible, l_source)
    except Exception as e:
        return f"Erreur de traduction : {str(e)}"
