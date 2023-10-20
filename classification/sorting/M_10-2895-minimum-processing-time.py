class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        #lct: sorting;
        #lcd: M_10;
        processorTime.sort()
        tasks.sort()
        j = 0
        ans = 0
        for i in range(len(tasks)-1,-1,-4):
            ans = max(ans,tasks[i]+processorTime[j])
            j+=1
            
        return ans
            