from collections import OrderedDict
class LRUCache:
    # Time: O(1), Space: O(1)
    # This solution uses OrderedDict.
    # OrderedDict is a hybrid between a hashmap and a double linked list.
    # The hashmap is where our cache is stored,
    # and the double linked list manages the time of each pair,
    # the head is the least recently used pair (LRU), 
    # and the tail is the most recently used pair.
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    # This functions gets the value of a certain key.
    # If the key does not exist, return -1
    def get(self, key: int) -> int:
        if key in self.cache: 
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1
        
    # This functions puts or update a key with its value
    def put(self, key: int, value: int) -> None:
        # If the key is in cache, we move the node to the end of the linked list
        if key in self.cache:
            self.cache.move_to_end(key)
        
        # First, we push the new pair in the cache
        self.cache[key] = value

        # Then, pop the head, that is the LRU
        # Last=False means that pops the head, not the tail
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)