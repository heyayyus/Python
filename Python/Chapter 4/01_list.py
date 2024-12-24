#  strings are immutable but lists are mutable  (means we can change the values of list)    
#  lists are used to store multiple values in a single variable



friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends[0])
friends[0] = "Grapes" # Unlike Strings lists are mutable

print(friends[0])
print(friends[1:4])