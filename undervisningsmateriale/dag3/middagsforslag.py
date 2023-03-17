with open("middagsforslag.txt", mode="r", encoding="utf-8") as tekstfil:
    #første_linje = tekstfil.readline()
    innhold_fil = tekstfil.read()
    #print(første_linje)
    #print(innhold_fil)
    
# Splitt til liste    
linjer = innhold_fil.splitlines()
#print(linjer)