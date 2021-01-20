#pour trouver list de tout les utilisateur
#l=list
l = open("input/connection.log", "r")
liste_connection=[]

for line in l :

    h=line.split(";")
    print(h[1])
print(liste_connection)

l.close()
