class Sporsmaal:
    
    
    
    def __init__(self, sporsmaal, korrekt_svar, alternativer):
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
        
    def sporsmaaltext(self):
        
        self.svrliste=list()
        fila=open("sporsmaalsfil.txt","r", encoding="UTF8")
        for linje in fila:
            self.svrliste.append(linje)
        return self.svrliste
    
    def korrekt_svar_text(self):
        return self.alternativer[self.korrekt_svar]
       
        
       
            
            
        
class Player:
    def __init__(self, navn,poengsum=0):
        self.navn=navn
        self.poengsum=poengsum
        
    def Spillere(self):
        self.spillere=list()
        antall=int(input("hvor mange spillere "))
        for i in range(0,antall):
            navnet=input("Hva heter du? ")
            self.spillere.append(navnet)
        return self.spillere
    
    def points(self,navn,poengsum):
        if navn in poengsum:
            poengsum[navn]=poengsum[navn]+1
        else:
            poengsum[navn]=1
        return poengsum
        
        
if __name__ == "__main__":
    lpoints=dict()
    
    deltakere=Player(0,0).Spillere()
    sprsm=Sporsmaal(0,0,0).sporsmaaltext()
    for linje in sprsm:
         b=linje.split(":")
         c=b[2].split(",")
         svr=Sporsmaal(b[0],int(b[1]),c)
         print(svr)
         m=list()
         for spillere in deltakere:
             m.append(0)
             
         for spiller in deltakere:
                svar=int(input(f"velg ett alternativ: {spiller}->"))
                if svr.sjekk_svar(svar):
                    lpoints=Player(spiller).points(spiller,lpoints)
                    m[deltakere.index(spiller)]=1
                else:
                    m[deltakere.index(spiller)]=0
         print()     
         print(f" korekt svar er: {svr.korrekt_svar_text()}")
         
         
         for spiller in deltakere:
             if m[deltakere.index(spiller)]==1:
                 print(f"{spiller} har svart riktig")
             else:
                 print(f"{spiller} har svart feil")
             
    print()       
    for spiller in deltakere:
            print(f"{spiller} har {lpoints[spiller]} points")
            
    vinner=max(lpoints,key=lpoints.get)
    print(f" vinneren er {vinner}")   
