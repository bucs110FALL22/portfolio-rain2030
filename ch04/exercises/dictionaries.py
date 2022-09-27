string1 = "Hurricane Ian strengthened to a Category 2 hurricane on Monday as it took aim at Cuba and Florida. Ian is currently forecast to make landfall on the west coast of Florida or the Florida Panhandle by midday Thursday, though there is uncertainty about the hurricane's track and intensity. Florida Gov. Ron DeSantis has declared a state of emergency for the entire state, with storm conditions projected to constitute a major disaster. The National Hurricane Center has advised residents of Cuba, the Florida Keys and the Florida Peninsula to have a hurricane plan in place and to closely follow forecast updates."

print(string1)
print("")

lookp_dict = {"strengthened" : "weakened", "make" : "push the", "Cuba" : "The Unnecessary Country", "Gov." : "Lizard Man", "advised":"opposed", "closely":"not to", "updates.":"updates at all."}

temp = string1.split()
string2 = []
for wrd in temp:
     
    # searching from lookp_dict
    string2.append(lookp_dict.get(wrd, wrd))
     
string2 = ' '.join(string2)
 
# printing result
print(string2)
  