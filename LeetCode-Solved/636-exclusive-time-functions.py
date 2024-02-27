# https://leetcode.com/problems/exclusive-time-of-functions/description/

class Solution:
    def exclusiveTime(self, n: int, logs):

        # time complexity: O(n) -> loop through logs n times
        # space complexity: O(n) -> execution_times is len n

        # array for execution times. initalize to 0
        execution_times = [0] * n

        # create call stack for function calls
        call_stack = []

        # keep track of prev start time to calculate execution time
        prev_start = 0

        # loop through logs: add to call stack or pop from call stack
        for log in logs:
            # parse the log
            func_id, func_type, timestamp = log.split(":")

            # convert func_id and timestamp to integers
            func_id = int(func_id)
            timestamp = int(timestamp)

            # add func to call stack
            if func_type == "start":
                # if we have func in the call stack, update execution time of func at top of stack
                if call_stack:
                    execution_times[call_stack[-1]] += timestamp - prev_start
                
                call_stack.append(func_id)
                # update prev_start
                prev_start = timestamp
            # else - func type is end, so pop off from stack and update execution time
            else:
                # calculate delta between time stamp and prev start. Add 1 since time units are inclusive 
                execution_times[call_stack.pop()] += timestamp - prev_start + 1

                # update prev_start -> new start time starts 1 unit up from end of timestamp
                prev_start = timestamp + 1
        
        return execution_times