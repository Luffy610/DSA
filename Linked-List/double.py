class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("The list is empty")
        else:
            temp = self.head
            result = "None <----> "
            while temp:
                result += temp.data + " <----> "
                temp = temp.next
            result += "None"
            print(result)

    def insert_front(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def insert_end(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
            node.prev = temp

    def insert_after(self, element, value):
        node = Node(value)
        if self.head is None:
            raise Exception("Invalid the list is empty")
        else:
            temp = self.head
            while temp:
                if temp.data == element:
                    if temp.next is None:
                        self.insert_end(value)
                    else:
                        node.next = temp.next
                        node.prev = temp
                        temp.next.prev = node
                        temp.next = node
                    break
                temp = temp.next
            else:
                raise Exception("Element not present in the list")

    def insert_before(self, element, value):
        node = Node(value)
        if self.head is None:
            raise Exception("Invalid the list is empty")
        elif self.head.data == element:
            self.insert_front(value)
        else:
            temp = self.head
            while temp:
                if temp.data == element:
                    node.prev = temp.prev
                    node.next = temp
                    temp.prev.next = node
                    temp.prev = node
                    break
                temp = temp.next

    def delete_front(self):
        if self.head is None:
            raise Exception("Invalid the list is empty")
        elif self.head.next is None:
            self.head = None
        else:
            self.head.next.prev = None
            self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            raise Exception("Invalid the list is empty")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.prev.next = None
            temp.prev = None

    def delete_node(self, value):
        if self.head is None:
            raise Exception("Invalid the list is empty")
        elif self.head.data == value:
            self.delete_front()
        else:
            temp = self.head
            while temp:
                if temp.data == value:
                    if temp.next is None:
                        self.delete_end()
                    else:
                        temp.prev.next = temp.next
                        temp.next.prev = temp.prev
                        temp.next = None
                        temp.prev = None
                    break
                temp = temp.next
            else:
                raise Exception('Element not present in the list')

    def search(self, value):
        if self.head is None:
            raise Exception("Invalid the list is empty")
        else:
            index = 0
            temp = self.head
            while temp:
                if temp.data == value:
                    print(index)
                    break
                temp = temp.next
                index += 1
            else:
                raise Exception('Element not present in the list')

    def reverse(self):
        if self.head is None:
            raise Exception("Invalid the list is empty")
        else:
            back = None
            current = self.head
            while current:
                front = current.next
                current.prev = front
                current.next = back
                back = current
                current = front
            self.head = back

    def length(self):
        if self.head is None:
            print(0)
        else:
            count = 0
            temp = self.head
            while temp:
                temp = temp.next
                count += 1
            print(count)


def display_menu():
    print("====================================================================")
    print("Menu:")
    print("1. Insert At Front")
    print("2. Insert At End")
    print("3. Insert After Element")
    print("4. Insert Before Element")
    print("5. Delete From Front")
    print("6. Delete From End")
    print("7. Delete A Node")
    print("8. Search for a element")
    print("9. Reverse a the list")
    print("10. Length the list")
    print("====================================================================")


if __name__ == "__main__":
    double_list = DoubleLinkedList()
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = input("Enter the data you want to insert: ")
            double_list.insert_front(data)
            double_list.print_list()
        elif choice == 2:
            data = input("Enter the data you want to insert: ")
            double_list.insert_end(data)
            double_list.print_list()
        elif choice == 3:
            ele = input("Enter the element after which you want to insert: ")
            data = input("Enter the data you want to insert: ")
            double_list.insert_after(ele, data)
            double_list.print_list()
        elif choice == 4:
            ele = input("Enter the element before which you want to insert: ")
            data = input("Enter the data you want to insert: ")
            double_list.insert_before(ele, data)
            double_list.print_list()
        elif choice == 5:
            double_list.delete_front()
            double_list.print_list()
        elif choice == 6:
            double_list.delete_end()
            double_list.print_list()
        elif choice == 7:
            ele = input("Enter the element before which you want to delete: ")
            double_list.delete_node(ele)
            double_list.print_list()
        elif choice == 8:
            ele = input("Enter the element before which you want to search: ")
            double_list.search(ele)
        elif choice == 9:
            double_list.reverse()
            double_list.print_list()
        elif choice == 10:
            double_list.length()
        else:
            break
