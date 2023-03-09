# Mer tekstbehandling: split, sort and join

# Middagsliste fra https://github.com/kodeskolen/simula-kodekurs-v23/blob/main/undervisningsmateriale/dag2/middagsliste.txt


middagsliste = 'laks_og_ovnsbakte_grønnsaker,gulrotsuppe,kyllingwok,mossaka,spansk_gazpacho,quiche,fylt_paprika,hamburgere,sushi,kylling_med_potet-_og_tomatsalat,gyoza,meksikansk_taco,linsesuppe,tortelloni,pizza,potet-_og_purresuppe,soyamarinert_laks,spanske_kjøttboller,lammegryte,steambuns,ørret_med_quinoasalat,shepherds_pie,tomatsuppe,helstekt_kylling,kremet_pasta_med_ørret,kylling-_og_sopprisotto,enchiladas,vegetarisk_thaigryte,asiatisk_kyllingsalat,ungarsk_gulasj,kylling_tikka_masala'


middagsliste = middagsliste.replace("_", " ")

# Del opp strengen i liste så du kan sortere
middagsliste = middagsliste.split( ',') # Potensielt: legg in feil ' ,' istedenfor ',' og se at det ikke splittes og at middagsliste[0] gir hele

# Sorter
middagsliste = sorted(middagsliste)


utvalgte_retter = []
nr_utvalgte_retter = 0
for rett in middagsliste:
    if 'ørret' in rett:
        utvalgte_retter.append(rett)
        nr_utvalgte_retter+=1
    elif 'laks' in rett:
        utvalgte_retter.append(rett)
        nr_utvalgte_retter+=1
    else:
        print('Hverken ørret eller laks her!')


print(nr_utvalgte_retter)

# Slå sammen til streng igjen, med én rett på hver linje
utvalgte_retter = '\n'.join(utvalgte_retter)

print(utvalgte_retter)  # Kommentar: kan skrives til fil. Dette gjør vi neste gang.



# Ekstra: not operator. Hvis vi ikke liker fisk
utvalgte_retter = []
nr_utvalgte_retter = 0
for rett in middagsliste:
    if ('ørret' not in rett) and ('laks' not in rett):
        utvalgte_retter.append(rett)
        nr_utvalgte_retter+=1




