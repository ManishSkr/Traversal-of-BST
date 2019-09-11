#All traversals

class node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None

def insert(root,node):
    if root is None:
        root=node
    elif(root.val<node.val):
        if root.right is None:
            root.right=node
        else:
            insert(root.right,node)
    else:
        if root.left is None:
            root.left=node
        else:
            insert(root.left,node)


r=input("Enter the root value- ")
root=node(r)
_node=int(input("How many nodes you want to enter- "))
while(_node):
    value=input("Enter the value- ")
    insert(root,node(value))
    _node-=1


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)



print("!.. Inorder Traversal..!")
inorder(root)
print("!.. Pre order Traversal..!")
preorder(root)
print("!.. Post order Traversal..!")
postorder(root)

        
