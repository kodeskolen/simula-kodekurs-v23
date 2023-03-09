# Kodekurs 09.03.2023

navn = "Marie" # Strengvariabel
#print(navn)

# tom liste: []
navneliste = ["Marie", "Lena", "Anders"] # Liste fylt med tre strenger
#print(navneliste) # Print hele listen

#print(navneliste[0]) # Print første element i listen

#for navn in navneliste: # For-løkke. For hvert navn, print hei og navn
#    print('hei')
#    print(navn)

beskjeder = ["Status - alt ok",
             "Status - trenger oppdatering",
             " Status - alt ok",
             "Status - fatal feil, trenger restart"]
nr_med_trenger = 0
nye_beskjeder = [] # Opprett tom liste
for beskjed in beskjeder: # Løkke gjennom beskjeder-listen
    # Lag nytt element uten "Status -":
    ny_beskjed = beskjed.replace("Status - ", "") # Replace("gammel teskst", "ny tekst")
    # Fyll på nytt element i den nye listen:
    nye_beskjeder.append(ny_beskjed)
    
    if "trenger" in ny_beskjed:  # If betingelse
        print(ny_beskjed)
        #nr_med_trenger = nr_med_trenger + 1
        nr_med_trenger +=1 # Øk nr_med_trenger med 1 (samme som linjen over, men enklere skrevet)

print(nr_med_trenger)
print(nye_beskjeder)

# range(start, stopp) gir rekke fra start til (ikke med) stopp
for tall in range(1,3): # tallrekken blir 1,2
    print(tall)
