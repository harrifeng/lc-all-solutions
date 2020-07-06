Given an integer array nums, find the sum of the elements between indices i and j (i &le; j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8



Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.




```python
  def __init__(self, start, end):
  def __init__(self, nums, start, end):
  def buildTree(self, nums, start, end):
  def updateVal(self, i, val):
  def sumRange(self, i, j):
  def __init__(self, nums):
    """
    :type nums: List[int]
    """
  def update(self, i, val):
    """
    :type i: int
    :type val: int
    :rtype: int
    """
  def sumRange(self, i, j):
    """
    :type i: int
    :type j: int
    :rtype: int
    """
```
