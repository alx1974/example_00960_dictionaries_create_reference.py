# erstelle dictionary 'christian': 50, 'bettina': 100, 'doris': 75, 'alfred': 10

persons = {"chrstian": 50, "bettina": 100, "doris": 75, "alfred": 10}
print(persons)
# change punkte von alfred auf 30 

alfred = {"alfred": 30}
persons.update(alfred)
print(persons)
# erstelle eine liste mit 2 nachnamen und fuege ihren alter und
# vornamen als liste in form von value hinzu

namen = ["ecker", [30, "richard"], "haumer", [50, "eduard"]]

# Iteration und alle Elemente einzeln aufzeigen

for element in namen:
    print(element)

liste = [["ecker", "haumer"], [30, 50, "richard", "eduard"]]
#liste = nachnamen+namen2 #zusammenfügen
print()

for row in liste:
    for elem in row:
        print(elem, end=' ')
    print()
#for element in liste:
 #   print(element)


#print(liste)







