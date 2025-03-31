
class Carta :
    def __init__(self, id, nombre, AP, AT, PD, MD, flechas):
        self.id = id
        self.nombre = nombre
        self.AP = AP  # ataque físico
        self.AT = AT  # ataque tipo
        self.PD = PD # defensa física
        self.MD = MD # defensa mágica
        self.flechas = flechas # flechas en las esquinas

    def __str__(self):
        return f"({self.id}) {self.nombre} (AP: {self.AP}, AT: {self.AT}, PD: {self.PD}, MD: {self.MD}, Flechas: {self.flechas})" 
    
    def __repr__(self):
        return f"({self.id}) {self.nombre} (AP: {self.AP}, AT: {self.AT}, PD: {self.PD}, MD: {self.MD}, Flechas: {self.flechas})"
    
    