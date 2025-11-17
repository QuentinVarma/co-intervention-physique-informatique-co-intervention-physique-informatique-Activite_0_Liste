#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Application de décodage de trame Ethernet

Cette application lit un fichier CSV contenant un signal d'oscilloscope,
le formate, décode le signal Manchester, puis extrait et affiche
les informations de la trame Ethernet (adresses MAC et type).
"""

from lecteurCSVOscillo import LecteurCSVOscillo
from formateurSignal import FormateurSignal
from decodeurManchester import DecodeurManchester
from decodeurEthernet import DecodeurEthernet


def main():
    """Fonction principale de l'application."""
    
    print("="*60)
    print("    APPLICATION DE DÉCODAGE DE TRAME ETHERNET")
    print("="*60)
    
    # Configuration
    CHEMIN_FICHIER = "T0005CH1_Tek.csv"
    DEBIT = 10e6  # 10 Mbps pour Ethernet 10BASE-T
    
    # Étape 1: Lecture du fichier CSV
    print("\n[1/5] Lecture du fichier CSV...")
    print("-" * 60)
    lecteur = LecteurCSVOscillo(CHEMIN_FICHIER)
    lecteur.charger_donnees(list, float)
    
    if not lecteur.donnees:
        print("\nErreur: Aucune donnée chargée. Vérifiez le chemin du fichier.")
        return
    
    # Étape 2: Formatage du signal
    print("\n[2/5] Formatage du signal...")
    print("-" * 60)
    formateur = FormateurSignal(lecteur.donnees, lecteur.intervalle_echantillon)
    formateur.supprimer_composante_continue()
    formateur.normalisation()
    formateur.aligner_debut_signal()
    donnees_formatees = formateur.mettre_en_forme()
    
    # Étape 3: Décodage Manchester
    print("\n[3/5] Décodage Manchester...")
    print("-" * 60)
    decodeur_manchester = DecodeurManchester(
        donnees_formatees,
        lecteur.intervalle_echantillon,
        DEBIT
    )
    trame_binaire = decodeur_manchester.decoder_donnees()
    trame_sans_preambule = decodeur_manchester.supprimer_preambule()
    
    # Étape 4: Extraction des champs Ethernet
    print("\n[4/5] Extraction des champs Ethernet...")
    print("-" * 60)
    decodeur_ethernet = DecodeurEthernet(trame_sans_preambule)
    decodeur_ethernet.extraire_champ(trame_sans_preambule)
    
    # Étape 5: Affichage des résultats
    print("\n[5/5] Affichage des résultats...")
    print("-" * 60)
    decodeur_ethernet.afficher_trame_complete()
    
    print("\nDécodage terminé avec succès!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterruption par l'utilisateur.")
    except Exception as e:
        print(f"\n\nErreur inattendue: {e}")
        import traceback
        traceback.print_exc()

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(port=9000)