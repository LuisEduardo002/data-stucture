class SingleLinkedList:

    class Node:

        def __init__(self, value):
            self.value = value
            self.next = None

    """ Por fuera de la clase nodo """

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def show_list(self):
        # 1. Declarar una array vacío que contendraá los valores de los nodos de SLL
        array_with_nodes_value = list()
        current_node = self.head
        # Mientras el nodo actual que estoy visitando sea diferente de None
        while (current_node != None):
            # Añado al final de la lista el valor extraido del nodo
            array_with_nodes_value.append(current_node.value)
            # Visito el próximo nodo antes de salir del while
            current_node = current_node.next
        # Imprimimos la lista
        return array_with_nodes_value

    def create_node_sll_ends(self, value):
        # Creamos una variable que va a tener la estructura de un nodo
        new_node = self.Node(value)
        # Validar si la SLL tiene nodos o no
        if self.head == None:
            # Al nuevo nodo se convierte en la cabeza y cola de la lista
            self.head = new_node
            self.tail = new_node
        else:
            # Si ingresa en esta condición, es porque ya existe al menos un nodo
            # 1. Debemos relacionar al nuevo nodo con la cola de la lista
            # 2. Convertir al nuevo nodo en la cola de la lista
            self.tail.next = new_node
            self.tail = new_node
        # Incrementamos en 1 el tamaño de la lista
        self.length += 1

    def create_node_sll_unshift(self, value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            print(self.head.value)
        else:
            new_node.next = self.head
            self.head = new_node
        # Incrementamos en 1 el tamaño de la lista
        self.length += 1

    def delete_node_sll_pop(self):
        if self.length == 0:
            print('>> Lista vacía no hay nodos por eliminar <<')
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            current_node = self.head

            while current_node.next != self.tail:
                current_node = current_node.next
            
            self.tail = current_node
            self.tail.next = None
            self.length -= 1

    '''Eliminar nodo al inicio de la lista'''

    def shift_node_sll(self):
        if self.length == 0:
            print('>> Lista vacía no hay nodos por eliminar <<')
        elif self.length == 1:

            self.head = None
            self.tail = None
            self.length -= 1
        else:
            remove_node = self.head
            print(f'Valor del nodo a eliminar es: {remove_node.value}')
            self.head = remove_node.next
            self.length -= 1

    def get_node(self, index):
        if index < 1 or index > self.length:
            return None
        elif index == 1:
            return self.head
        elif index == self.length:
            return self.tail
        else:
            current_node = self.head
            node_counter = 1
            while (index != node_counter):
                current_node = current_node.next
                node_counter += 1
            return current_node

    def get_node_value(self, k):
        if index < 1 or index > self.length:
            print('No se encontro')
        elif index == 1:
            print(self.head.value)
        elif index == self.length:
            print(self.tail.value)
        else:
            current_node = self.head
            node_counter = 1
            #Validar que el nodo a consultar sea el mismo del contador
            while (index != node_counter):
                current_node = current_node.next
                node_counter += 1
            print(current_node.value)

    def update_node_value(self, index, new_value):
        if index < 0 or index > self.length or self.head == None :
            return None
        elif index == self.length-1:
            self.tail.value= new_value
        elif index == 0:
            self.head.value = new_value
        else:
            current = self.head
            for i in range(index+1):
                if i == index:
                    current.value=new_value
                    break
                current= current.next

    def remove_node(self, index):
        if index < 0 or index > self.length or self.head == None :
            return None
        elif index == self.length-1:
            self.delete_node_sll_pop()
        elif index == 0:
            self.shift_node_sll()
        else:
            current = self.head
            for i in range(index):
                if i == index-1:
                    current.next=current.next.next
                    break
                current= current.next
            self.length-=1



#Codigo nuevo del taller

    #Obtiene el tamaño de la lista 
    def get_list_lenght(self):
        return self.length

    #Obtiene la posicion del valor ingresado
    def get_value_index(self, value):
        current_node = self.head
        index = 0
        #Validar que el nodo a consultar sea el mismo del contador
        while current_node != None:
            if current_node.value == value:
                return index+1
            index += 1
            current_node = current_node.next
        print("No se encontro")
        return -1

    #Invierte la Lista SLL
    def reverse_sll(self):

        previous = None  #guardo el nodo anterior y el actual
        current = self.head
        guardar = self.head

        while current != None:  # Hasta que llegue a null
            after = current.next  # guardo el nodo siguiente
            current.next = previous  # el actual ahora apunta al anterior
            previous = current  #  el anterior se vuelve el actual
            current = after  # el actual se vuelve el siguiente
        self.head = previous
        self.tail = guardar

    #Elimina todos los nodos
    def remove_all_nodes(self):
        for i in range(self.length):
            self.delete_node_sll_pop()

    #Ordena la SLL
    def sort_sll(self):
        n = self.length

        swapped = False

        for i in range(n - 1):
            current = self.head
            for j in range(0, n - i - 1):

                if current.value > current.next.value:
                    swapped = True
                    x = current.value
                    current.value = current.next.value
                    current.next.value = x
                
                current = current.next
                if j == n-2:
                    self.tail = current
                
            if not swapped:
                return
    #Inserta un valor a la SLL en un determinado index
    def insert_value_at_index(self, value, index):

        if index < 0 or index > self.length :
            return None
        
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node  
            self.length += 1
        elif index == 0:
            self.create_node_sll_unshift(value)
        elif index == self.length:
            self.create_node_sll_ends(value)
        else:
            current = self.head
            before = None

            node_counter = 0
            while current:
                if node_counter == index :
                    print("uwu")
                    before.next = new_node
                    new_node.next = current
                    break
                before = current
                current = current.next
                node_counter += 1
            self.length += 1

    #Retorna true si la SLL esta vacia
    def is_sll_empty(self):
        if self.length == 0:
            return True
        return False
