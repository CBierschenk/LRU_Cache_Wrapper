import CacheLRU
from TestStub import get_book_info
from cache_wrapper import cache_wrapper_function

#Define cache size
CACHE_SIZE = 10

#Define cache object to hold saved lookups
CACHE = CacheLRU.CacheLRU(CACHE_SIZE)

if __name__ == "__main__":

    #Test1: Cache class empty method
    assert(CACHE.empty())
    print("Test1 Succesful: Cache empty")

    #Test2: Insertion in not full cache - push 8 different elements in the cache through function wrapper call
    for x in range(8):
        ret_obj, cached = cache_wrapper_function(str(x), get_book_info, CACHE)
        assert(not cached)

    print("Test2: Succesful: 8 x function call -> miss")

    #Test3: Hit test - Find cached value
    ret_obj, cached = cache_wrapper_function('1', get_book_info, CACHE)
    assert(cached)
    print("Test3 Succesful: 1x function call -> hit")
    
    #Test4: Check update after hit
    assert(CACHE.head == CACHE.hash_map['1'])
    print("Test4 Succesful: Head points to right position")

    #Test5: Check length of chache
    assert(len(CACHE.hash_map) == 8)
    print("Test5 Succesful: Cache is not full and has still 8 entries")

    #Test6: Check cache full method
    ret_obj, cached = cache_wrapper_function('8', get_book_info, CACHE)
    ret_obj, cached = cache_wrapper_function('9', get_book_info, CACHE)
    assert(CACHE.full())
    print("Test6 Succesful: Cache is full now, lets check replacement")

    #Test7 & 8: Insertion in full cache
    ret_obj, cached = cache_wrapper_function('11', get_book_info, CACHE)
    assert(CACHE.head == CACHE.hash_map['11'] and len(CACHE.hash_map) == 10)
    if '0' in CACHE.hash_map:
        assert(False)
    print("Test7: Succesful: LRU value ('0') replaced and cache still full")
    

    ret_obj, cached = cache_wrapper_function('132', get_book_info, CACHE)
    assert(CACHE.head == CACHE.hash_map['132'] and CACHE.full())
    if '2' in CACHE.hash_map:
        assert(False)
    print("Test8: Succesful: LRU value ('2') replaced and cache still full")

    print("All test succesfull")

    