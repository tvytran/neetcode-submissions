class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        mid = total//2

        if len(nums1) > len(nums2):
            A = nums2
            B = nums1
        else:
            A = nums1
            B = nums2
        l = 0
        r = len(A)-1

        while True:
            m = (l+r)//2
            #print("m = ", m)
            j = mid-m-2
            
            Aleft = A[m] if m >= 0 else float("-infinity")
            Aright = A[m+1] if (m+1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            if Aleft > Bright:
                r = m-1
            elif Bleft > Aright:
                l = m+1
            else:
                break
        
        if total%2 == 0:
            return (max(Aleft, Bleft)+min(Aright, Bright))/2
        else:
            return min(Aright, Bright)
