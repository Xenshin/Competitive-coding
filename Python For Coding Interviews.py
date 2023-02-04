# Division is decimal by default
print(5/2)

# Double slash rounds down
print(5//2)

# CAREFUL: most languages round towards 0 by default so negative numbers will round down
print(-3//2)

# A workaround for rounding towards zero is to use decimal division and then convert to int.
print(int(-3/2))

# Modding is similar to most languages
print(10%3)

# Except for negative values
print(-10%3)

# To be consistent with other languages modulo
import math
print(math.fmod(-10, 3))

# Array (called lists in python)
arr = [1,2,3]
print(arr)

# Can be used as a stack (dynamic array)
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

arr.insert(1,7) # this will insert 7 at index 1 (time complexity : O(n))
print(arr)

# But with direct indexing it can be done in constant
arr[0] = 0
arr[3] = 0
print(arr)

# Initialize arr of size n with default value of 1
n = 5
arr = [1]*n
print(arr)
print(len(arr))

# CAREFUL: -1 is not out of bounds, it's the last value
print(arr[-1])

# Sublists (aka slicing)
arr = [1,2,3,4]
print(arr[1:3]) # similar to for-loop ranges, last index is non-inclusive

# Unpacking
a,b,c = [1,2,3]

# Loop through arrays
    # 1) using index
for i in range(len(arr)):
    print(arr[i])

    # 2) without indexing
for n in arr:
    print(n)

    # 3) with index and value
for i, n in enumerate(arr):
    print(i, n)

# Loop through multiple arrays simultaneously with unpacking
nums1 = [1,2,3,4]
nums2 = [5,6,7,8]
for n1, n2 in zip(nums1,nums2):
    print(n1,n2) 

# REVERSE
arr.reverse()
print(arr)

# SORTING
arr = [5,4,7,3,8]
arr.sort() # sorts in ascending order by default
print(arr)

arr.sort(reverse=True) # this will sort in descending order
print(arr)

# sorting string literals
arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr) 

# Custom Sort (by length of string)
arr.sort(key=lambda x: len(x))
print(arr)

# List Comprehension
arr = [i+i for i in range(5)]
print(arr)

# 2-D lists
arr = [[0] * 4 for i in range(4)]
print(arr)

##########################################################  STRINGS  ################################################################################
s = "abc"
print(s[0:2])

# but they are immutable
'''s[0] = "A"'''

# so this creates a new string
s += "def"
print(s) # modifying a string is considered as O(n) type operation

# Valid numeric strings can be converted
print(int("123") + int("123"))

# And numbers can be converted to strings
print(str(123) + str(123))

# In rare cases you may need the ASCII value of a char
print(ord("a"))
print(ord("A"))

# Combine a list of strings (with an empty string delimitor)
strings = ["ab", "cd", "ef"]
print("^_^".join(strings)) # i can specify anything in between those "" to join the strings

#############################################################################################################################################
#############################################################################################################################################
#############################################################################################################################################

#*************************************************QUEUES*************************************************************************************

# By default they are double ended queues
from collections import deque

queue = deque()
queue.append(1) 
queue.append(2)
print(queue)

queue.popleft() # operations are performed in constant time unlike stacks
print(queue)

queue.appendleft(1)
print(queue)

queue.pop() # popright()
print(queue)


#***********************************    HASHSET  *****************************************************************************************
myset = set()

myset.add(1)
myset.add(2)
print(myset)
print(len(myset)) # all these operations like adding, finding the length, removing and searching is done in constant time in hashset

print(1 in myset)
print(2 in myset)
print(3 in myset)

myset.remove(2)
print(2 in myset)


# list to set
print(set([1,2,3])) # as sets dont contain duplicate values, so if passed list has duplicates then those will be removed

# set comprehension
myset = {i for i in range(5)}
print(myset)

######################################   HASHMAP  ############################################################################
mymap = {}
mymap["alice"] = 88          #initializing the key "alice"
mymap["bob"] = 77            #initializing the key "bob"
print(mymap)                 #in this hashmap also the operations are performed in constant time
print(len(mymap))

mymap["alice"] = 80          #changing the value of key "alice"
print(mymap["alice"])        

print("alice" in mymap)      #searching for alice in the hashmap (this operation is also performed in constant time)
mymap.pop("alice")           #removing "alice" by mentioning its key
print("alice" in  mymap)

mymap = {"alice":90, "bob":70}
print(mymap)


# Dict comprehension
mymap = {i: 2*i for i in range(5)}
print(mymap)

# Looping through maps
mymap = {"alice":90, "bob":70}
for key in mymap:
    print(key, mymap[key])

for val in mymap.values():
    print(val)

for key, val in mymap.items():
    print(key, val)


