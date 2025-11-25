import random
rugzak = []
afkortingen ={
    "ah":"albert heijn",
    "markt":"lokale markt",
    "stelen":"broden stelen",
    "kopen":"broodje kopen",
    "pakken":"stokbrood pakken"
}
ROOD = "\033[31;43m"
GROEN = "\033[32;40m"
BLAUW = "\033[34m"
RESET = "\033[0m"
print("Het spannende avontuur van Paladin en de Kip, schrijf telkens welke keuze u wilt maken.")
print("U hoeft niet op hoofdletters te letten en het doel is dat Paladin rustig kan eten")
print("Geschreven door Ruben Spithoven")

states= {
    "staat1":{
        "text": f"{GROEN}Paladin{RESET} wordt wakker met haar {ROOD}kip{RESET}, ze hebben honger. Gaan ze naar de lokale markt of naar de {BLAUW}albert heijn{RESET}?",
        "choices": {
            "lokale markt":"staat2",
            "albert heijn":"staat3"
            }
        },
    "staat2":{
        "text": f"Aangekomen bij de markt zien ze de kraam van de bakker. {GROEN}Paladin{RESET} heeft 1 euro bij haar. Gaan ze een broodje kopen, meerdere broden stelen of niks eten?",
        "choices": {
            f"broodje kopen":"staat14",
            f"broden stelen":"staat5",
            f"niks eten":"staat6"
            }
        },
    "staat3":{
        "text": f"Ze zijn aangekomen bij de {BLAUW}albert heijn{RESET} en hebben keuze uit heel veel eten, alleen {GROEN}Paladin{RESET} heeft maar 1 euro bij haar. Gaan ze een appel kopen of stelen?",
        "choices": {
             f"appel kopen":"staat4",
             f"appel stelen":"staat7"
             }
        },
    "staat4":{
        "text":f"Ze zijn niet gezien, pakken ze nog een appel of niet?",
        "choices": {
            f"nog een appel":"staat5",
            f"geen appel":"staat6"
            }
        },
    "staat5":{
        "text":f"{GROEN}Paladin{RESET} en haar {ROOD}kip{RESET} zijn gesnapt door de politie! Gaan ze links, rechts of rechtdoor?",
        "choices": {
            "links":"staat8",
            "rechts":"staat9",
            "rechtdoor":"staat10"
            }
        },
    "staat6":{
        "text":f"{GROEN}Paladin{RESET} heeft te weinig gegeten maar ze ziet op straat iemand lopen met een lekker stokbrood. Pakt ze die of loopt ze verder?",
        "choices": {
            "stokbrood pakken":"staat5",
            "verder lopen":"staat8"
            }
        },
    "staat7":{
        "text":f"{GROEN}Paladin{RESET} komt nog maar net weg!",
        "choices": {
            "paladin gaat eten":"staat9"
            }
        },
    "staat8":{
        "text":f"{GROEN}Paladin{RESET} heeft nog niks op en valt flauw. Wordt ze wakker in het park of in een bed in het paleis?",
        "choices": {
            "in het park":"staat12",
            "in het paleis":"staat11"
            }
        },
    "staat9":{
        "text":f"{GROEN}Paladin{RESET} kan nu rustig eten, maar waar gaat ze eten? In het park, thuis of wilt ze nog meer eten?",
        "choices": {
            "in het park":"staat12",
            "thuis":"staat13",
            "nog meer eten":"staat10"
            }
        },
    "staat10":{
        "text":f"{GROEN}Paladin{RESET} heeft zin in een appel, steelt ze die van de markt of gaat ze naar de {BLAUW}albert heijn{RESET}?",
        "choices": {
            "van de markt":"staat4",
            "albert heijn":"staat3"
            }
        },
    "staat11": {
        "text":f"{GROEN}Paladin{RESET} belandt in de cel in de kelder in het paleis. Bedankt voor het spelen!",
        "choices": {
            "opnieuw":"staat1",
            "stoppen":"stop"
            }
        },
    "staat12": {
        "text":f"In het park word {GROEN}Paladin{RESET} beroofd en nu heeft ze helemaal niks.",
        "choices":{
            "opnieuw":"staat1",
            "stoppen":"stop"
            }
        },
    "staat13": {
        "text":f"Het eten halen is geslaagd! {GROEN}Paladin{RESET} eet rustig haar eten op!",
        "choices":{
            "opnieuw":"staat1",
            "stoppen":"stop"
            }
        },
    "staat14": {
        "text":f"{GROEN}Paladin{RESET} rekent netjes af maar haar {ROOD}kip{RESET} steelt opeens een zak met zaadjes. Blijven ze staan, rennen ze we of geeft {GROEN}Paladin{RESET} het terug?",
        "choices":{
            "ze blijven staan":"staat15",
            "ze rennen weg":"staat5",
            "Paladin geeft het terug":"staat9"
            }
        },
    "staat15": {
        "text":f"De man achter de balie pakt een geweer en schiet de {ROOD}kip{RESET} dood, {GROEN}Paladin{RESET} is heel erg verdrietig.",
        "choices":{
            "opnieuw":"staat1",
            "stoppen":"stop"
            }
        },
    }

def in_rugzak(item):
    rugzak.append(item)
    print(f"{item} toegevoegd aan de rugzak.")
        
def kakelen():
    if random.random() < 0.25:
        print(f"{ROOD}KAAAAKKK! de kip trekt de aandacht!{RESET}")
    print()
    
def inputcheck(keuze,keuzes,huidigestaat):
    if keuze in keuzes:
        return keuzes[keuze], True
    else:
        return huidigestaat, False

def FSM(staat):
    while True:
        if staat == "stop":
            return None
        print(states[staat]["text"])
        kakelen()
        
        if staat in ["staat11", "staat13", "staat15"]:
            if rugzak:
                print(f"Je hebt {rugzak}in je rugzak.")
            else:
                print("Je rugzak is leeg.")
                
        if states[staat]["choices"]=={}:
            return None
        print()
        print("Uw keuzes zijn:")
        correctantwoord = False
        while correctantwoord == False:
            for keuze in states[staat]["choices"]:
                print(keuze)
            invoer = input("wat is uw keuze?").lower()
            if invoer in afkortingen:
                invoer = afkortingen[invoer]
                
            if staat == "staat2" and invoer == "broodje kopen":
                in_rugzak("broodje")
                
            elif staat == "staat2" and invoer == "broden stelen":
                in_rugzak("broodje")
                
            elif staat == "staat3" and invoer == "appel kopen":
                in_rugzak("appel")
                
            elif staat == "staat4" and invoer == "nog een appel":
                in_rugzak("appel")
                
            elif staat == "staat6" and invoer == "stokbrood pakken":
                in_rugzak("stokbrood")
                
            elif staat == "staat14" and invoer == "ze rennen weg":
                in_rugzak("zaadjes")
 
            staat, correctantwoord = inputcheck(invoer, states[staat]["choices"],staat)
            
FSM("staat1")
           
            
        
            