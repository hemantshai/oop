from car import Car
class RaceCar(Car):
    sound="Peep Peep\nBeep Beep"
    def __init__(self,max_speed,acceleration,tyre_friction,color="None"):
        super().__init__(max_speed,acceleration,tyre_friction,color="none")
        self._nitro=0
    @property    
    def nitro(self):
        return self._nitro
    def accelerate(self):
        
            
        
    