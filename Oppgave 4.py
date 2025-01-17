# Arbeidskrav 2 PY1010
# Oppgave 4)


data = {
       "Norge": ["Oslo", 0.634],
       "England": ["London", 8.982],
       "Frankrike": ["Paris", 2.161],
       "Italia": ["Roma", 2.873],
        }

svar = input("Skriv et land: ")

# Hvis landet man skriver inn, finnes i dictionaryen, blir det printet ut med info om hovedstad og innbyggertall i hovedstaden.

if svar in data:
    
    hovedstad, innbyggertall = data [svar]
    print (f"{hovedstad} er hovedstaden i {svar} og det er {innbyggertall} millioner innbyggere i {hovedstad}")

# Hvis landet man skriver inn, ikke finnes i dictionaryen, får man opp at landet ikke er registrert.
# Man vil så bli spurt om man ønsker å legge til landet man skrev inn i dictionaryen.

else:
    print (f"{svar} er ikke registrert")
    
    nytt_land = input("Vil du legge til landet? ")

# Hvis man svarer ja, vil man bli spurt om hva hovedstaden og innbyggertallet i hovedstaden
# Det man svarer her vil bli lagt inn i dictionaryen


    if nytt_land == "ja":
        land_hovedstad = input(f"Hva er hovedstaden i {svar}?")
        hovedstad_innbyggertall = input("Hvor mange millioner mennesker bor det i hovedstaden? ")
        
        data [svar] = [land_hovedstad, hovedstad_innbyggertall]
        

        print(f"{svar} er nå lagt inn")


# Hvis man svarer noe annet en ja, blir denne beskjeden printet
        
    else:
        
        print(f"{svar} ble ikke lagt inn")



# Her blir en oppdatert dictionary printet til skjerm
print (data)
        
    
    



