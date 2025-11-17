import csv
import numpy as np


class LecteurCSVOscillo:
  
    def __init__(self, chemin_fichier: str):

        self.chemin_fichier = chemin_fichier
        self.donnees = []
        self.intervalle_echantillon = 0.0
    
    def charger_donnees(self, np_array, float):

        CH1 = []
        t = []
        
        try:
            with open(self.chemin_fichier, 'r') as fichier:
                lecteur_csv = csv.reader(fichier)
                
                for ligne in lecteur_csv:
                    try:
                        t_val = float(ligne[0])
                        ch1_val = float(ligne[1])
                        t.append(t_val)
                        CH1.append(ch1_val)
                    except:
                        continue
            
            # Convertir en numpy arrays
            t = np.array(t)
            CH1 = np.array(CH1)
            
            # Calculer l'intervalle d'échantillonnage
            if len(t) > 1:
                self.intervalle_echantillon = t[1] - t[0]
            
            self.donnees = CH1
            
            print(f"Données chargées: {len(self.donnees)} échantillons")
            print(f"Intervalle d'échantillonnage: {self.intervalle_echantillon}s")
            
        except FileNotFoundError:
            print(f"Erreur: Fichier '{self.chemin_fichier}' introuvable.")
        except Exception as e:
            print(f"Erreur lors de la lecture du fichier: {e}")
