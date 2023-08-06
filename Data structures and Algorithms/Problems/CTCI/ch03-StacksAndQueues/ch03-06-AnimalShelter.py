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
        self.head_dog = None

    def reset_head(self):
        pass

    def enqueue(self, a_type:int):
        a_type = 0 if a_type != 0 else 1
        animal = AnimalNode(a_type, self.animal_count)
        self.animal_count += 1
        


    def dequeueAny(self):
        pass

    def dequeueDog(self):
        pass

    def dequeueCat(self):
        pass
