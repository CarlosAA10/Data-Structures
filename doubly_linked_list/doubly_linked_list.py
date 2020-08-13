"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):

        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):

        new_node = ListNode(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head

            self.head = new_node
        
        self.length += 1

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        

        if not self.head: # there is no head to delete
            return
         # use my delete function above in ListNode to delete
        value = self.head.value
        self.delete(self.head)
        
        return value 
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_tail = ListNode(value)

        if self.tail is None: # if there was one item, both head and tail would be the same, if there is none for tail it is empty 
            self.tail = self.head = new_tail
        else: # there does exist a tail, more than 1 node
            # make the prev pointer of new tail point to current tail 
            new_tail.prev = self.tail
            # we want the new tail to be the tail
            self.tail = new_tail
            # we want to make the next pointer of the new_tails previous to point to the now new tail
            new_tail.prev.next = self.tail
        
        self.length += 1
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # same operation as removing from head, except we want to check the tail this time

        value = self.tail.value

        if not self.tail:
            print("Error! there must be a tail to delete")
        else:
            self.delete(self.tail)
        
        return value

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return # the node is already at the front
        else:
            # node is not at the front
            self.delete(node) # delete the current node in it's spot
            self.add_to_head(node.value) # since add to head takes a value, we add the node now to the head

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail: # if the node is already at the end
            return # we are done
        else:
            self.delete(node) # deletes node at current spot
            self.add_to_tail(node.value) #  add the node's value to tail

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):

        self.length -= 1

        if self.head is None and self.tail is None:
            return
        if self.tail is self.head:
            self.tail = self.head = None
        elif self.head is node:# if the current node is the head
            self.head = self.head.next # make the next node from this head the head
            node.delete() # delete the current node
        elif self.tail is node: # if the current node is the tail
            self.tail = self.tail.prev # make the previous node to this tail the new tail
            node.delete() # delete the current node 
        else: 
            node.delete() # else , just delete the node
            # our delete function from before takes care of the pointers for us 


        # solution 1
        # if self.head is None and self.tail is None:
        #     return 
        # if node is self.head and node is self.tail:
        #     self.head = None
        #     self.tail = None
        # elif node is self.head: 
        #     self.head = node.next
        #     if node.prev:
        #         node.prev.next = node.next
        #     if node.next:
        #         node.next.prev = node.prev
        # elif node is self.tail: 
        #     self.tail = node.prev
        #     if node.prev:
        #         node.prev.next = node.next
        #     if node.next: 
        #         node.next.prev = node.prev
        # self.length -= 1
        # is there anything to delete?
        # check if there is only one node
        # is the node the head?
        # is it the tail? 
        # otherwise it is somewehre down the middle
        # decrement

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
    
        if self.head is None and self.tail is None:
            return 

            
        max_so_far = self.head.value 

        current = self.head

        while current is not None:
            if current.value > max_so_far:
                max_so_far = current.value
            
            current = current.next    
        return max_so_far