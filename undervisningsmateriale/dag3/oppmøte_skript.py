'''reg_deltakere = ["Linn", "Pål", "Per", "Sam"]
fakt_deltakere = ["Per", "Sam", "Linn"]

oppmøte_antall = 0
for deltaker in reg_deltakere:
    if deltaker in fakt_deltakere:
        oppmøte_antall += 1

print(f"Av de {len(reg_deltakere)} registrerte deltakerne, møtte {oppmøte_antall} deltakere opp.")
