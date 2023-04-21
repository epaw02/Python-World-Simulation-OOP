from Animal import *

class Turtle(Animal):
    def __init__(self, x, y,w):
        self.world=w
        self._position_x=x 
        self._position_y=y
        self._strength= 2
        self._initiative= 1
        self._age=0     
    
    def action(self):
        self.add_age()
        self.last_position_x = self._position_x #rememebering the previous position
        self.last_position_y = self._position_y
        x = self._position_x
        y = self._position_y
        m= random.randint(0, 4)
        if m == 0: #25% chance it will move
            while True:
                r= random.randint(0, 4)
                if r==0: #North
                    if self._position_x==0: #checking if we are at the end of the world
                        continue
                    self._position_x-=1
                    break
                elif r==1: #East
                    if self._position_y>=self.world.get_m()-1:
                        continue
                    self._position_y+=1
                    break
                elif r==2: #South
                    if self._position_x>=self.world.get_n()-1:
                        continue
                    self._position_x+=1
                    break
                else: #West
                    if self._position_y == 0:
                        continue
                    self._position_y-=1
                    break
        print("Turtle is moving from " + str(x) + "," + str(y) + " to x= " + str(self._position_x) + " y= " + str(self._position_y))
        kk="Turtle is moving from " + str(x) + "," + str(y) + " to x= " + str(self._position_x) + " y= " + str(self._position_y)
        self.world.get_messageinfo().append(kk)

    def collision(self):
        org = self.world.get_organism()
        for i in org:
            if i==NULL:
                continue
            if (i != self):
                if i.get_x() == self._position_x and i.get_y() == self._position_y:#collision of animal and org[i]
                    if i.name()=="Turtle": #collision with trutle
                        self.set_y(self.get_last_y())
                        self.set_x(self.get_last_x())
                        if len(org) < (self.world.get_m() * self.world.get_n()):
                            x = self._position_x
                            y = self._position_y
                            if (self._position_x - 1) >= 0 and self.world.is_empty(self._position_x - 1, self._position_y) == NULL:
                                x = self._position_x - 1
                                print("Add a "+ self.name())
                                k="Add a "+ self.name()
                                self.world.get_messageinfo().append(k)
                                org.append(Turtle(x, y, self.world))
                                self.world.set_organism(org)
                                return
                            elif (self._position_y + 1) < self.world.get_m() and self.world.is_empty(self._position_x, self._position_y + 1) == NULL:
                                y = self._position_y + 1
                                print("Add a "+ self.name())
                                k="Add a "+ self.name()
                                self.world.get_messageinfo().append(k)
                                org.append(Turtle(x, y, self.world))
                                self.world.set_organism(org)
                                return
                            elif (self._position_x+ 1) < self.world.get_n() and self.world.is_empty(self._position_x+ 1, self._position_y) == NULL:
                                x = self._position_x+ 1
                                print("Add a "+ self.name())
                                k="Add a "+ self.name()
                                self.world.get_messageinfo().append(k)
                                org.append(Turtle(x, y, self.world))
                                self.world.set_organism(org)
                                return
                            elif (self._position_y - 1) >= 0 and self.world.is_empty(self._position_x, self._position_y - 1) == NULL:
                                y = self._position_y - 1
                                print("Add a "+ self.name())
                                "Turtle is moving from " + str(x) + "," + str(y) + " to x= " + str(self._position_x) + " y= " + str(self._position_y)
                                org.append(Turtle(x, y, self.world))
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
                    if i.get_strength() <= self.get_strength(): #animal stronger than org[]
                        if i.name()=="Human":
                            print("Collison. " + self.name() + " kills " + i.name())
                            k3="Collison. " + self.name() + " kills " + i.name()
                            self.world.get_messageinfo().append(k3)
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

    def draw(self):
        return 'T'

    def name(self):
        return "Turtle"
    
    def color(self):
        return (0, 102, 0) #dark green