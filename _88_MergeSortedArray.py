class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for ai in nums2:
            self.chen_so(ai, nums1, m)
            m+=1
    

    def chen_so(self, x, arr, m):
        chen_vao_cuoi = False

        for i in range(0,m):
            if (arr[i] > x):
                chen_vao_cuoi = True
                for k in range(m-1,i-1,-1):
                    arr[k+1] = arr[k]
                arr[i] = x
                break
        if chen_vao_cuoi == False:
            arr[m] = x


        
    