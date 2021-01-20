
file= open("input/connection.log","r")
Lines=file.readlines()
for line in Lines:

     l0=line.split(";")

     l1=line.split(" ")
    # print(l1[1])
     l2=l1[1].split(":")
     #print(l2[0])
     heure=int(l2[0])
     minute=int(l2[1])
     if  8 <= heure <= 18:
            pass
     elif heure==19:

            if minute==0:
                pass

            else:
                print(l0[0:2])