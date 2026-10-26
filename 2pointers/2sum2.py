def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1
    while l<r:
        if numbers[l] + numbers[r] > target:
            r -= 1
            continue
        if numbers[l] + numbers[r] < target:
            l += 1
            continue
        return [l + 1, r + 1]
    return []
  
print(twoSum([2,7,11,15], 9))
