class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        counter, start, end = 0, 0, len(nums) - 1

        while (start < end):
            if(nums[start] + nums[end] == k):
                counter += 1
                start += 1
                end -= 1
            elif(nums[start] + nums[end] < k):
                start += 1
            else:
                end -= 1

        return counter