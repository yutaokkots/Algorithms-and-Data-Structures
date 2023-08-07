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

    def reset_head(self, new_node):
        pass

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
        pass

    def dequeueDog(self):
        pass

    def dequeueCat(self):
        pass

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