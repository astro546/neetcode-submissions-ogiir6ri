class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #2 O(n)
        #It's O(n) 'cause the iner loop in the final loop does not takes a constant numer of steps
        #and the number of steps is < n
        freq_map = defaultdict(int)
        freq_arr = [[] for i in range(len(nums) + 1)]
        for num in nums:
            freq_map[num] += 1

        for num, freq in freq_map.items():
            freq_arr[freq].append(num)

        res = []
        for i in range(len(freq_arr) - 1, 0, -1):
            for num in freq_arr[i]:
                res.append(num)
                if len(res) == k:
                    return res

        

        #1 O(n log n)
        #freq_map = defaultdict(int)
        #for num in nums:
        #    freq_map[num] += 1
        
        #return sorted(freq_map, key= freq_map.get, reverse=True)[:k]