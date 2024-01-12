# Animal Shelter
# an animal shelter holds dogs and cats and operates under FIFO basis
# People must adopt "oldest" (arrival time) of all animals in shelter, OR
# adopt either a dog or cat, and will receive the oldest of the type. 

#create a class that implements:
# enqueue, dequeueAny, dequeueDOg, dequeueCat. You may also use a LinkedList data structure. 

class AnimalNode():
    def __init__(self, a_type=0, order=0):
        self.val = a_type
        self.order = order
        self.next = None

class AnimalShelter():
    def __init__(self):
        self.animal_count = 0
        self.head_dog = None
        self.head_cat = None
        self.animal_count_out = 0
        

    def reset_head(self, head):
        if head.next:
            head = head.next
        return head

    def append_node(self, new_node):
        node = None
        if new_node.val == 1 and self.head_dog == None:
            self.head_dog = new_node
            return
        elif new_node.val == 0 and self.head_cat == None:
            self.head_cat = new_node
            return
        node = self.head_dog if new_node.val == 1 else self.head_cat
        while node.next != None:
            node = node.next
        node.next = new_node

    def enqueue(self, a_type:int):
        a_type = 1 if a_type else 0
        animal = AnimalNode(a_type, self.animal_count)
        self.animal_count += 1
        self.append_node(animal)

        
    def dequeueAny(self):
        animal = ""
        number = 0
        if self.head_dog.order < self.head_cat.order: 
            animal = "dog"
            number = self.head_dog.order
            new_head = self.reset_head(self.head_dog)
            self.head_dog = new_head
        else:
            animal = "cat"
            number = self.head_cat.order
            new_head = self.reset_head(self.head_cat)
            self.head_cat = new_head
            
        self.animal_count_out += 1

        print(f"Your {animal} #{number} is ready for adoption")

    def dequeueDog(self):
        animal = "dog"
        number = self.head_dog.order
        new_head = self.reset_head(self.head_dog)
        self.head_dog = new_head
        print(f"Your {animal} #{number} is ready for adoption")

    def dequeueCat(self):
        animal = "cat"
        number = self.head_cat.order
        new_head = self.reset_head(self.head_cat)
        self.head_cat = new_head
        print(f"Your {animal} #{number} is ready for adoption")

    def peekQueue(self):
        dog = []
        cat = []
        node_dog = self.head_dog
        node_cat = self.head_cat
        if node_dog != None:
            while node_dog.next != None:
                dog.append([node_dog.order, node_dog.val])
                node_dog = node_dog.next
            dog.append([node_dog.order, node_dog.val])
        if node_cat != None:
            while node_cat.next != None:
                cat.append([node_cat.order, node_cat.val])
                node_cat = node_cat.next
            cat.append([node_cat.order, node_cat.val])
        print(f"dog: {dog} cat: {cat}")

animal_shelter = AnimalShelter()
animal_shelter.enqueue(0)
animal_shelter.enqueue(0)
animal_shelter.enqueue(1)
animal_shelter.enqueue(0)
animal_shelter.enqueue(0)
animal_shelter.enqueue(1)
animal_shelter.enqueue(1)
animal_shelter.enqueue(0)
animal_shelter.enqueue(1)
animal_shelter.peekQueue()
animal_shelter.dequeueAny()
animal_shelter.dequeueCat()
animal_shelter.dequeueDog()
animal_shelter.dequeueCat()


animal_shelter.peekQueue()