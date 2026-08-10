class LLNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = self.tail = None
    
    def add(self, node: LLNode):
        node.next = node.prev = None  # Clear stale pointers
        
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.next = node
            node.prev = self.head
            self.head = node
        self.size += 1

    def pop_tail(self):
        if not self.tail:
            return
        if self.size == 1:
            self.head = self.tail = None
            self.size = 0
            return
        
        self.tail = self.tail.next
        self.tail.prev = None
        self.size -= 1

    def pop_head(self):
        if not self.head:
            return
        if self.size == 1:
            self.head = self.tail = None
            self.size = 0
            return
            
        self.head = self.head.prev
        self.head.next = None
        self.size -= 1


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_mapping: dict[int, LLNode] = {}
        self.linked_list = LinkedList()

    def _extract_node(self, node: LLNode):
        # Case 1: Node is both head and tail (only 1 element)
        if node == self.linked_list.head and node == self.linked_list.tail:
            self.linked_list.head = self.linked_list.tail = None
        # Case 2: Node is the head
        elif node == self.linked_list.head:
            self.linked_list.pop_head()
            return  # pop_head already updates size
        # Case 3: Node is the tail
        elif node == self.linked_list.tail:
            self.linked_list.pop_tail()
            return  # pop_tail already updates size
        # Case 4: Node is in the middle
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            
        self.linked_list.size -= 1

    def get(self, key: int) -> int:
        if key not in self.node_mapping:
            return -1
            
        node = self.node_mapping[key]
        self._extract_node(node)
        self.linked_list.add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.node_mapping:
            # Update existing key
            node = self.node_mapping[key]
            node.value = value
            self._extract_node(node)
            self.linked_list.add(node)
        else:
            # Add new key
            if self.linked_list.size == self.capacity:
                # Evict oldest (tail)
                oldest = self.linked_list.tail
                del self.node_mapping[oldest.key]
                self.linked_list.pop_tail()
                
            new_node = LLNode(key, value)
            self.node_mapping[key] = new_node
            self.linked_list.add(new_node)