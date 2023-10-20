class Solution:
    # lct:twopointer;
    def maxArea(self, height: List[int]) -> int:
        l ,r = 0,len(height)-1
        ans = 0
        while l < r:
            current = min(height[l],height[r]) *(r-l)
            ans = max(current,ans)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return ans

        