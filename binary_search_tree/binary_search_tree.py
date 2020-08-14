"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the value is less than the current node's value 
        if value < self.value:
            # does the current node have a left child?
            if self.left:

                self.left.insert(value) # we recurse again meeting base case and then inserting it where it should be 
            # otherwise there is no left child
            # we can park the new node here 
            else:
                self.left = BSTNode(value)
        # otherwise the value is greater or equalto the current node's value 
        else:
            # does the current node have a right child 
            if self.right:
                self.right.insert(value)
            # otherwise there is no right node
            # let's park this value at this right value
            else:
                self.right = BSTNode(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        if self.value == target: # where our recursion stops 
            # return true or the value
            return True


        else:
            # we want to compare the value of the target to the current node's value
            # if it is less than the node, we will want to traverse through the node's
            # left pointer 
            if target < self.value:

                if self.left:

                    return self.left.contains(target)
            
            # if it greater than the node, we will traverse through the right side 
            if target > self.value:
                
                if self.right:

                    return self.right.contains(target)
                
        
        return False

# recursion saves each call in a stack and that is how it executes 

    # Return the maximum value found in the tree

    def get_max(self):

        max_so_far = self # the current node we start at 

        while max_so_far.right is not None: # we dont want to reach when the node is none
            # because when the node is none we don't have any right, left or value attr

            max_so_far = max_so_far.right

        return max_so_far.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value) # we must recurse but call the function on each self.value

        if self.left: # we want to call it for each item left or right of the root node, and then on 
            # so we must check for a left and also for a right and if there is, then we call the function on them

            self.left.for_each(fn)

        if self.right:

            self.right.for_each(fn)



    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        
        # we go through each left node, till we can't go anymore
        # the last value is the smallest
        # then we go through the right most side all the way, and then print those
        # because those will be the biggest values, so they will be printed at the end
        current_node = self
        
        if not current_node:
            return 

        if current_node.left:

            current_node.left.in_order_print()

        print(current_node.value)

        if current_node.right:

            current_node.right.in_order_print()


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
# inserted some nodes

# print(bst.contains(6))
# print(bst.contains(32))

# print(bst.get_max())
print(bst.in_order_print())


# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
