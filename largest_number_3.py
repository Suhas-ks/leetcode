def counting_sort(arr):
    counter = [0] * 10
    length = len(arr)
    for i in range(length):
        counter[arr[i]] += 1
        arr[i] = 0
    i = 0
    while 




class Solution:
    def largestMultipleOfThree(self, digits):
