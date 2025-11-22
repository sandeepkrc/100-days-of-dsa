from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge_arrays(arr1, arr2):
            ans = len(arr1) + len(arr2)
            merged = []
            i ,j = 0, 0
            while i < len(arr1) or j < len(arr2):
                if i < len(arr1) and j < len(arr2):
                    if arr1[i] <= arr2[j]:
                        merged.append(arr1[i])
                        i += 1
                    else:
                        merged.append(arr2[j])
                        j += 1
                elif i < len(arr1):
                    merged.append(arr1[i])
                    i += 1
                else:
                    merged.append(arr2[j])
                    j += 1
            return merged
        merged_array = merge_arrays(nums1, nums2)
        n = len(merged_array)
        if n % 2 == 0:
            mid1 = n // 2
            mid2 = mid1 - 1
            median = (merged_array[mid1] + merged_array[mid2]) / 2
        else:
            mid = n // 2
            median = merged_array[mid]
        return median                       
    

sol = Solution()
print(sol.findMedianSortedArrays([1, 3], [2]))  # 2
print(sol.findMedianSortedArrays([1, 2], [3, 4]))  # 2.5
print(sol.findMedianSortedArrays([0, 0], [0, 0]))





