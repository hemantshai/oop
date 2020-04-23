class Car:
    sound="Beep Beep"
    def __init__(self,max_speed,acceleration,tyre_friction,color="none"):
        self._color=color
        self._max_speed=max_speed
        self._acceleration=acceleration
        self._tyre_friction=tyre_friction
        self._is_engine_started=False
        self._current_speed=0
        if self._max_speed<0:
            raise ValueError("Invalid value for max_speed")
        if self._acceleration<0:
            raise ValueError("Invalid value for acceleration")
        if self._tyre_friction<0:
            raise ValueError("Invalid value for tyre_friction")
            
    @property
    def is_engine_started(self):
        return self._is_engine_started
    @property
    def max_speed(self):
        return self._max_speed
    @property
    def color(self):
        return self._color
    @property
    def tyre_friction(self):
        return self._tyre_friction
    @property
    def current_speed(self):
        return self._current_speed
        
    @property
    def acceleration(self):
        return self._acceleration 

    def start_engine(self):
        self._is_engine_started=True

    def stop_engine(self):
        self._is_engine_started=False    

    def accelerate(self):
        if self._is_engine_started:
            #self._current_speed+=self._acceleration
            if self._current_speed+self._acceleration<self._max_speed:
                self._current_speed+=self._acceleration
            else:
                self._current_speed=self._max_speed
        else:
            print("Start the engine to accelerate")
        
    def apply_brakes(self):
        if self._current_speed<=self._tyre_friction:
            self._current_speed=0
        else:
            self._current_speed-=self._tyre_friction
        
    def sound_horn(self):
        if self._is_engine_started==False:
            print("Start the engine to sound_horn")
        else:
            
            print(self.sound)
                