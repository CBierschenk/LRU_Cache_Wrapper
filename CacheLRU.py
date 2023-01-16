'''The CacheLRU class is a cache data structure using a hashmap (dict) to access the elements in the cache, which are stored in a double linked list. The head is the most recently used and the tail the least recently used element (replacement element).'''

class NodeDLL:
    data = None
    prev = None
    next = None

    def __init__(self, data):
        self.data = data


class CacheLRU:
    hash_map = {}
    head = None
    tail = None
    cache_size = None

    def __init__(self, c_size):
        self.cache_size = c_size

    '''
    Description: Checks if the cache is full (return True if len(hash_map) == cache_size else False)
    @return: bool
    '''
    def full(self):
        return True if len(self.hash_map) == self.cache_size else False

    def empty(self):
        return True if len(self.hash_map) == 0 else False

    '''
    Description: Updates the found node (from hash_map) to the head. Therefore reconnect found node's prev and next node and put found node as head.
    @param: identifier - identifier to identify the node in the hash_map
    '''
    def update(self, identifier):
        if(self.hash_map[identifier] == self.tail):
            self.tail = self.tail.prev

        existing_node = self.hash_map[identifier]
        existing_node.prev.next = existing_node.next
        existing_node.next.prev = existing_node.prev
        existing_node.prev = None
        existing_node.next = self.head
        self.head.prev = existing_node
        self.head = existing_node

    
    '''
    Description: Deletes the LRU node, which is the tail node
    @param: identifier - identifier to identify the node in the hash_map
    '''
    def delete(self):
        key = list(filter(lambda x:self.hash_map[x] == self.tail, self.hash_map))[0]
        self.hash_map.pop(key)
        self.tail = self.tail.prev

    
    '''
    Description: Inserts a new node infront of the head and makes the new node to the head.
    @param: identifier - identifier to identify the node in the hash_map
    '''
    def insert(self, identifier, data):
        new_node = NodeDLL(data)
        
        if self.empty():
            self.head = new_node
            self.tail = new_node

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

        if self.full():
            self.delete()

        self.hash_map[identifier] = new_node
