# Data Structure & Algorithms
## This repo is created for studying Data Structure and Algorithms.
### Data Structure
* Linked lists
* Doubly Linked lists
* Stacks: LIFO
* Queue: FIFO
* Binary Search Tree
* Hash table
* Graph
### Algorithms
* Recursion
* Basic Sorts
* Merge Srot
* Quick Sort
* Tree Traversal

### Big O
Check out [Cheatsheet](https://www.bigocheatsheet.com/) for reference and charts.

> Big O let us decide which data structure or algorithm to use in different situations.
Because each data structure and algorithms has different Big O for different operations we consider our situtution and tradeoffs of time complexity and space complexity to choose which one to use.

#### Greek Letters
* **Omega Ω**: best case scenario  
* **Theta θ**: average case scenario 
* **Omicron(big O) Ο**: worst case scenario (always worst case)

#### Terminologies
* **Time complexity**: how fast the code run
* **Space complexity**: how much space

#### Examples
- O(n)
```
for i in range(n):
    print(i)
```
- O(n^2)
```
for i in range(n):

    for j in range(n):

        print(I, j)
```
-  O(1) constant time 
```
def add_items(n)

    return n+n+n
```


- O(log(n))  
>Binary search

- O(nlogn)

    >Some sorting algorithm: most efficient sorting algorithm
    
#### Drop Constants 
A rule of thumb to drop constanst expressing performance in Big O.  

* O(2n) = O(n)

* O(2n^2) = O(n^2)

#### Drop non-dominants
As n gets bigger non-dominant term become trivial so we can drop the non-dominant term

* O(n^2 +n) = O(n)
```
for I in range(n):

    for j in range(n):

        print(I, j)
for i in range(n):

    print(i)
```

#### Different terms for inputs

When you have two different variables as input we can’t simplify this to O(n) instead it’s O(a+b)
```
def print_items(a,b):

    for i in range(a):

        print(i)

    for j in range(b):

        print(j)

```
#### Lists

* Adding, removing at the end -> O(1)

* Adding, removing at the front and middle -> O(n) _because of re-indexing_

* Searching -by value> O(n)

* Searching by index -> O(1)

#### Wrap up

| Big O.    | Algorithm          |
| ----------|:------------------:|
| O(n^2)    | Loop whitin a loop |
| O(n log n)| Most efficient algo|
| O(n)      | Proportional       |
| O(log n)  | Divide and conquer |
| O(1)      | Constant time      |

