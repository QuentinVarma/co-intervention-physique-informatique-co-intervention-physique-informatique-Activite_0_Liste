class DecodeurEthernet:
    
    def __init__(self, trame_decodee: str):
        
        self.trame_decodee = trame_decodee
        self.trame_sans_SFD = ""
        self.mac_dest_bin = ""
        self.mac_src_bin = ""
        self.type_bin = ""
    
    def extraire_champ(self, champ_sans_SFD: str) -> None:
        
        self.trame_sans_SFD = champ_sans_SFD
        
        if len(self.trame_sans_SFD) < 112:  # 48 + 48 + 16 = 112 bits minimum
            print("Erreur: Trame trop courte")
            return
        
        # Extraction des champs
        self.mac_dest_bin = self.trame_sans_SFD[0:48]
        self.mac_src_bin = self.trame_sans_SFD[48:96]
        self.type_bin = self.trame_sans_SFD[96:112]
        
        print("Champs extraits avec succès")
    
    def afficher_mac(self) -> None:
        print("\n=== ADRESSES MAC ===")
        
        # MAC destination
        mac_dest_hex = self._binaire_vers_mac(self.mac_dest_bin)
        print(f"MAC Destination: {mac_dest_hex}")
        
        # MAC source
        mac_src_hex = self._binaire_vers_mac(self.mac_src_bin)
        print(f"MAC Source:      {mac_src_hex}")
    
    def afficher_type(self) -> None:
        if not self.type_bin:
            return
        
        type_hex = hex(int(self.type_bin, 2))[2:].upper().zfill(4)
        type_decimal = int(self.type_bin, 2)
        
        print("\n=== TYPE/LONGUEUR ===")
        print(f"Type: 0x{type_hex} ({type_decimal})")
        
        # Interprétation courante
        types_courants = {
            0x0800: "IPv4",
            0x0806: "ARP",
            0x86DD: "IPv6",
            0x8100: "VLAN"
        }
        
        if type_decimal in types_courants:
            print(f"Protocol: {types_courants[type_decimal]}")
    
    def _binaire_vers_mac(self, mac_bin: str) -> str:

        if len(mac_bin) != 48:
            return "MAC invalide"
        
        # Convertir par groupes de 8 bits (1 octet)
        octets = []
        for i in range(0, 48, 8):
            octet_bin = mac_bin[i:i+8]
            octet_hex = hex(int(octet_bin, 2))[2:].upper().zfill(2)
            octets.append(octet_hex)
        
        return ":".join(octets)
    
    def afficher_trame_complete(self) -> None:
        """Affiche tous les détails de la trame."""
        print("\n" + "="*50)
        print("        DÉCODAGE TRAME ETHERNET")
        print("="*50)
        
        self.afficher_mac()
        self.afficher_type()
        
        print("\n" + "="*50)