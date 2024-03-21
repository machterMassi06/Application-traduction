import gradio as gr
import sys
sys.path.append("..")

from traduction import traduction
from vocale import vocale
from iso639 import languages
import tempfile

# Obtenez la liste des codes de langues
langues_disponibles = [(lang.name, lang.alpha2) for lang in languages if lang.alpha2 != ""]

def traduire_synthese_vocale(option, l_source, l_cible, texte):
    # Vérifiez si l'option est "Traduction et Synthèse Vocale" et que la longueur du texte est supérieure à 0
    if (option == "Traduction et Synthèse Vocale" or not option):
        text_traduit=traduction.traduire_texte(texte, l_source, l_cible).strip()
        return text_traduit,vocale.lire_texte_a_voix(text_traduit, l_cible)
    else:
        return traduction.traduire_texte(texte, l_source, l_cible)
def on_text_change(value):
    option = iface.components["Radio"].value
    l_source = iface.components["Dropdown"].value
    l_cible = iface.components["Dropdown_2"].value
    texte = value
    traduire_synthese_vocale(option, l_source, l_cible, texte)

iface = gr.Interface(
    fn=traduire_synthese_vocale,
    inputs=[
        gr.Radio(choices=["Traduction et Synthèse Vocale", "Juste Traduction"], label="Choisissez une option"),
        gr.Dropdown(langues_disponibles, label="Sélectionnez la langue source"),
        gr.Dropdown(langues_disponibles, label="Sélectionnez la langue cible"),
        gr.Textbox(placeholder="Entrez le texte", label="Texte à traduire ou synthétiser", type="text")
    ],
    outputs=gr.HTML(),
    title="Traduction et Synthèse Vocale",
    description="Choisissez une option, sélectionnez la langue source et la langue cible, puis entrez le texte à traduire ou synthétiser."
)

# Observer les modifications du texte
def lancement_interface():
    iface.launch(inbrowser=True)
    iface.add_observer(on_text_change, "Textbox")






