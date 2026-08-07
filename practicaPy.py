estrellas = ['sirio', 'canopus', 'arcturus', 'vega', 'capella', 'rigel', 'procyon', 'achernar', 'betelgeuse', 'hadar']

estrellas.append('altair')
estrellas.insert(2, 'aldebaran')



estrellas.sort()
for estrella in estrellas:
    print(estrella.title())
    
print('La lista tiene',len(estrellas))