class Solution:
    # BRUTE FORCE
    # def twoSum(self, arr, target):
    #     lim = len(arr)
    #     for i in range(0, lim):
    #         for j in range(i + 1, lim):
    #             if arr[i] + arr[j] == target:
    #                 return [i, j]

    # Using hash map and with each iteration making a check if the target solution already exists or not
    def twoSum(self, arr, target):
        soln = {}
        for i in range(len(arr)):
            k = soln.get(target - arr[i])
            if i == k:
                continue
            if k != None and arr[i] + arr[k] == target:
                return [k, i]
            soln[arr[i]] = i


# sol = Solution()
# print(sol.twoSum([2, 7, 11, 15], 9))
# print(sol.twoSum([3, 2, 4], 6))
# print(sol.twoSum([3, 3], 6))