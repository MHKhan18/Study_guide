

#=====================pre-order==========================:

# recursive:  
def preorder_rec(root):
    if root is None:
        return None
    print(root.val , end = ' ')
    preorder_rec(root.left)
    preorder_rec(root.right)

#iterative:
def preorder_iter(root):

    stack = [root]

    while len(stack) > 0:
        root = stack.pop()

        if root is not None:
            print(root.val , end = ' ')
            stack.append(root.right)
            stack.append(root.left)

# ======================inorder================================

def inorder_rec(root):
    if root is None:
        return None
    inorder_rec(root.left)
    print(root.val , end = ' ')
    inorder_rec(root.right)

def inorder_iter(root):

    stack = []
    curr = root

    while len(stack) > 0 or curr is not None:

        if curr is not None:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.val , end = ' ')
            curr = curr.right


#================postorder =====================================

def postorder_rec(root):
    if root is None:
        return None
    postorder_rec(root.left)
    postorder_rec(root.right)
    print(root.val , end = ' ')

# using two stacks:

def postorder_iter1(root):

    if root is None: 
        return None
    
    stack1 = []
    stack2 = []

    stack1.append(root)

    while len(stack1) > 0:
        node = stack1.pop()
        stack2.append(node)
        if node.left is not None:
            stack1.append(node.left)
        if node.right is not None:
            stack1.append(node.right)

    while len(stack2) > 0:
        node = stack2.pop()
        print(node.val , end = ' ')


# usign one stack:
def postorder_iter2(root):

    curr = root
    stack = []

    while curr is not None or len(stack) > 0:
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        else:
            temp = stack[len(stack)-1].right
            if temp is None:
                temp = stack.pop()
                print(temp.val , end = ' ')
                while len(stack) > 0 and temp == stack[len(stack)-1].right:
                    temp = stack.pop()
                    print(temp.val , end = ' ')
            else:
                curr = temp




class Node:
    def __init__(self , val):
        self.val = val
        self.left = None
        self.right = None



if __name__ == "__main__":
    # create a tree
    '''
                1
               / \
              /   \
             2     3
            / \   / \
           /   \ 6   7
          4     5
    '''

    root = Node(1)
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    root.right.left = Node(6) 
    root.right.right = Node(7) 
    
    print("preorder_rec:")
    preorder_rec(root)
    print("\n" , end = '')
    print("preorder_iter:")
    preorder_iter(root)
    
    print("\n==============================")
    
    print("inorder_rec:")
    inorder_rec(root)
    print("\n" , end = '')
    print("inorder_iter:")
    print(inorder_iter(root))

    print("\n==============================")
    
    print("postorder_rec:")
    postorder_rec(root)
    print("\n" , end = '')
    print("postorder_iter1:")
    postorder_iter1(root)
    print("\n" , end = '')
    print("postorder_iter2:")
    postorder_iter2(root)
