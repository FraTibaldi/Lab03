class Prestito:
    def __init__(self, codicePrestito, data, codiceStrumento, cognomeAllievo):
        self.codicePrestito = codicePrestito
        self.data = data
        self.codiceStrumento = codiceStrumento
        self.cognomeAllievo = cognomeAllievo

    def __str__(self):
        return (f"Codice del prestito: {self.codicePrestito} - Data del prestito: {self.data} - "
                f"Codice dello Strumento: {self.codiceStrumento} - Cognome Allievo: {self.cognomeAllievo}")
