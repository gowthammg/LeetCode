# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
class Solution:
    def traverse(root1, left, right, li):
        if (root1.left != None):
            Solution.traverse(left, left.left, left.right, li)
        li.append(root1.val)
        if (root1.right != None):
            Solution.traverse(right, right.left, right.right, li)
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        leftList, rightList = [], []
        if (root1 != None):
            Solution.traverse(root1, root1.left, root1.right, leftList) 
        if (root2!= None):
            Solution.traverse(root2, root2.left, root2.right, rightList) 
        print(leftList)
        print(rightList)
        return (sorted(leftList+rightList))
    
    
    