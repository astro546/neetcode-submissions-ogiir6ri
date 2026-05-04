class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0: return len(tasks)
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        maxFreq = max(count)
        maxCount = 0
        for i in count:
            maxCount += 1 if i == maxFreq else 0
        
        time = (maxFreq - 1) * (n + 1) + maxCount
        return max(len(tasks), time)
        