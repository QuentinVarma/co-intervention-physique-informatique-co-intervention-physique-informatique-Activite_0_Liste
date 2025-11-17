import numpy as np


class DecodeurManchester:
    
    def __init__(self, np_array, intervalle_echantillon: float, debit: float):
        
        
        self.donnees = np_array
        self.intervalle_echantillon = intervalle_echantillon
        self.debit = debit
        # Calcul: N = Tb/Te = (1/debit) / intervalle_echantillon
        self.nbr_ech_bin = int(1 / (debit * intervalle_echantillon))
        self.trame_binaire = ""
        print(f"Nombre d'échantillons par bit: {self.nbr_ech_bin}")
    
    def decoder_donnees(self) -> str:
        
        if not self.donnees:
            return ""
        
        decode = ''
        i = 0
        N = self.nbr_ech_bin
        
        while i + N <= len(self.donnees):
            first_half = np.mean(self.donnees[i : i + N//2])
            second_half = np.mean(self.donnees[i + N//2 : i + N])

            if first_half > 0 and second_half < 0:
                decode += '0'
            elif first_half < 0 and second_half > 0:
                decode += '1'
            else:
                decode += '?'

            i += N
        
        self.trame_binaire = decode
        print(f"Décodage Manchester: {len(self.trame_binaire)} bits")
        return self.trame_binaire
    
    def supprimer_preambule(self) -> str:
        
        if not self.trame_binaire:
            return ""
        
        # Le SFD (Start Frame Delimiter) est "10101011" en Manchester
        sfd = "10101011"
        position_sfd = self.trame_binaire.find(sfd)
        
        if position_sfd != -1:
            # Retirer tout jusqu'au SFD inclus
            self.trame_binaire = self.trame_binaire[position_sfd + len(sfd):]
            print(f"Préambule supprimé (position SFD: {position_sfd})")
        else:
            print("Attention: SFD non trouvé")
        
        return self.trame_binaire