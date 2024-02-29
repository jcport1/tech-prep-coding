# https://leetcode.com/problems/meeting-rooms-ii/description/

class Solution:
    def minMeetingRooms(self, intervals) -> int:

        # approach: two pointers with two sorted arrays
        # time complexity: O(n log n) => sorting algorithm
        # space complexity: O(n) => extra space for start/end time arrays

        # extract start and end times and add to sep
        start_times = sorted([subarr[0] for subarr in intervals])
        end_times = sorted([subarr[1] for subarr in intervals])

        print(start_times)
        print(end_times)

        # initialize start, end pointers
        s, e = 0, 0

        # track minConferenceRms and curRmCount
        # res => min num of conference rooms required to hold meetings == max of overlaps or number of meetings occuring at same time
        # i.e. a meeting has started before another 1 has finished (this means we need another room)
        res, curRmCount = 0,0

        # loop through start times while we have meetings

        while s < len(intervals):
            # if a meeting is started before a meeting has ended, increment num of rooms required
            # move start pointer
            if start_times[s] < end_times[e]:
                curRmCount += 1
                s += 1
            # else a meeting has ended, so decrement count of curRm, move end time pointer to next end time
            else: 
                curRmCount -= 1
                e += 1

            # track maximum by evaluting cur room count at a given time
            res = max(res, curRmCount)

        
        return res