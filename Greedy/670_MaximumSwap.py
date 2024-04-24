class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [int(i) for i in str(num)]
        task_index = {val: i for i,val in enumerate(nums)}

        for i in range(len(nums)):
            for d in range(9,nums[i],-1):
                if d in task_index and task_index[d] > i:
                    nums[i],nums[task_index[d]] = nums[task_index[d]],nums[i]
                    return int("".join(map(str,nums)))
        return num


        
