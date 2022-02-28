
class Dlist:
    def __init__(self, key :int , valu: int):
        self.key = key
        self.value = valu
        self.pre = None
        self.next = None
class LRU:

    def __init__(self, capacity: int):
        self.head = Dlist(-1,-1)
        self.tail = Dlist(-1,-1)
        if 1:
            self.head.pre = None
            self.head.next = self.tail

            self.tail.pre = self.head
            self.tail.next = None

        self.hash_node = {}
        self.capacity = capacity


    def put(self, key: int, value: int):
        node = None
        if key in self.hash_node.keys():
            node = self.hash_node[key]
            if node.value != value:
                node.value = value
            if 1:
                pre_node = node.pre
                next_node = node.next
                pre_node.next = next_node
                next_node.pre = pre_node
        else:
            if len(self.hash_node) == self.capacity:
                #print(f"haslen:{len(self.hash_node)}")
                delete_node = self.tail.pre
                delete_node_pre = delete_node.pre

                delete_node_pre.next = self.tail
                self.tail.pre = delete_node_pre

                delete_node.pre = None
                delete_node.next = None

                del self.hash_node[delete_node.key]

            node = Dlist(key,value)
            self.hash_node[key] = node

        old_first = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = old_first
        old_first.pre = node


    def get(self, key: int):
        if key not in self.hash_node.keys():
            return -1
        node = self.hash_node[key]

        if self.head.next.key == key:
            return self.head.next.value

        if 1:
            pre_node = node.pre
            next_node = node.next
            pre_node.next = next_node
            next_node.pre = pre_node
        old_first = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = old_first
        old_first.pre = node
        return node.value


    def show(self):
        cur_node = self.head.next
        print(f"-----")
        while cur_node != self.tail:
            print(f" {cur_node.value}")
            cur_node = cur_node.next
        for  key ,value in self.hash_node.items():
           #print(f"__ {key} {value.value}")
            pass



if __name__ == "__main__":
    lru = LRU(1)

    #["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    #[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    lru.put(2,1)
    lru.show()
    print(f"get ：{lru.get(1)}")
    lru.show()
