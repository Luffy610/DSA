class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("The List is empty")
        else:
            result = ""
            temp = self.head
            while temp:
                result += (temp.data + " --> ")
                temp = temp.next
            result += "None"
            print(result)

    def get_length(self):
        count = 0
        if self.head is None:
            return count
        else:
            temp = self.head
            while temp:
                count += 1
                temp = temp.next
            return count

    def insert_at_front(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insert_at_end(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

    def insert_after(self, element, value):
        node = Node(value)
        if self.head is None:
            raise Exception("Invalid, the list is empty")
        else:
            temp = self.head
            while temp:
                if temp.data == element:
                    node.next = temp.next
                    temp.next = node
                    break
                temp = temp.next
            else:
                raise Exception("Element not present in the list")

    def insert_before(self, element, value):
        node = Node(value)
        if self.head is None:
            raise Exception("Invalid, the list is empty")
        elif self.head.data == element:
            node.next = self.head
            self.head = node
        else:
            temp = self.head
            while temp.next:
                if temp.next.data == element:
                    node.next = temp.next
                    temp.next = node
                    break
                temp = temp.next
            else:
                raise Exception("Element not present in the list")

    def delete_front(self):
        if self.head is None:
            raise Exception("Invalid the list is empty")
        else:
            self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            raise Exception("Invalid the list is empty")
        elif self.get_length() == 1:
            self.head = None
        else:
            prev = None
            temp = self.head
            while temp.next:
                prev = temp
                temp = temp.next
            prev.next = None

    def delete_node(self, element):
        if self.head is None:
            raise Exception("Invalid the list is empty")
        elif self.head.data == element:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next:
                if temp.next.data == element:
                    temp.next = temp.next.next
                    break
                temp = temp.next
            else:
                raise Exception("Element not present in the list")

    def search(self,element):
        if self.head is None:
            raise Exception("Invalid the list is empty")
        else:
            index = 0
            temp = self.head
            while temp:
                if temp.data == element:
                    return index
                temp = temp.next
                index += 1
            else:
                raise Exception("Element not present in the list")

    def reverse(self):
        if self.head is None:
            raise Exception("Invalid the list is empty")
        else:
            prev = None
            temp = self.head
            while temp:
                new = temp.next
                temp.next = prev
                prev = temp
                temp = new
            self.head = prev


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
    single_list = SingleLinkedList()
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = input("Enter the data you want to insert: ")
            single_list.insert_at_front(data)
            single_list.print_list()
        elif choice == 2:
            data = input("Enter the data you want to insert: ")
            single_list.insert_at_end(data)
            single_list.print_list()
        elif choice == 3:
            ele = input("Enter the element after which you want to insert: ")
            data = input("Enter the data you want to insert: ")
            single_list.insert_after(ele, data)
            single_list.print_list()
        elif choice == 4:
            ele = input("Enter the element before which you want to insert: ")
            data = input("Enter the data you want to insert: ")
            single_list.insert_before(ele, data)
            single_list.print_list()
        elif choice == 5:
            single_list.delete_front()
            single_list.print_list()
        elif choice == 6:
            single_list.delete_end()
            single_list.print_list()
        elif choice == 7:
            ele = input("Enter the element before which you want to delete: ")
            single_list.delete_node(ele)
            single_list.print_list()
        elif choice == 8:
            ele = input("Enter the element before which you want to search: ")
            res = single_list.search(ele)
            print(res)
        elif choice == 9:
            single_list.reverse()
            single_list.print_list()
        elif choice == 10:
            res = single_list.get_length()
            print(res)
        else:
            break
