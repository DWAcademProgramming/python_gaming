class Dog():
    """A class to represent a dog"""
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def bark(self, is_loud): 
        """Get the dog to speak"""
        if is_loud: 
            print("Quiet!!!!")
        else: 
            print("Good dog")
    
    def age(self):
        """Compute the dog's age in dog years"""
        dog_years = self.age * 7
        print(self.name + " is " + str(dog_years) + " years in dog years")