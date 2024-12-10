class parrot:
    species="bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age

parrot1=parrot("Blue",5)
parrot2=parrot("Red",2)
parrot3=parrot("Yellow",4)
print("{} is a species {} and its age is {}".format(parrot1.name,parrot1.species,parrot1.age))
print("{} is a species {} and its age is {}".format(parrot2.name,parrot2.species,parrot2.age))
print("{} is a species {} and its age is {}".format(parrot3.name,parrot3.species,parrot3.age))