from asyncio.windows_events import NULL
from Animal import *

class Fox(Animal):
    def __init__(self, x, y,w):
        self.world=w
        self._position_x=x 
        self._position_y=y
        self._strength= 3
        self._initiative= 7
        self._age=0       
    
    def action(self):
        self.add_age()
        self._last_position_x= self._position_x
        self._last_position_y= self._position_y
        #elf.age+=1
        x=self._position_x
        y=self._position_y
        while True:
            r= random.randint(0, 4)
            if r == 0: #North
                if self._position_x<=0:
                    continue
                org=self.world.is_empty(self._position_x - 1, self._position_y) #checking if the adjacent position is empty, if yes changing the position
                if org == NULL:
                    self._position_x-=1
                    break
                else:
                    if org.get_strength() > self.get_strength(): #checking if the opponent is stronger
                         break; 
            elif r == 1: #East
                if self._position_y >= self.world.get_m()-1:
                    continue
                org = self.world.is_empty(self._position_x, self._position_y + 1)
                if org == NULL:
                    self._position_y+=1
                    break
                else:
                    if org.get_strength() > self.get_strength():
                        break
            elif r == 2: #South
                if self._position_x >= self.world.get_n()-1:
                    continue
                org = self.world.is_empty(self._position_x + 1, self._position_y)
                if org == NULL:
                    self._position_x+=1
                    break
                else:
                    if org.get_strength() > self.get_strength():
                        break
            else: #West
                if self._position_y <= 0:
                    continue
                org = self.world.is_empty(self._position_x, self._position_y-1)
                if org==NULL:
                    self._position_y-=1
                    break
                else:
                    if org.get_strength() > self.get_strength():
                        break
        print("Fox is moving from " + str(x) + "," + str(y) + " to x= " + str(self._position_x) + " y= " + str(self._position_y))
        k="Fox is moving from " + str(x) + "," + str(y) + " to x= " + str(self._position_x) + " y= " + str(self._position_y)
        self.world.get_messageinfo().append(k)

    def collision(self):
        org = self.world.get_organism()
        for i in org:
            if i==NULL:
                continue
            if (i != self):
                if i.get_x() == self._position_x and i.get_y() == self._position_y:#collision of animal and org[i]
                    if i.name()=="Fox": #collision with fox
                        self.set_y(self.get_last_y())
                        self.set_x(self.get_last_x())
                        if len(org) < (self.world.get_m() * self.world.get_n()):
                            x = self._position_x
                            y = self._position_y
                            if (self._position_x - 1) >= 0 and self.world.is_empty(self._position_x - 1, self._position_y) == NULL:
                                x = self._position_x - 1
                                print("Add a new organism")
                                kk="Add a new Fox"
                                self.world.get_messageinfo().append(kk)
                                org.append(Fox(x, y, self.world))
                                self.world.set_organism(org)
                                return
                            elif (self._position_y + 1) < self.world.get_m() and self.world.is_empty(self._position_x, self._position_y + 1) == NULL:
                                y = self._position_y + 1
                                print("Add a new organism")
                                kk="Add a new Fox"
                                self.world.get_messageinfo().append(kk)
                                org.append(Fox(x, y, self.world))
                                self.world.set_organism(org)
                                return
                            elif (self._position_x+ 1) < self.world.get_n() and self.world.is_empty(self._position_x+ 1, self._position_y) == NULL:
                                x = self._position_x+ 1
                                print("Add a new organism")
                                kk="Add a new Fox"
                                self.world.get_messageinfo().append(kk)
                                org.append(Fox(x, y, self.world))
                                self.world.set_organism(org)
                                return
                            elif (self._position_y - 1) >= 0 and self.world.is_empty(self._position_x, self._position_y - 1) == NULL:
                                y = self._position_y - 1
                                print("Add a new organism")
                                kk="Add a new Fox"
                                self.world.get_messageinfo().append(kk)
                                org.append(Fox(x, y, self.world))
                                self.world.set_organism(org)
                                return
                            else:
                                return
                    if i.name() =="Belladonna" or i.name()=="Sosnowskyshogweed":  #if org[i] is Belladonna or Sosnowsky
                        print(self.name() + " ate the poisonous plant")
                        k1=self.name() + " ate the poisonous plant"
                        self.world.get_messageinfo().append(k1)
                        self.world.delete_organism(self)
                        return
                    if i.name()=="Guarana": #collison with guarana
                        print("Guarana is eaten by " + self.name() + " Adding +3 strength.")
                        k2="Guarana is eaten by " + self.name() + " Adding +3 strength."
                        self.world.get_messageinfo().append(k2)
                        self.add_strength()
                        self.world.delete_organism(i)
                        return
                    if i.name()=="Turtle" and self.get_strength() < 5: # case of turtle, which reflectsthe attack and put animal on its previous position
                        print("Turtle reflects the attack of " + self.name())
                        k3="Turtle reflects the attack of " + self.name()
                        self.world.get_messageinfo().append(k3)
                        self.set_y(self.get_last_y())
                        self.set_x(self.get_last_x())
                        return
                    if i.get_strength() <= self.get_strength(): #animal stronger than org[]
                        if i.name()=="Human":
                            print("Collison. " + self.name() + " kills " + i.name())
                            k4="Turtle reflects the attack of " + self.name()
                            self.world.get_messageinfo().append(k4)
                            print("Game over")
                            k5="Game over"
                            self.world.get_messageinfo().append(k5)
                            exit(1)
                        print("Collison. " + self.name() + " kills " + i.name())
                        k6="Collison. " + self.name() + " kills " + i.name()
                        self.world.get_messageinfo().append(k6)
                        self.world.delete_organism(i)
                        return
                    else: # animal weaker than org[]
                        print("Collison. " + i.name() + " kills " + self.name() + ".")
                        k7="Collison. " + i.name() + " kills " + self.name() + "."
                        self.world.get_messageinfo().append(k7)
                        self.world.delete_organism(self)
                    return
                    
    def draw(self):
        return 'F'

    def name(self):
        return "Fox"
    
    def color(self):
        return (255, 153, 51) #orange