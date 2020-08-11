"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        



class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):

        return self.size


    def push(self, value):
        pass

    def pop(self):
        pass


# stack = Stack()

# stack.push(4) # we have one item in our array
# stack.push(3)
# stack.push(5)
# stack.push(43)

# # we should have 4 items added to our storage array


# print(stack.__len__(), 'the length should be 4')
# print(stack.storage)


# print(stack.pop())
# print(stack.pop())

# # we should have 2 items removed from our array, leaving us 
# # with a length of 2 items 
# print(stack.__len__(), 'it should be 2')
# # print(stack.storage)

# print(len(stack), 'length of stack')

# stack class implemented with array

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):

#         return self.size


#     def push(self, value):
#         self.storage.append(value) # we added an item to our array 
#         self.size += 1 # each time we call push, increment the size by one

#     def pop(self):

#         if self.size == 0:
#             return None

#         self.size -= 1 # successfully decrease the size respectively 
#         return self.storage.pop() # succesfully takes away from our array




