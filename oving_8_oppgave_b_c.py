# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 09:23:12 2021

@author: Erlend Tøssebro
"""

class Sporsmaal:
    def __init__(self, sporsmaal, alternativer, korrekt_svar=0):
        self.sporsmaal = sporsmaal
        self.alternativer = alternativer
        self.korrekt_svar = korrekt_svar
        
    def __str__(self):
        resultat = self.sporsmaal + "\nSvaralternativer:\n"
        for index, verdi in enumerate(self.alternativer):
            resultat += f"{index}: {verdi}\n"
        return resultat
    
    def sjekk_svar(self, svaret):
        if svaret == self.korrekt_svar:
            return True
        else:
            return False
        

if __name__ == "__main__":
    sp1 = Sporsmaal("Hva heter hovedstaden i Sverige?", ["Oslo", "Stockholm", "Göteborg", "Norge"], 1)
    sp2 = Sporsmaal("Hva er det største universitetet i Norge?", ["UiO", "UiS", "NTNU", "UiB", "UiT"], 2)
    print("Spørsmål 1: ")
    print(sp1)
    svar = int(input("Ditt svar: "))
    if sp1.sjekk_svar(svar):
        print("Korrekt")
    else:
        print("Feil")
    print()
    print("Spørsmål 2: ")
    print(sp2)
    svar = int(input("Ditt svar: "))
    if sp2.sjekk_svar(svar):
        print("Korrekt")
    else:
        print("Feil")
    
