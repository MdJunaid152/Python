class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def inorder_traversal(root):

    result = []
    if root:
        result += inorder_traversal(root.left)
        result.append(root.val)
        result += inorder_traversal(root.right)
    return result

def preorder_traversal(root):

    result = []
    if root:
        result.append(root.val)
        result += preorder_traversal(root.left)
        result += preorder_traversal(root.right)
    return result

def postorder_traversal(root):

    result = []
    if root:
        result += postorder_traversal(root.left)
        result += postorder_traversal(root.right)
        result.append(root.val)
    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder traversal:", inorder_traversal(root))
print("Preorder traversal:", preorder_traversal(root))
print("Postorder traversal:", postorder_traversal(root))