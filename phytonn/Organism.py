from abc import ABC, abstractmethod

class Organism(ABC):
    def __init__(self, w, strength, initiative, position_x, position_y,last_position_x,last_position_y, age)->None:
        self.world=w
        self._strength = strength
        self._initiative = initiative
        self._position_x = position_x
        self._position_y = position_y
        self._last_position_x = last_position_x
        self._last_position_y = last_position_y
        self._age = int(0)
        
    
    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def name(self):
        pass

    def set_x(self, pos_x): 
        self._position_x=pos_x

    def set_y(self, pos_y): 
        self._position_y=pos_y
	
    def get_x(self): #returns the x coordinate of the organism
        return self._position_x

    def get_y(self): #returns the y coordinate of the organism
        return self._position_y

    def get_last_x(self): #returns the previous x coordinate
        return self._last_position_x

    def get_last_y(self): #returns the previous y coordinate
        return self._last_position_y

    def get_strength(self):
        return self._strength

    def get_initiative(self):
        return self._initiative

    def get_age(self):
        return self._age

    def set_strength(self, s):
        self._strength=s

    def set_age(self, a):
        self._age=a
    
    def add_age(self):
        self._age=int(self._age)
        self._age+=1

    def add_strength(self): #adding strength (guarana collison)
        self._strength=self._strength+3

