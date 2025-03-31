class BatallaCartas:
    def __init__(self, cartaA, cartaB):
        self.cartaA = cartaA
        self.cartaB = cartaB

    def calcular_carta_ganadora(self):
        # fase 1: Calcula el ataque real de la carta A
        self.cartaA.ataque_real = self.cartaA.fase1()
        # fase 2: Calcula la defensa real de la carta B
        self.cartaB.defensa_real = self.cartaB.fase2()
        return 0
    
    def cartaA_fase1(self):
        # fase 1: Calcula el ataque real de la carta A
        return 0
    
    def cartaA_fase2(self):
        # fase 2: Calcula el ataque real de la carta A
        return 0


    def cartaB_fase1(self):
        # fase 1: Calcula la defensa real de la carta B
        return 0
    
    