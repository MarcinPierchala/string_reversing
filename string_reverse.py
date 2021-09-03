podaj = input("podaj text do odwrócenia:  ")
dlug = len(podaj)
z = 1
for x in podaj:
    print(podaj[dlug-z])
    z+=1