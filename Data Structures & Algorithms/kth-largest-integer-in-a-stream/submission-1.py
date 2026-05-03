from heapq import heappush, heappop, heapify
class KthLargest:
    # Time: O(m log k) Space: O(k), k = number of calls made to add()
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k

        # We initialize the class by first put all items of nums in a min heap
        heapify(nums)

        # Then, we pop the elements from the heap until the heap has only k elements
        # Each time we pop an element from the heap,
        # the next element at the root will be greater than the previous one,
        # so, if we pop unitl the heap has only k elements, 
        # at the end, the root will be the kth element.
        while len(self.heap) > self.k:
            heappop(self.heap)

    # When we add a element, then we need to remove an element
    # if the heap has more than k elements.
    # Finally, we return the smallest element, the first element of the heap
    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]
