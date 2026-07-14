class Node:
    def __init__(self, key, value):
        self.key = key
        self.data = value
        self.prev = None
        self.next = None

cap = 0
cache = {}
head = Node("head","dummy")
tail = Node("tail","dummy")
head.next = tail
tail.prev = head

def get(key):
    if cache.get(key) is None:
        return "NOT_FOUND"
    node = cache.get(key)
    remove(node)
    add_to_tail(node)
    return cache.get(key).data

def remove(node):
    curr = node
    first = curr.prev
    second = curr.next
    first.next = second
    second.prev = first

def add_to_tail(node):
    last = tail.prev

    last.next = node
    node.prev = last

    node.next = tail
    tail.prev = node

def put(key, value):

    node = cache.get(key)
    if node:
        remove(node)
        add_to_tail(node)
        node.data=value
    else:
        if cap == len(cache):
            lru = head.next
            remove(lru)
            del cache[lru.key]
        cache[key] = Node(key, value)
        add_to_tail(cache[key])

    return "OK"

def capacity(value):
    global cap
    if value <= 0:
        return "ERROR"
    cap = value
    return "OK"

while True:
    try:
        line = input().strip()
    except EOFError:
        break

    if not line:
        continue
    line = line.split()
    command = line[0]
    if command == "PUT":
        key = line[1]
        value = line[2]
        print(put(key, value))
    elif command == "GET":
        key = line[1]
        print(get(key))
    elif command == "CAPACITY":
        value = int(line[1])
        capacity(value)
'''
Rough work
head < - > tail
100         200
A 300
NULL head 300 < - >100 A 200< - > 300 tail NULL
100                300        200

extract tail.prev (100)
assign to Node.prev
assign to tail.prev = currnode
currnode.next = tail
Node.prev.next = currnode

NULL head 200 <-> 100 tail NULL
100                 200

Node A = 300
curr = node
first = curr.prev
second = curr.next
first.next = second
second.prev = first

'''
