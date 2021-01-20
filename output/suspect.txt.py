file= open("input/warning.txt","r")
suspect_lines=file.readlines()

file.close()
file= open("input/connection.log","r")

lines=file.readlines()
file.close()
Liste_suspect=[]
for line2 in suspect_lines:



     Liste_suspect.append(line2.strip('\n'))


liste_des_connectés_IP_suspects=[]

for line in lines:
    line1=line.split(";") 
    ip=line1[0]

    for ip_suspect in  Liste_suspect:
        if ip==ip_suspect:
           liste_des_connectés_IP_suspects.append(line1[1])
        else:
            pass
print(liste_des_connectés_IP_suspects)


     
f = open('output/suspect.txt','w')
for nom in set(liste_des_connectés_IP_suspects):

    nombre_de_fois=liste_des_connectés_IP_suspects.count(nom)

    f.write("{},{}\n".format(nom,nombre_de_fois))

    print("{},{}".format(nom,nombre_de_fois))
f.close()