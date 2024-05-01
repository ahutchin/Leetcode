from typing import List


class Solution:
    def insert1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]: # initial thought to approach
        # Read through interval list 
        # (left to right, but there is likely a better way to search here)
        for i in range(len(intervals)):
            if intervals[i[0]] < newInterval[0] and intervals[i[1]] > newInterval[0]:
                # Case for when a start merge needs to happen
                print('start merge')
            elif intervals[i[0]] < newInterval[1] and intervals[i[1]] > newInterval[1]:
                # Case for when a end merge needs to happen
                print('end merge')
            elif intervals[i[1]] < newInterval[0] and intervals[(i + 1)[0]]:
                # Case for no merge
                print('no merge')


    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]: # Chaning approach 
        # Initialize outputList
        outputList = []
        i = 0

        # Read through & append intervals until intervals[i][1] < newInterval[0]
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            outputList.append(intervals[i])
            i += 1

        # Continue reading through intervals while intervals[i][0] <= newInterval[1]
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        outputList.append(newInterval)

        # Continue reading to the end of intervals while intervals[i][0] > newInterval[1]
        while i < len(intervals) and intervals[i][0] > newInterval[1]:
            outputList.append(intervals[i])
            i += 1
        
        # return
        return outputList
    
# test case
solution = Solution()

intervals = [[1,3],[6,9]]
newInterval = [2,5]

result = solution.insert2(intervals, newInterval)
print(result)

# O(n) space and time complexity