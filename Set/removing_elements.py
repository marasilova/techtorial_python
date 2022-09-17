# We use two methods to remove elements from the set.
#discard() method and remove() method.

#remove(valueoftheObject)

set={3,5,7,9}

#I want to remove the number 7 from the set

set.remove(7)
#number 7 will be gone from the set.
print(set)

#when the lement needs to be removed does not exists in the set
# it will throw an error.
# set.remove(7)

# discard(valueOfTheObject) method

set.discard(3)
print(set)
# when the element needs to be removed does not exist in the set
# it will not throw an error and it won't anything.
set.discard(3)