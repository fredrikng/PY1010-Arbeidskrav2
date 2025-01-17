# Arbeidskrav 2 PY1010
#Oppgave 2)

#Det skal arrangeres klassefest og det skal kjøpes inn riktig mengde pizza


# Her fyller man inn antall elever som skal delta

antall_elever = int(input("Skriv inn antall elever:"))



# Man antar at hver elev spiser 1/4 pizza

antall_pizzaer = antall_elever * (1 / 4)



# For å sikre at det ikke blir kjøpt for lite pizza til festen, runder vi opp.
# Her plusser jeg på med 0.9 for å runde opp, og bruker // for å runde ned til nærmeste hele tall.

hel_pizza = (antall_pizzaer + 0.9) // 1



# For å kun vise et hel tall i printen, gjør jeg om variabelen til en int

print("Det må kjøpes inn", int(hel_pizza) , "pizzaer til klassefesten")



