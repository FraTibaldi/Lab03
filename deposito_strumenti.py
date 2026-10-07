import csv
from strumento import Strumento
from operator import attrgetter
from prestito import Prestito
class DepositoStrumenti:

    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.listaStrumenti = []
        self.i = 0
        self.listaPrestiti = []

    def set_responsabile(self, nuovo_responsabile):
        self.responsabile = nuovo_responsabile

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""

        with open(file_path, "r") as filein:
            reader = csv.reader(filein, delimiter=",")
            self.listaStrumenti = []
            for line in reader:
                if not line:
                    continue
                codice = line[0]
                tipo = line[1]
                marca = line[2]
                annoAcquisto = int(line[3])
                valore = float(line[4])
                s = Strumento(codice, tipo, marca, annoAcquisto, valore)
                self.listaStrumenti.append(s)

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        if self.listaStrumenti:
            nuovoCodice = "S" + str(int(self.listaStrumenti[-1].codice[1:]) + 1)
        else:
            nuovoCodice = "S1"
        s = Strumento(nuovoCodice, tipo, marca, anno_acquisto, valore)
        self.listaStrumenti.append(s)
        return s

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        return sorted(self.listaStrumenti, key=attrgetter('marca'))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        if any(p.codiceStrumento == id_strumento for p in self.listaPrestiti):
            raise Exception("Strumento già in prestito")
        if not any(s.codice == id_strumento for s in self.listaStrumenti):
            raise Exception("Strumento non trovato nel sistema")
        self.i += 1
        pres = Prestito("P" + str(self.i), data, id_strumento, cognome_allievo)
        self.listaPrestiti.append(pres)
        return pres

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        if any(p.codicePrestito == id_prestito for p in self.listaPrestiti):
            self.listaPrestiti[:] = [p for p in self.listaPrestiti if p.codicePrestito != id_prestito]
        else:
            raise Exception("Prestito non trovato")

