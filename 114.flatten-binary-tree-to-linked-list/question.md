
Given a binary tree, flatten it to a linked list in-place.



For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6



The flattened tree should look like:

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6


click to show hints.

Hints:
If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.



```python
class Solution(object):
  def flatten(self, root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
```
