class Strumento:
    def __init__(self, codice, tipo, marca, annoAcquisto, valore):
        self.codice = codice
        self.tipo = tipo
        self.marca = marca
        self.annoAcquisto = annoAcquisto
        self.valore = valore
    def __str__(self):
        return (f"Codice: {self.codice} - Tipo: {self.tipo} - Marca: {self.marca} "
                f"- Anno di acquisto: {self.annoAcquisto} - Valore: {self.valore}")


