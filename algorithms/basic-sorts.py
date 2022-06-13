# bubble up; sort the largest item to the end each iteration
# O(n^2)
def bubble_sort(my_list):
    for i in range(len(my_list) -1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
                
    return my_list

print('bubble sort')
print(bubble_sort([4,2,6,5,1,3]))

# look for minium index each iteration and switch with the first  one
# O(n^2)
def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i]= my_list[min_index]
            my_list[min_index] = temp
    return my_list

print('slection sort')
print(selection_sort([4,2,6,5,1,3]))

# start with second item and compare with the previous ones
# O(n^2)
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

print('insertion sort')
print(insertion_sort([4,2,6,5,1,3]))        

# helper function
def merge(list1, list2):
    combined = []
    i, j = 0, 0
    while i < len(list1) and j  < len(list2):
        if list1[i] < list2[j]:
            combined.appnend(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined
    
# break list in half
# base case when len(the_list) == 1
# use merge() to put list together
def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = len(my_list)//2
    left = my_list[:mid]
    right = my_list[mid:]
    return merge(merge_sort(left), merge_sort(right))
