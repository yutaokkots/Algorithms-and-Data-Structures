class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        counter = 0
        p = n
        o = m + n
        for i in range(o):
            if i < m:
                pass
            elif p > 0:
                nums1[i] = nums2[counter]
                p -= 1
                counter += 1
        nums1.sort()
        print(nums1)

sol = Solution()

print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))