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
    def add_front_list(self,data):
        new_node = Node(data)
        temp = self.head
        self.head = new_node
        new_node.Next = temp
        del temp
    def print_List(self):
        print_list = self.head
        while True:
            print(print_list.data)
            if print_list.Next is None:
                break
            print_list = print_list.Next