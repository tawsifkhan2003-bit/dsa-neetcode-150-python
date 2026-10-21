def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1] * len(nums) #[1 for x in nums]
        pfx = 1
        sfx = 1
        for i, x in enumerate(nums):
            answer[i] = pfx
            pfx *= x
        for j in range(len(nums)-1, -1, -1):
            answer[j] *= sfx
            sfx *= nums[j]
        return answer

nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))
