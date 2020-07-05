class Solution(object):
  def numberOfBoomerangs(self, points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    # we compute the distance starting from any given point and we use a hashtable to count the number of the same distance obtained
