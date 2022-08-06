## Binary Tree

### Terminologies
- Full tree: every node point to 0 or 2 nodes
- perfect tree: in every level in the tree is filled
- complete tree: filling the tree from left to right without gap

n = # of nodes
number of nodes = 2^n - 1 where n is level

### Time Complexity
lookup, insert, remove: O(log n)  

!!!!! but  
when (10)-(20)-(30)-(40)-(50)  
technically O(n)    

NOTE!!!   
insert() on linkedList is O(1) but on bst in O(log n)  
for other operations bst is better O(log n)

### When to use 
Binary Search Trees are sorted which makes them better at searching for all values that fall within a range

## Class
class is like a cookie cutter, a frame. and with a class we can make objects based the class with different flavors.

```
Class Cookie:
	# constructor initilize the class with a variable "color"
  # 'self' tells that this method inside a class instead of a function
	def __init__(self, color):
		self.color = color

	def get_color(self):
		return self.color

	def set_color(self, color):
		self.color = color
```

## Hash Table
- dictionary is made of key and value. and uses hash function to assign key value pairs to a hash table.
- with the hash function we perform hash on a key and we get an address to store the value. 

### Hash
1. one way: get the address only one way 
2. deterministic: for particular key input we get the same output everytime we run key on hash

### collision 
happens when adding a key value pair when a pair already exist at an address. 

### how to solve collision
1. sepereate chaining: creating a list of linked list at an address to contain multiple key value pairs 
2. linear probing (open addressing): keep looking for  a empty address when a hashed address is already occupied
