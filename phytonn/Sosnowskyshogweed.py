from Plant import *

class Sosnowskyshogweed(Plant):
    def __init__(self, x, y,w):
        self.world=w
        self._position_x=x 
        self._position_y=y
        self._strength= 10
        self._initiative= 0
        self._age=0       
    
    def sowing(self):
        m= random.randint(0, 19)
        if m == 0: #20% chance it will sow
            org = self.world.get_organism()
            if len(org) < self.world.get_m() * self.world.get_n():
                x = self._position_x
                y = self._position_y
            if (self._position_x - 1) >= 0 and self.world.is_empty(self._position_x - 1, self._position_y) == NULL:
                x = self._position_x - 1
                print("Add a "+ self.name())
                k="Add a "+ self.name()
                self.world.get_messageinfo().append(k)
                org.append(Sosnowskyshogweed(x, y, self.world))
                self.world.set_organism(org)
            elif (self._position_y + 1) < self.world.get_m() and self.world.is_empty(self._position_x, self._position_y + 1) == NULL:
                y = self._position_y + 1
                print("Add a "+ self.name())
                k="Add a "+ self.name()
                self.world.get_messageinfo().append(k)
                org.append(Sosnowskyshogweed(x, y, self.world))
                self.world.set_organism(org)
            elif (self._position_x + 1) < self.world.get_n() and self.world.is_empty(self._position_x + 1, self._position_y) == NULL:
                x = self._position_x + 1
                print("Add a "+ self.name())
                k="Add a "+ self.name()
                self.world.get_messageinfo().append(k)
                org.append(Sosnowskyshogweed(x, y, self.world))
                self.world.set_organism(org)
            elif (self._position_y - 1) >= 0 and self.world.is_empty(self._position_x, self._position_y - 1) == NULL:
                y = self._position_y - 1
                print("Add a "+ self.name())
                k="Add a "+ self.name()
                self.world.get_messageinfo().append(k)
                org.append(Sosnowskyshogweed(x, y, self.world))
                self.world.set_organism(org)
            else:
                # print("No empty cells")
                return

    def action(self):
        self.add_age()
        self.sowing()
        if (self._position_x - 1) >= 0:  #checking if we are still on the board
            tmp = self.world.is_empty(self._position_x - 1, self._position_y)
            if tmp != NULL: 
                if tmp.name()=="Wolf" or tmp.name()=="Fox" or tmp.name()=="Sheep" or tmp.name()== "Antelope" or tmp.name()=="Turtle":
                    print("Sosnowsky's hogweed kills " + tmp.name())
                    k1="Sosnowsky's hogweed kills " + tmp.name()
                    self.world.get_messageinfo().append(k1)
                    self.world.delete_organism(tmp)
                elif tmp.name()=="Human": #if the animal is human
                    print("Sosnowsky's hogweed kills human.")
                    k2="Sosnowsky's hogweed kills human."
                    self.world.get_messageinfo().append(k2)
                    print("Game over")
                    k3="Game over"
                    self.world.get_messageinfo().append(k3)
                    exit(1)
                elif tmp.name()=="Cybersheep":
                    pass
        if (self._position_y + 1) < self.world.get_m():
            tmp = self.world.is_empty(self._position_x, self._position_y + 1)
            if tmp != NULL: 
                if tmp.name()=="Wolf" or tmp.name()=="Fox" or tmp.name()=="Sheep" or tmp.name()== "Antelope" or tmp.name()=="Turtle":
                    print("Sosnowsky's hogweed kills " + tmp.name())
                    k4="Sosnowsky's hogweed kills " + tmp.name()
                    self.world.get_messageinfo().append(k4)
                    self.world.delete_organism(tmp)
                elif tmp.name()=="Human": #if the animal is human
                    print("Sosnowsky's hogweed kills human.")
                    k5="Sosnowsky's hogweed kills human."
                    self.world.get_messageinfo().append(k5)
                    print("Game over")
                    k6="Game over"
                    self.world.get_messageinfo().append(k6)
                    exit(1)
                elif tmp.name()=="Cybersheep":
                    pass
        if (self._position_x + 1) < self.world.get_n():
            tmp = self.world.is_empty(self._position_x + 1, self._position_y)
            if tmp != NULL: 
                if tmp.name()=="Wolf" or tmp.name()=="Fox" or tmp.name()=="Sheep" or tmp.name()== "Antelope" or tmp.name()=="Turtle":
                    print("Sosnowsky's hogweed kills " + tmp.name())
                    k7="Sosnowsky's hogweed kills " + tmp.name()
                    self.world.get_messageinfo().append(k7)
                    self.world.delete_organism(tmp)
                elif tmp.name()=="Human": #if the animal is human
                    print("Sosnowsky's hogweed kills human.")
                    k8="Sosnowsky's hogweed kills human."
                    self.world.get_messageinfo().append(k8)
                    print("Game over")
                    k9="Game over"
                    self.world.get_messageinfo().append(k9)
                    exit(1)
                elif tmp.name()=="Cybersheep":
                    pass
        if (self._position_y - 1) >= 0:
            tmp = self.world.is_empty(self._position_x, self._position_y - 1)
            if tmp != NULL: 
                if tmp.name()=="Wolf" or tmp.name()=="Fox" or tmp.name()=="Sheep" or tmp.name()== "Antelope" or tmp.name()=="Turtle":
                    print("Sosnowsky's hogweed kills " + tmp.name())
                    k10="Sosnowsky's hogweed kills " + tmp.name()
                    self.world.get_messageinfo().append(k10)
                    self.world.delete_organism(tmp)
                elif tmp.name()=="Human": #if the animal is human
                    print("Sosnowsky's hogweed kills human.")
                    k11="Sosnowsky's hogweed kills human."
                    self.world.get_messageinfo().append(k11)
                    print("Game over")
                    k12="Game over"
                    self.world.get_messageinfo().append(k12)
                    exit(1)
                elif tmp.name()=="Cybersheep":
                    pass
				
    def draw(self):
        return '$'

    def name(self):
        return "Sosnowskyshogweed"
    
    def color(self):
        return (0, 76, 153) #dark blue