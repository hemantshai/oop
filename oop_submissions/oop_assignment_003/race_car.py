from car import Car
import math
class RaceCar(Car):
    sound="Peep Peep\nBeep Beep"
    def __init__(self,max_speed,acceleration,tyre_friction,color="None"):
        super().__init__(max_speed,acceleration,tyre_friction,color)
        self._nitro=0
    @property    
    def nitro(self):
        return self._nitro
    def accelerate(self):
        if self._nitro>0:
            self._current_speed+=math.ceil(self._acceleration*0.3)
            self._nitro-=10
        super().accelerate()
    def apply_brakes(self):
        if self._current_speed >=self._max_speed//2:
            self._nitro+=10
        super().apply_brakes()
        
    