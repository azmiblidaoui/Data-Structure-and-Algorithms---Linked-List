class Node:
    def __init__(self,data):
        self.data = data
        self.Next = None #Pointer to Node
class linled_List:
    def __init__(self):
        self.head = None #Pointer to first node
    def add_last_list(self,data):
        new_Node = Node(data)
        if self.head is None:
            self.head = new_Node
        else:
            curr = self.head
            while curr.Next is not None:
                if curr.Next is None:
                    break
                curr = curr.Next
            curr.Next = new_Node