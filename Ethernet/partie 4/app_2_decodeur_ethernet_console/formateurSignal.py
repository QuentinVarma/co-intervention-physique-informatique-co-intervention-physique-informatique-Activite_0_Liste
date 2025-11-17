import numpy as np


class FormateurSignal:

    def __init__(self, donnees, intervalle_echantillon: float):
        
        self.donnees = np.array(donnees)
        self.intervalle_echantillon = intervalle_echantillon
    
    def supprimer_composante_continue(self) -> None:
        """Supprime la composante continue du signal en soustrayant la moyenne."""
        if len(self.donnees) == 0:
            return
        
        moyenne = np.mean(self.donnees)
        self.donnees = self.donnees - moyenne
        print(f"Composante continue supprimée (moyenne: {moyenne:.4f}V)")
    
    def normalisation(self) -> None:
        """Normalise le signal entre -1 et 1."""
        if len(self.donnees) == 0:
            return
        
        max_abs = np.max(np.abs(self.donnees))
        if max_abs > 0:
            self.donnees = self.donnees / max_abs
        print("Signal normalisé")
    
    def aligner_debut_signal(self) -> None:
        if len(self.donnees) == 0:
            return
        
        seuil = -0.1
        i = 0
        
        while i < len(self.donnees) and self.donnees[i] > seuil:
            i += 1
        
        if i < len(self.donnees):
            self.donnees = self.donnees[i:]
            print(f"Signal aligné au début (échantillon {i})")
    
    def mettre_en_forme(self):
        
        if len(self.donnees) == 0:
            return []
        
        seuil = 0.1
        CH1_ideal = []
        
        for i in range(len(self.donnees)):
            if self.donnees[i] < seuil:
                CH1_ideal.append(-1)
            else:
                CH1_ideal.append(1)
        
        print(f"Signal mis en forme: {len(CH1_ideal)} échantillons")
        return CH1_ideal
