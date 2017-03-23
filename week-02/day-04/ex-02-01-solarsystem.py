# Saturn is missing from the planetList
# Insert it into the correct position

planetList = ["Mercury","Venus","Earth","Mars","Jupiter","Uranus","Neptune"]
planetList.insert(5, "Saturn")
print(planetList)

#or:

planetList = ["Mercury","Venus","Earth","Mars","Jupiter","Uranus","Neptune"]
pl = ["Saturn"]
planetList = [planetList[:5] + pl + planetList[5:]]
print(planetList)
