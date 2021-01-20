f = open('input/prenoms.txt', 'r')
liste_prenoms=[]

for line in f:
    liste_prenoms.append(line.strip()) #la fonction .strip() permet de retirer le '\n' dans la liste 


print(liste_prenoms)

f.close()