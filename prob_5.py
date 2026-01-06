# Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m
        # m and n is a size of array

        while low <= high:
            px = (low + high) // 2
            py = (m + n + 1) // 2 - px

            # px → partition index in nums1
            # py → partition index in nums2
            # We split both arrays into left part and right part such that:
            # Total elements on the left side = total elements on the right side (or +1)

            lx = float('-inf') if px == 0 else nums1[px - 1]
            rx = float('inf') if px == m else nums1[px]

            # lx: largest element on left side of nums1
            # rx: smallest element on right side of nums1
            # -inf and inf handle edge cases

            ly = float('-inf') if py == 0 else nums2[py - 1]
            ry = float('inf') if py == n else nums2[py]

            if lx <= ry and ly <= rx:
                if (m + n) % 2 == 0:
                    return (max(lx, ly) + min(rx, ry)) / 2
                else:
                    return max(lx, ly)
            elif lx > ry:
                high = px - 1
            else:
                low = px + 1


# ------------------ TEST IN VS CODE ------------------

if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    nums1 = [1, 3]
    nums2 = [2]
    print("nums1:", nums1)
    print("nums2:", nums2)
    print("Median:", solution.findMedianSortedArrays(nums1, nums2))

    print("-" * 30)

    # Test Case 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    print("nums1:", nums1)
    print("nums2:", nums2)
    print("Median:", solution.findMedianSortedArrays(nums1, nums2))

    print("-" * 30)

   #only Binary Search on partitions is give n O(log(min(m,n))) time complexity
   #In case of merg+sort time complexity will be O((m+n)log(m+n)) because of in merge O(m+n) and in sort O(log(m+n))
   #In case of two pointer approach time complexity will be O(m+n) because we are traversing both arrays once
