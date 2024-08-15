'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''


nums = [3, 2, 4, 8, 15]
target = 10
cnums = []
aux2 = 0
v = False
for x in nums:
    aux = 0

    while aux < len(nums):
        if nums[aux] == x:
            x = x
        else:
            if x + nums[aux] == target:
                cnums.append(aux2)
                cnums.append(aux)
                v = True
        aux = aux + 1
    aux2 += 1
    if v == True:
        break
print(cnums)