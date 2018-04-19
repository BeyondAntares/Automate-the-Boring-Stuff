# Sorting and creating set items
# (i.e. removing redundant or repeated items from a list)

List1 = [10,9,9,9,9,9,8,7,6,5,5,4,4,3,2,1,1,1,1,1,1]
print("Your list is "), print(List1)
print("Your list sorted is: ")
List1.sort() 
print(List1)
List3 = list(set(List1))
List3.sort()
print("Your list as a set is: "), print(List3)

