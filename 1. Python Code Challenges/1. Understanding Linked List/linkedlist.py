class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def ElementoInicio(self):
        if self.head is not None:
            return self.head.data
        else:
            return None

    def InserirInicio(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def InserirFinal(self, data):
        new_node = Node(data)
        if self.tail is not None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def InserirMeio(self, data, position):
        if position == 0:
            self.InserirInicio(data)
        else:
            current_node = self.head
            current_position = 0
            while current_node is not None and current_position < position - 1:
                current_node = current_node.next
                current_position += 1
            if current_node is not None:
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
                if current_node == self.tail:
                    self.tail = new_node

    def ElementoFinal(self):
        if self.tail is not None:
            return self.tail.data
        else:
            return None

    def MostrarLista(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def Remover(self, data):
        if self.head is not None:
            if self.head.data == data:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            else:
                current_node = self.head
                while current_node.next is not None and current_node.next.data != data:
                    current_node = current_node.next
                if current_node.next is not None:
                    if current_node.next == self.tail:
                        self.tail = current_node
                    current_node.next = current_node.next.next

my_list = LinkedList()
my_list.ElementoInicio()
my_list.InserirInicio(43)
my_list.InserirFinal(89)
my_list.InserirMeio(55,2)
my_list.ElementoFinal()
my_list.MostrarLista()
my_list.Remover(55)
my_list.Remover(43)
my_list.Remover(7)
my_list.Remover(89)
