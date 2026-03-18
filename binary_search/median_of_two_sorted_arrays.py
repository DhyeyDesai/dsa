# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

# TODO: revise

# Find median of two sorted arrays using binary search on partitions.

# INTUITION:
# Instead of merging arrays, we partition both arrays such that:
# - Left partition contains smaller half of all elements
# - Right partition contains larger half of all elements
# - All elements in left ≤ all elements in right

# The median is at the boundary of these partitions.
# We binary search on the SMALLER array to find the correct partition point.

# TIME COMPLEXITY: O(log(min(m, n)))
# - Binary search on the smaller array
# - Each iteration does O(1) work

# SPACE COMPLEXITY: O(1)
# - Only using a few variables, no extra data structures

def findMedianSortedArrays(nums1, nums2):
    
    # Always perform binary search on the smaller array for efficiency
    # This ensures we do log(min(m,n)) instead of log(max(m,n))
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    
    # Binary search range: 0 to m (partition positions, not indices)
    # We can take anywhere from 0 to m elements from nums1
    left, right = 0, m
    
    while left <= right:
        # partitionX = how many elements we take from nums1 for left partition
        partitionX = (left + right) // 2
        
        # partitionY = how many elements we take from nums2 for left partition
        # Total left partition should have (m+n+1)//2 elements
        # The +1 handles both odd and even cases correctly
        partitionY = (m + n + 1) // 2 - partitionX
        
        # Get the boundary elements around the partition
        # Use infinity for edge cases when partition is at array boundaries
        
        # maxLeft1: largest element in left partition of nums1
        # If partitionX=0, we took nothing from nums1, so use -infinity
        maxLeft1 = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        
        # minRight1: smallest element in right partition of nums1
        # If partitionX=m, we took everything from nums1, so use +infinity
        minRight1 = float('inf') if partitionX == m else nums1[partitionX]
        
        # maxLeft2: largest element in left partition of nums2
        maxLeft2 = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        
        # minRight2: smallest element in right partition of nums2
        minRight2 = float('inf') if partitionY == n else nums2[partitionY]
        
        # Check if we found the correct partition
        # Valid partition: max(left) ≤ min(right) for both arrays
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            # Perfect partition found! Calculate median.
            
            # For odd total length: median is the max of left partition
            if (m + n) % 2 == 1:
                return max(maxLeft1, maxLeft2)
            
            # For even total length: median is average of:
            # - max element from left partition
            # - min element from right partition
            else:
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
        
        # Partition is invalid - adjust binary search
        elif maxLeft1 > minRight2:
            # We took too many elements from nums1
            # The largest from nums1's left > smallest from nums2's right
            # Need to move left: take fewer elements from nums1
            right = partitionX - 1
        
        else:
            # We took too few elements from nums1
            # The largest from nums2's left > smallest from nums1's right
            # Need to move right: take more elements from nums1
            left = partitionX + 1