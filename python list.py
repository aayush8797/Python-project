states= ["delhi" , "bihar","banglore",1,5.8,True]
print(states)
#print separate item by using index
print(states[2])
#change the item using index
states[0]="jammu"
print(states)
#add any item to the list
states.append("rajasthan")
print(states)
#extend means making a new list and adding to another list at the end
states.extend(["jharkhand","kerala"])
print(states)