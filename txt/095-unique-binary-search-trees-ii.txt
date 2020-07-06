Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.


For example,
Given n = 3, your program should return all 5 unique BST's shown below.


   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3




```python
class Solution(object):
  def generateTrees(self, n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
```
