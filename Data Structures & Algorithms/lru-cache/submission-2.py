from collections import defaultdict
class LRUCache:
    # Time: O(C) C= capacity, Space: O(1)
    # capacity: Capacity of the cache
    # curr_len: Current size of the cache
    # cache: The cache itself. Is a hashmap with the following structure: 
    #    key: int -> [value: int, time: int]
    # tiempo_actual: tracks the time of the cache
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_len = 0
        self.cache = defaultdict(int)
        self.tiempo_actual = 0
    
    # This functions updates the global and the key times
    def update_recent(self, key: int):
        self.tiempo_actual += 1
        self.cache[key][1] = self.tiempo_actual

    # This functions gets the value of a certain key.
    # If the key does not exist, return -1
    def get(self, key: int) -> int:
        if key in self.cache: 
            self.update_recent(key)
            return self.cache.get(key)[0]
        else:
            return -1
        
    # This functions puts or update a key with its value
    def put(self, key: int, value: int) -> None:
        # First, check if the key is already in the cache,
        # if it, update its value
        if key in self.cache:
            self.cache[key][0] = value
            self.update_recent(key)
            return

        # If there's no space in cache, search the key with the minimum time,
        # This is the least recently used element
        if self.curr_len == self.capacity:
            lru_key = None
            menor_tiempo = float('inf')

            for k, tuple_val in self.cache.items():
                if tuple_val[1] < menor_tiempo:
                    menor_tiempo = tuple_val[1]
                    lru_key = k

            del self.cache[lru_key]
            self.curr_len -= 1

        # Then, update time and size and push the new pair
        self.tiempo_actual += 1
        self.cache[key] = [value, self.tiempo_actual]
        self.curr_len += 1
        return
