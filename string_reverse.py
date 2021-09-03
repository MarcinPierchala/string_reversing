podaj = input("podaj text do odwrócenia:  ")
dlug = len(podaj)
for x, z in enumerate(podaj):
    print(podaj[dlug-x-1])
    