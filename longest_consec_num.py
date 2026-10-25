def longestConsecutive(self, nums):
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
