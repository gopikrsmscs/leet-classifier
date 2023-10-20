class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        sorted_array = []
        #lct: orderedset,binarysearch;
        min_ans = abs(nums[0] - nums[-1])
        for i in range(x,len(nums)):
            insort(sorted_array,nums[i-x]) 
            pos = bisect_left(sorted_array,nums[i])
            if pos < len(sorted_array):
                min_ans = min(min_ans,abs(sorted_array[pos]-nums[i]))
            min_ans = min(min_ans,abs(sorted_array[pos-1]-nums[i]))  
        return min_ans

        