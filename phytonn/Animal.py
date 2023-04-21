from asyncio.windows_events import NULL
from Organism import *
from abc import ABC, abstractmethod
import random

class Animal(Organism, ABC):

    @abstractmethod
    def name(self):
        pass 

    def action(self):
        self.add_age()
        self._last_position_x= self._position_x
        self._last_position_y= self._position_y
        x=self._position_x
        y=self._position_y
        while True:
            r= random.randint(0, 4)
            if r == 0: #North
                if self._position_x==0:
                    continue
                self._position_x-=1
                break
            elif r == 1: #East
                if self._position_y >= self.world.get_m()-1:
                    continue
                self._position_y+=1
                break
            elif r == 2: #South
                if self._position_x >= self.world.get_n()-1:
                    continue
                self._position_x+=1
                break
            else: #West
                if self._position_y == 0:
                    continue
                self._position_y-=1
                break		
        print(self.name() + " is moving from " + str(x) + "," + str(y) + " to x= " + str(self._position_x) + " y= " + str(self._position_y))
        kk=self.name() + " is moving from " + str(x) + "," + str(y) + " to x= " + str(self._position_x) + " y= " + str(self._position_y)
        self.world.get_messageinfo().append(kk)

    def collision(self):
        org = self.world.get_organism()
        for i in org:
            if i==NULL:
                continue
            if (i != self):
                if i.get_x() == self._position_x and i.get_y() == self._position_y:#collision of animal and org[i]

                    if i.name() =="Belladonna" or i.name()=="Sosnowskyshogweed":  #if org[i] is Belladonna or Sosnowsky
                        print(self.name() + " ate the poisonous plant")
                        k=self.name() + " ate the poisonous plant"
                        self.world.get_messageinfo().append(k)
                        self.world.delete_organism(self)
                        return
                    if i.name()=="Guarana": #collison with guarana
                        print("Guarana is eaten by " + self.name() + " Adding +3 strength.")
                        k1="Guarana is eaten by " + self.name() + " Adding +3 strength."
                        self.world.get_messageinfo().append(k1)
                        self.add_strength()
                        self.world.delete_organism(i)
                        return
                    if i.name()=="Turtle" and self.get_strength() < 5: # case of turtle, which reflectsthe attack and put animal on its previous position
                        print("Turtle reflects the attack of " + self.name())
                        k2="Turtle reflects the attack of " + self.name()
                        self.world.get_messageinfo().append(k2)
                        self.set_y(self.get_last_y())
                        self.set_x(self.get_last_x())
                        return
                    if i.get_strength() <= self.get_strength(): #animal stronger than org[]
                        if i.name()=="Human":
                            print("Collison. " + self.name() + " kills " + i.name())
                            k3="Collison. " + self.name() + " kills " + i.name()
                            self.world.get_messageinfo().append[k3]
                            print("Game over")
                            k4="Game over"
                            self.world.get_messageinfo().append(k4)
                            exit(1)
                        print("Collison. " + self.name() + " kills " + i.name())
                        k5="Collison. " + self.name() + " kills " + i.name()
                        self.world.get_messageinfo().append(k5)
                        self.world.delete_organism(i)
                        return
                    else: # animal weaker than org[]
                        print("Collison. " + i.name() + " kills " + self.name() + ".")
                        k6="Collison. " + i.name() + " kills " + self.name() + "."
                        self.world.get_messageinfo().append(k6)
                        self.world.delete_organism(self)
                        return
        