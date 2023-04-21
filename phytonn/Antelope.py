from Animal import *

class Antelope(Animal):
    def __init__(self, x, y,w):
        self.world=w
        self._position_x=x 
        self._position_y=y
        self._strength= 4
        self._initiative= 4
        self._age=0 

    def action(self):
        self.add_age()
        self._last_position_x= self._position_x
        self._last_position_y= self._position_y
        x=self._position_x
        y=self._position_y
        #Has wider range of movement - 2 fields
        while True:
            r= random.randint(0, 4)
            if r == 0: #North
                if self._position_x<=1:
                    continue
                self._position_x-=2
                break
            elif r == 1: #East
                if self._position_y >= self.world.get_m()-2:
                    continue
                self._position_y+=2
                break
            elif r == 2: #South
                if self._position_x >= self.world.get_n()-2:
                    continue
                self._position_x+=2
                break
            else: #West
                if self._position_y <= 1:
                    continue
                self._position_y-=2
                break
        print("Antelope is moving from " + str(x) + "," + str(y) + " to x= " + str(self._position_x) + " y= " + str(self._position_y))
        kk="Antelope is moving from " + str(x) + "," + str(y) + " to x= " + str(self._position_x) + " y= " + str(self._position_y)
        self.world.get_messageinfo().append(kk)
    
    def collision(self):
        org = self.world.get_organism()
        g= random.randint(0, 1) # 0 fight, 1 escape]
        for i in org:
            if i==NULL:
                continue
            if (i != self):
                if i.get_x() == self._position_x and i.get_y() == self._position_y:#collision of antelope and org[i]
                    if g==1:    #if there is an empty space we put antelope there, if not it fights in a normal way													
                        if (self._position_x - 1) >= 0:
                            if self.world.is_empty(self._position_x - 1, self._position_y) == NULL:
                                self._position_x = self._position_x - 1
                                return
                        if (self._position_y + 1) < self.world.get_m():
                            if self.world.is_empty(self._position_x, self._position_y + 1) == NULL:
                                self._position_y = self._position_y + 1
                                return
                        if (self._position_x + 1) < self.world.get_n():
                            if self.world.is_empty(self._position_x + 1, self._position_y) == NULL:
                                self._position_x = self._position_x + 1
                                return
                        if (self._position_y - 1) >= 0:
                            if self.world.is_empty(self._position_x, self._position_y - 1) == NULL:
                                self._position_y = self._position_y - 1
                                return
                    else:  #fighting
                        if i.name()=="Antelope": #collision with antelope
                            self.set_y(self.get_last_y())
                            self.set_x(self.get_last_x())
                            if len(org) < (self.world.get_m() * self.world.get_n()):
                                x = self._position_x
                                y = self._position_y
                                if (self._position_x - 1) >= 0 and self.world.is_empty(self._position_x - 1, self._position_y) == NULL:
                                    x = self._position_x - 1
                                    print("Add a Antelope")
                                    k="Add a Antelope"
                                    self.world.get_messageinfo().append(k)
                                    org.append(Antelope(x, y, self.world))
                                    self.world.set_organism(org)
                                    return
                                elif (self._position_y + 1) < self.world.get_m() and self.world.is_empty(self._position_x, self._position_y + 1) == NULL:
                                    y = self._position_y + 1
                                    print("Add a Antelope")
                                    k="Add a Antelope"
                                    self.world.get_messageinfo().append(k)
                                    org.append(Antelope(x, y, self.world))
                                    self.world.set_organism(org)
                                    return
                                elif (self._position_x+ 1) < self.world.get_n() and self.world.is_empty(self._position_x+ 1, self._position_y) == NULL:
                                    x = self._position_x+ 1
                                    print("Add a Antelope")
                                    k="Add a Antelope"
                                    self.world.get_messageinfo().append(k)
                                    org.append(Antelope(x, y, self.world))
                                    self.world.set_organism(org)
                                    return
                                elif (self._position_y - 1) >= 0 and self.world.is_empty(self._position_x, self._position_y - 1) == NULL:
                                    y = self._position_y - 1
                                    print("Add a Antelope")
                                    k="Add a Antelope"
                                    self.world.get_messageinfo().append(k)
                                    org.append(Antelope(x, y, self.world))
                                    self.world.set_organism(org)
                                    return
                                else:
                                    return
                        if i.name()=="Belladonna" or i.name()=="Sosnowskyshogweed": #if org[i] is Belladonna or Sosnowsky																
                            print("Antelope ate the poisonous plant")
                            k1="Antelope ate the poisonous plant"
                            self.world.get_messageinfo().append(k1)
                            self.world.delete_organism(self)
                            return
                        if i.name()=="Guarana": #collison with guarana
                            print("Guarana is eaten by antelope. Adding +3 strength.")
                            k2="Guarana is eaten by antelope. Adding +3 strength."
                            self.world.get_messageinfo().append(k2)
                            self.add_strength()
                            self.world.delete_organism(i)
                            return
                        if i.name()=="Turtle" and self.get_strength() < 5: #case of turtle, which reflects the attack and put antelope on its previous position
                            print("Turtle reflects the attack of antelope")
                            k3="Turtle reflects the attack of antelope"
                            self.world.get_messageinfo().append(k3)
                            self.set_y(self.get_last_y())
                            self.set_x(self.get_last_x())
                            return
                        if i.get_strength() <= self.get_strength(): #antelope stronger than org[]
                            if (i.name()!=self.name()):
                                print("Collison. Antelope kills " + i.name())
                                k4="Collison. Antelope kills " + i.name()
                                self.world.get_messageinfo().append(k4)
                                self.world.delete_organism(i)
                                return
                        else: #antelope weaker than org[]
                            print("Collison. " + i.name() + "kills antelope.")
                            k5="Collison. Antelope kills " + i.name()
                            self.world.get_messageinfo().append(k5)
                            self.world.delete_organism(self)
                            return

    def draw(self):
        return 'A'

    def name(self):
        return "Antelope"
    
    def color(self):
        return (255, 213, 0) #yellow