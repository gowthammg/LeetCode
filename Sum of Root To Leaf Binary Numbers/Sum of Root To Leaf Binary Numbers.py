# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(root, val, arr):
        if (root.left!=None):
            val = val*10+root.val
            Solution.traverse(root.left, val, arr)
            val = int(val/10)
        if (root.right != None):
            val = val*10 +root.val
            Solution.traverse(root.right, val, arr)
            val = int(val/10)
        if (root.left == None and root.right == None):
            val = (val*10)+root.val
            arr.append(val)
            return val
        
    def sumRootToLeaf(self, root: TreeNode) -> int:
        arr = []
        Solution.traverse(root, 0, arr)
        print(arr)
        sum = 0
        mul = 1
        for i in arr:
            mul = 1
            while(i!=0):
                rem=i%10
                sum=sum+(rem*mul)
                i=i//10
                mul*=2
            print(sum,i)
        return sum
                
                
        