from Animal import *

class Human(Animal):
    def __init__(self, x, y, w):
        self.world=w
        self._ability = 0
        self._noability = 0 #cooldown
        self._alive = 1 #1-alive, 0-dead
        self._position_x=x 
        self._position_y=y
        self._strength= 5
        self._initiative= 4
        self._age=0

    def action(self):
        pass

    def collision(self):
        self.add_age()
        org = self.world.get_organism()
        for i in org:
            if i==NULL:
                continue
            if i != self:
                if i.get_x() == self._position_x and i.get_y() == self._position_y: #collison ofself and org[]
                    if i.name()=="Belladonna" or i.name()=="Sosnowskyshogweed":  #if org[i] is Belladonna or Sosnowsky
                        print("Human ate the poisonous plant")
                        k1="Human ate the poisonous plant"
                        self.world.get_messageinfo().append(k1)
                        print("Game over")
                        k2="Game over"
                        self.world.get_messageinfo().append(k2)
                        exit(1)
                    if i.name()=="Guarana": #collison with guarana
                        print("Guarana is eaten byself. Adding +3 strength.")
                        k3="Guarana is eaten byself. Adding +3 strength."
                        self.world.get_messageinfo().append(k3)
                        self.add_strength()
                        self.world.delete_organism(i)
                        return
                    if i.get_strength() <= self.get_strength():   #human stronger than org[]
                        print("Collison.self kills " + i.name())
                        k4="Collison.self kills " + i.name()
                        self.world.get_messageinfo().append(k4)
                        self.world.delete_organism(i)
                        return
                    else: #human weaker than org[]
                        print("Collison. " + i.name() + " killsself.")
                        k5="Collison. " + i.name() + " killsself."
                        self.world.get_messageinfo().append(k5)
                        print("Game over")
                        k6="Game over"
                        self.world.get_messageinfo().append(k6)
                        exit(1)
        if self._ability != 0:  #destroys all animals and plants that are adjacent toself's position
            print("Special ability on")
            k="Special ability on"
            self.world.get_messageinfo().append(k)
            if (self._position_x - 1) >= 0:
                tmp = self.world.is_empty(self._position_x - 1, self._position_y)
                if tmp !=  NULL:
                    self.world.delete_organism(tmp)
            if (self._position_y + 1) < self.world.get_m():
                tmp = self.world.is_empty(self._position_x, self._position_y + 1)
                if tmp != NULL:
                    self.world.delete_organism(tmp)
            if (self._position_x + 1) < self.world.get_n():
                tmp = self.world.is_empty(self._position_x + 1, self._position_y)
                if tmp != NULL:
                    self.world.delete_organism(tmp)
            if (self._position_y - 1) >= 0:
                tmp = self.world.is_empty(self._position_x, self._position_y - 1)
                if tmp != NULL:
                    self.world.delete_organism(tmp)

    def draw(self):
        return 'X'

    def name(self):
        return "Human"

    def decreasespecialability(self):
        if self._ability!=0:
            self._ability-=1
            if self._ability==0:
                self._noability=5 
        if self._noability!=0:
            self._noability=-1

    def get_alive(self):
        return self._alive 
    
    def set_alive(self,i):
        self._alive=i
	
    def get_ability(self):
        return self._ability
    
    def set_ability(self, a):
        self._ability=a
	
    def get_noability(self):
        return self._noability

    def set_noability(self, n):
        self._noability=n
    
    def color(self):
        return (255, 51, 51) #red

    def set_x(self, pos_x): 
        self._position_x=pos_x

    def set_y(self, pos_y): 
        self._position_y=pos_y
	
    def get_x(self): #returns the x coordinate of the organism
        return self._position_x

    def get_y(self): #returns the y coordinate of the organism
        return self._position_y
	
