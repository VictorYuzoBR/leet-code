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


nums = [3,5,5,8]
target = 10
cnums = []
result =[]
aux = 1
stop = False
aux2 = 0
for num in nums:
    if stop == True:
        break
    else:
        for i in range(aux,len(nums)):
            if (num + nums[i]) == target:
                cnums.append(num)
                cnums.append(nums[i])
                stop = True
                break
    aux += 1

for item in cnums:
    count = 1
    for i in range (aux2,len(nums)):
        if item == nums[i]:
            result.append(i)
            break
        else:
            count +=1
    aux2 += count

print(result)
print(cnums)