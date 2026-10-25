def longestConsecutive(nums):
  nn = set(nums)
  best = 0
  for i in nn:
    if i-1 in nn:
      continue
    cnt = 0
    cur = i
    while cur in nn:
      cnt += 1
      cur += 1
    best = max(best, cnt)
  return best

nums = [1, 0, 1, 2, 7, 8, 9, 10]
print(longestConsecutive(nums))
nums = [1, 0, 1, 2, 7, 8]
print(longestConsecutive(nums))
