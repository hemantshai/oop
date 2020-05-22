class Animal:
    sound = 'None'
    required_food = 0
    def __init__(self, age_in_months, breed, required_food_in_kgs):
        if age_in_months != 1:
            raise ValueError(f'Invalid value for field age_in_months: {age_in_months}')
        elif required_food_in_kgs <= 0:
            raise ValueError(f'Invalid value for field required_food_in_kgs: {required_food_in_kgs}')
            
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
    
    @classmethod
    def make_sound(cls):
        print(cls.sound)

    def grow(self):
        self._age_in_months +=1
        self._required_food_in_kgs += self.required_food
        
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
        
class water_animals:
    breathing = "Breathe oxygen from water"
    @classmethod
    def breathe(cls):
        print(cls.breathing)


class land_animals:
    breathing="Breathe in air"        
    @classmethod
    def breathe(cls):
        print(cls.breathing)

class Hunter:
    hunt_type="Buck Buck"
    hunt_value="No deers to hunt"
    
    @classmethod
    def hunt(cls, zoo):
        count=0
        for animal in zoo.animals_list:
            if animal.sound == cls.hunt_type:
                count=1
                zoo.animals_list.remove(animal)
                zoo.number_of_animals_in_all_zoos.remove(animal)
                break
        if count==0:
            print(cls.hunt_value)
     
class Deer(Animal,land_animals):
    sound = 'Buck Buck'
    required_food = 2
        
class Lion(Animal, land_animals, Hunter):
    sound = 'Roar Roar'
    required_food = 4
    
        
class GoldFish(Animal,water_animals):    
    sound = 'Hum Hum'
    required_food = 0.2
      
class Shark(Animal,water_animals, Hunter):
    sound = 'Shark Sound'
    required_food = 8
    hunt_type="Hum Hum"
    hunt_value="No GoldFish to hunt"  
        
class Snake(Animal,land_animals, Hunter):
    
    sound = 'Hiss Hiss'
    required_food = 0.5
        
class Zoo:
    number_of_animals_in_all_zoos =[]
    def __init__(self):
        self._reserved_food_in_kgs = 0
        self.animals_list = []
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
    def add_food_to_reserve(self, food_quantity):
        self._reserved_food_in_kgs += food_quantity
    
    def add_animal(self, animal):
        self.animals_list.append(animal)
        self.number_of_animals_in_all_zoos.append(animal)
        
        
    def count_animals(self):
        return len(self.animals_list)
        
    def feed(self, animal_name):
        if self._reserved_food_in_kgs!=0:
            self._reserved_food_in_kgs -= animal_name.required_food_in_kgs
            animal_name.grow()
          
    @classmethod
    def count_animals_in_all_zoos(cls):
        return len(cls.number_of_animals_in_all_zoos)
        
    @staticmethod    
    def count_animals_in_given_zoos(arg):
        total_animal_count = 0
        for zoo in arg:
            total_animal_count+=len(zoo.animals_list)
        return total_animal_count






