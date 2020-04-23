from car import Car
class Truck(Car):
    sound="Honk Honk"
    def __init__(self,max_speed,acceleration,tyre_friction,max_cargo_weight,color="none"):
        super().__init__(max_speed,acceleration,tyre_friction,color)
        self._max_cargo_weight=max_cargo_weight
        self._total_load=0
        self._present_load=0
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
    @property
    def total_load(self):
        return self._total_load
    @property
    def present_load(self):
        return self._present_load

    
    def load(self,n):
        if n>=0:
            self._present_load += n
            if self._current_speed>0:
                print("Cannot load cargo during motion")
            elif self._present_load>self._max_cargo_weight:
                print("Cannot load cargo more than max limit:",self._max_cargo_weight)
            else:
                self._total_load = self._present_load
        else:
            raise ValueError("Invalid value for cargo_weight")
    
    def unload(self,n):
        if n>=0:
            if self._current_speed>0:
                print("Cannot unload cargo during motion")
            else:
                if n>=self._total_load:
                    self._present_load=0
                else:
                    self._total_load -= n                        
        else:
            raise ValueError("Invalid value for cargo_weight")    
            
            