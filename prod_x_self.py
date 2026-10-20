"""brute:
	r = []
        p = 1
        for i in nums:
            for j in nums:
                if i != j:#this is a bug, what if [2, 2, 3],Fix: iterate with indices. for i in range(len(nums)): for j in range(len(nums)): if i != j: ...
                    p *= j
            r.append(p)
            p = 1"""
