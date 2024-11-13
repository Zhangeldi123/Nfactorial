def search(nums, target: int):
        r = len(nums) - 1
        l = 0
        while l <= r:
            m = int(l + ((r - l) / 2))
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

nums = [5]
target = 5
print(search(nums, target))