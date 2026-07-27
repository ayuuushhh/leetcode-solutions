# Last updated: 27/07/2026, 01:32:26
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        nums1[:] = nums1[:m]
7        nums2[:] = nums2[:n]
8        nums1.extend(nums2)
9        nums1.sort()
10        