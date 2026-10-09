class Node:
    def __init__(self, v, l=None, r=None):
        self.value = v
        self.left = l
        self.right = r

def same(root_a, root_b):

    if root_a == None and root_b == None:
        return True

    if root_a == None and root_b != None:
        return False

    if root_a != None and root_b == None:
        return False

    if root_a.value == None and root_b.value == None:
        return True

    if root_a.value != root_b.value:
        return False


    result_1 = same(root_a.right, root_b.right)
    result_2 = same(root_a.left, root_b.left)
    if result_1 and result_2:
        return True
    else:
        return False
