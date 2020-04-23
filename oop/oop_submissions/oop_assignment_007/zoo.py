class Deer:
    sound="Buck Buck"
    breath="Breathe in air"
    increase_in_food=2
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        self._age_in_months=age_in_months
        self._breed=breed
        self._required_food_in_kgs=required_food_in_kgs
        
        if self._required_food_in_kgs<=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        if age_in_months!=1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    @classmethod
    def breathe(cls):
        print(cls.breath)
    
    def grow(self):
        self._age_in_months+=1
        self._required_food_in_kgs+=self.increase_in_food

class Lion(Deer):
    sound="Roar Roar"
    increase_in_food=4
    
    def hunt(self,zoo):
        temp = zoo.animals
        
        #print(temp)
        deers_count = 0
        for animal in temp:
            #print("H",str(type(animal)))
            if "Deer" in str(type(animal)):
                 deers_count += 1
                 
        if deers_count == 0:
            print("No deers to hunt")
        else:
            count = 0
            for animal in temp:
                if "Deer" in str(type(animal)):
                    zoo.animals.remove(animal)
                    count += 1
                elif count == 1:
                    break  
     
    
class Shark(Deer):
    sound="Shark Sound"
    breath="Breathe oxygen from water"
    increase_in_food=8
    
    def hunt(self,zoo):
        temp = zoo.animals
        gold_fish_count = 0
        for animal in temp:
            if "GoldFish" in str(type(animal)):
                 gold_fish_count += 1
                 
        if gold_fish_count == 0:
            print("No GoldFish to hunt")
        else:
            count = 0
            for animal in temp:
                if "GoldFish" in str(type(animal)):
                    zoo.animals.remove(animal)
                    count += 1
                elif count == 1:
                    break

class Snake(Deer):
    sound="Hiss Hiss"
    increase_in_food=0.5
    
    def hunt(self,zoo):
        temp = zoo.animals
        deers_count = 0
        for animal in temp:
            if "Deer" in str(type(animal)):
                 deers_count += 1
                 
        if deers_count == 0:
            print("No deers to hunt")
        else:
            count = 0
            for animal in temp:
                if "Deer" in str(type(animal)):
                    zoo.animals.remove(animal)
                    count += 1
                elif count == 1:
                    break
    

class GoldFish(Deer):
    sound="Hum Hum"
    breath="Breathe oxygen from water"
    increase_in_food=0.2
        
class Zoo:
    number_of_animals_in_all_zoos=[]
    def __init__(self):
        self.animals=[]
        self._reserved_food_in_kgs=0
        
    def add_food_to_reserve(self,amount_of_food):
        self._reserved_food_in_kgs+=amount_of_food
    
    def count_animals(self):
        return len(self.animals)
        
    def add_animal(self,animal):
        self.animals.append(animal)
        self.number_of_animals_in_all_zoos.append(animal)
        
    @classmethod
    def count_animals_in_all_zoos(cls):
        return len(cls.number_of_animals_in_all_zoos)
        
     
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs

    @staticmethod    
    def count_animals_in_given_zoos(arg):
        total_animal_count = 0
        for zoo in arg:
            total_animal_count+=len(zoo.animals)
        return total_animal_count
        

    def feed(self,animal):
        if self._reserved_food_in_kgs!=0:
            self._reserved_food_in_kgs -= animal.required_food_in_kgs
            animal.grow()






zoo = Zoo()


gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
zoo.add_animal(gold_fish)
#print(zoo.count_animals())



nehru_zoological_park = Zoo()
#oo.add_food_to_reserve(10000000)
lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
nehru_zoological_park.add_animal(lion)
print(nehru_zoological_park.count_animals())

print("l",Zoo.count_animals_in_all_zoos())

print("b",Zoo.count_animals_in_given_zoos([zoo]))



#from zoo import Deer
# deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
# nehru_zoological_park.add_animal(deer)
# nehru_zoological_park.count_animals()
#2
# lion.hunt(nehru_zoological_park)
# nehru_zoological_park.count_animals()
#1
# lion.hunt(nehru_zoological_park) # Prints
#No deers to hunt
