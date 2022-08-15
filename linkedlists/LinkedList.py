#implementing a Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            return new_node
    
    # def find_value(self, value):
    #     if self.head is None:
    #         print("Failed to delete from empty list")
    #     else:
    #         current = self.head
    #         if current.value == value:
    #             current.next =
    #             current = current.next
    #         if current.value == value:
    #             current.next = current.next
    #             self.print()
    #         else:
    #             print("Value not found")
    #             self.print()

    
    def delete(self, value):
        if self.head is None:
            print("Failed to delete from empty list")
        else:
            prev = self.head
            current = self.head.next
            while current is not None:
                if current.value == value:
                    prev.next = current.next
                    self.print()
                    return
                else:
                    prev = current
                    current = current.next
            print("Value not found")
          
            
        
    def insert_at_beginning(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    def reverse(self):
        reversed_list = LinkedList()
        if self.head is None:
            print("Empty list")
        else:
            current = self.head
            while current is not None:
                reversed_list.insert_at_beginning(current.value)
                current = current.next
            reversed_list.print()

    
    def print(self):
        list_rep = []
        if self.head is None:
            print("Empty list")
        else:
            current = self.head
            while current is not None:
                list_rep.append(current.value)
                current = current.next
            print(list_rep)
    

    def has_loop(self):
        if self.head is None or self.head.next is None:
            return False
        
        else:
            slower = self.head
            faster = slower.next
            if slower == faster:
                return True
            else:
                slower = slower.next
                faster = faster.next.next
            return False
    def create_loop(self, value):
        last_node = self.append(value)
        last_node.next = self.head
        return self.has_loop()



    
new_one = LinkedList()
new_one.append(1)
new_one.append(4)
new_one.insert_at_beginning(10)
new_one.print()
new_one.reverse()
new_one.delete(4)
new_one.delete(4)
print(new_one.has_loop())
print(new_one.create_loop(12))