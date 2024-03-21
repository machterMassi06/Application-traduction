import pyttsx3
import os

def lire_texte_a_voix(texte, lg='fr'):  
    try:
        engine = pyttsx3.init()
        
        engine.setProperty('rate', 220) 
        engine.setProperty('voice', lg)  
        engine.say(texte)
        engine.runAndWait()
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


