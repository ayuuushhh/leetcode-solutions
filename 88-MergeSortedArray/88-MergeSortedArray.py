# Last updated: 27/07/2026, 15:26:38
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        reader1 = m - 1 # pointer for nums1
7        reader2 = n - 1 # pointer for nums2
8        writer = m + n - 1 # pointer for writing to nums1
9
10        # comparing the values at a and b:
11        while reader1 >= 0 and reader2 >= 0:
12            # if value at reader1 is larger, writer writes value of reader1
13            if nums1[reader1] > nums2[reader2]:
14                nums1[writer] = nums1[reader1]
15                # reader1 and writer decrement
16                reader1 -= 1
17                writer -= 1
18        
19        # if value at reader2 is larger, writer writes value of reader2
20            else:
21                nums1[writer] = nums2[reader2]
22                # reader2 and writer decrement
23                reader2 -= 1
24                writer -= 1
25
26        while reader2 >= 0:
27            nums1[writer] = nums2[reader2]
28            reader2 -= 1
29            writer -= 1
30
31