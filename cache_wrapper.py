'''
    This code provides a cache wrapper function to increase performance by storing objects in an cache. The replacement strategy is LRU := least recently used, if all N cache - lines are in use.

    The implementation is based on the following rules:
    1) The cache is not full and current obj. haven't been in the cache, yet -> insert obj. in cache, mark as most recently used.
    2) Current obj. is in the cache -> cache hit := update obj. to most recently used and use cache obj.
    3) The cache is full and obj. haven't been in the cache, yet -> LRU replacement.

    Design decisions:
    1) Implementation via "dict" brute-force, but not optimal with increasing cache size N. Time Complexity: ~ O(N)
    2) Implementation via "double-linked-list" to track the most recently used obj. (head) and least recently used obj. (tail) in combination with a hash table to keep track of the obj. position in the cache. Optimal space and time complexity: ~O(1).   
'''


'''
Description: 
'''
def cache_wrapper_function(identifier, function, cache_obj): 
    if identifier in cache_obj.hash_map:
        print("CACHE HIT: Update and return cached value")
        cache_obj.update(identifier)
        return cache_obj.hash_map[identifier], True
    else:
        print("Cache MISS: Call wrapped function and store in cache")
        data = function(identifier)
        cache_obj.insert(identifier, data)
        return data, False