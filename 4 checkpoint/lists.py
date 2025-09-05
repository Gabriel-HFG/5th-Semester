independance_stages = ["Inicio","Organizisacion","Resistencia","Consumacion"] #The list
print(independance_stages[:2]) #prints from the first item to item 2 in the list independance stages
print(len(independance_stages)) #prints how many items are in the list independance stages

leaders = [] #Empty leaders list
leaders.append("Miguel Hidalgo")   #adds a name to the list leaders
leaders.append("Jose Maria Morelos") #adds another name to the list leaders
# leaders.extend(independance_stages) #adds both lists together

leaders.insert(1,"Vicente Guerrero") # inserts a value in a certain index
# leaders.remove("Vicente Guerrero")
leaders.append("Agustin de Iturbide") # adds an item to the end of the list
# leaders.append(input("Type a leader"))
# leaders.pop(0)
# leaders.clear()
print(leaders.index("Miguel Hidalgo")) # gets the index of something in the list
print(leaders.count("Vicente Guerrero")) # counts how many there are of an item in the list
print(leaders.sort()) # orders the list in alphabetica order
print(leaders.reverse()) # prints the list in reverse
new_leaders = leaders.copy() # creats a copy of the list

print(new_leaders)