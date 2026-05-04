class Solution:
    # Time: O(n), Space: O(1)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # If n = 0, that means wont be any idle task, so, return the length of tasks
        if n == 0: return len(tasks)

        # First, create the fixed array to store all frequencies
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        # Next, we count all letters that has the maximum frecuency
        # This letters will remain at the end of the tasks sequence
        maxFreq = max(count)
        maxCount = 0
        for i in count:
            maxCount += 1 if i == maxFreq else 0
        
        # Then, we calcule the minimum time by the following formula:
        # - (maxFreq - 1) represents the number of full chunks.
        #   A full chunk is a set of tasks that includes the letter with the biggest frequency
        #   and its "idle" tasks
        # - (n + 1) represents the length of a full chunk, that is n idles tasks and the letter
        # - maxCount is the number of letters remaining at the end of the sequence
        time = (maxFreq - 1) * (n + 1) + maxCount
        return max(len(tasks), time)
        