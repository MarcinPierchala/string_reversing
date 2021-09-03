podaj = input("podaj text do odwrócenia:  ")
dlug = len(podaj)
new = ''
for x, z in enumerate(podaj):
    print(podaj[dlug-x-1])
    new += podaj[dlug-x-1]

print(new)

    