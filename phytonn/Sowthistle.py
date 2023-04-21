from Plant import *

class Sowthistle(Plant):
    def __init__(self, x, y,w):
        self.world=w
        self._position_x=x 
        self._position_y=y
        self._strength= 0
        self._initiative= 0
        self._age=0

    def action(self):
        self.add_age()
        org = self.world.get_organism()
        for i in range (0,3):
            m= random.randint(0, 19)
            if m == 0: #5% chance it will sow
                if len(org) < self.world.get_m() * self.world.get_n():
                    x = self._position_x
                    y = self._position_y
                    if (self._position_x - 1) >= 0 and self.world.is_empty(self._position_x - 1, self._position_y) == NULL:
                        x = self._position_x - 1
                        print("Add a "+ self.name())
                        k="Add a "+ self.name()
                        self.world.get_messageinfo().append(k)
                        org.append(Sowthistle(x, y, self.world))
                        self.world.set_organism(org)
                    elif (self._position_y + 1) < self.world.get_m() and self.world.is_empty(self._position_x, self._position_y + 1) == NULL:
                        y = self._position_y + 1
                        print("Add a "+ self.name())
                        k="Add a "+ self.name()
                        self.world.get_messageinfo().append(k)
                        org.append(Sowthistle(x, y, self.world))
                        self.world.set_organism(org)
                    elif (self._position_x + 1) < self.world.get_n() and self.world.is_empty(self._position_x + 1, self._position_y) == NULL:
                        x = self._position_x + 1
                        print("Add a "+ self.name())
                        k="Add a "+ self.name()
                        self.world.get_messageinfo().append(k)
                        org.append(Sowthistle(x, y, self.world))
                        self.world.set_organism(org)
                    elif (self._position_y - 1) >= 0 and self.world.is_empty(self._position_x, self._position_y - 1) == NULL:
                        y = self._position_y - 1
                        print("Add a "+ self.name())
                        k="Add a "+ self.name()
                        self.world.get_messageinfo().append(k)
                        org.append(Sowthistle(x, y, self.world))
                        self.world.set_organism(org)
                    else:
                        # print("No empty cells")
                        return
					   
    def draw(self):
        return '&'

    def name(self):
        return "Sowthistle"
    
    def color(self):
        return (102, 178, 255) #light blue