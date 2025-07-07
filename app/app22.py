#NODES#
class Node:
    def __init__(self, data):
        self.data = data
        self.next=None
node1=Node(1)
node2=Node(2)
node3=Node(3)
node1.next=node2
node2.next=node3
node3.next=node1
now=node1
while True:
    print(now.data)
    now=now.next
    if now==node1:
        break