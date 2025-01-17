class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1 
        maxArea = 0
        while(left<right):
            curr_area = min(height[left],height[right]) * (right-left) #area=l*b
            maxArea = max(maxArea,curr_area)

            if(height[left] < height[right]):
                left = left + 1
            else:
                right = right - 1
        return maxArea
            
