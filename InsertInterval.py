'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.



Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        arraynewinterval = []
        arraystomerge = []
        newmin = newInterval[0]
        newmax = newInterval[1]
        newarray = []
        intervals2 = []
        for item in intervals:
            auxarray = []
            for i in range(item[0], item[1] + 1):

                if i not in auxarray:
                    auxarray.append(i)
            intervals2.append(auxarray)

        for i in range(newInterval[0], newInterval[1] + 1):
            arraynewinterval.append(i)

        for num in arraynewinterval:
            for j in range(0, len(intervals2)):
                if num in intervals2[j]:
                    arraystomerge.append(j)

        for item in arraystomerge:
            if newmin > intervals[item][0]:
                newmin = intervals[item][0]
            if newmax < intervals[item][1]:
                newmax = intervals[item][1]

        newarray.append([newmin, newmax])

        for i in range(0, len(intervals)):
            if i in arraystomerge:
                continue
            else:
                newarray.append(intervals[i])

        return sorted(newarray)
