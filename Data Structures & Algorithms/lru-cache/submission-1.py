from collections import defaultdict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_len = 0
        self.cache = defaultdict(int)
        self.tiempo_actual = 0
    
    def update_recent(self, key: int):
        self.tiempo_actual += 1
        self.cache[key][1] = self.tiempo_actual

    def get(self, key: int) -> int:
        if key in self.cache: 
            self.update_recent(key)
            return self.cache.get(key)[0]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key][0] = value
            self.update_recent(key)
            return

        if self.curr_len == self.capacity:
            lru_key = None
            menor_tiempo = float('inf')

            for k, tuple_val in self.cache.items():
                if tuple_val[1] < menor_tiempo:
                    menor_tiempo = tuple_val[1]
                    lru_key = k

            del self.cache[lru_key]
            self.curr_len -= 1

        self.tiempo_actual += 1
        self.cache[key] = [value, self.tiempo_actual]
        self.curr_len += 1
        return
