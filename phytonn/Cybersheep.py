from Animal import *
import math

class Cybersheep(Animal):
    def __init__(self, x, y,w):
        self.world=w
        self._position_x=x 
        self._position_y=y
        self._strength= 11
        self._initiative= 4
        self._age = 0

    def action(self):
        self.add_age()
        sosnowsky=[] #list of sosnowsky's hogweeds
        org = self.world.get_organism()
        for obj in org:
            if obj.name()=="Sosnowskyshogweed":
                point=(obj.get_x(), obj.get_y())
                sosnowsky.append((obj,point))
        if len(sosnowsky)==0:
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
            return
        else:
            self._last_position_x= self._position_x
            self._last_position_y= self._position_y
            distance=[]
            for s in sosnowsky:
                x=s[0].get_x()
                y=s[0].get_y()
                d=math.hypot(self._position_x-x,self._position_y-y) #calculating the distance
                distance.append((d,s)) #list of all the distances
            distance.sort(key=lambda y: y[0])
            for obj in distance:
                num=distance.index(obj)
                g= [x1[1] for x1 in distance]
                plant= [xx[0] for xx in g]
                h=[x2[1] for x2 in g]
                j=[x3[0] for x3 in h]
                k=[x4[1]for x4 in h]
                sh=plant[num]
                posx=j[num]
                posy=k[num]
                if self._position_x > posx: 
                    if self.world.is_empty(self._position_x-1,self._position_y)==NULL or self.world.is_empty(self._position_x-1,self._position_y)==sh: #avoiding collison
                        self._position_x-=1
                        print(self.name() + " is moving from " + str(self._last_position_x) + "," + str(self._last_position_y) + " to x= " + str(self._position_x) + " y= " + str(self._position_y))
                        k=self.name() + " is moving from " + str(self._last_position_x) + "," + str(self._last_position_y) + " to x= " + str(self._position_x) + " y= " + str(self._position_y)
                        self.world.get_messageinfo().append(k)
                        return 
                if self._position_x < posx:
                    if self.world.is_empty(self._position_x+1,self._position_y)==NULL or self.world.is_empty(self._position_x+1,self._position_y)==sh:
                        self._position_x+=1
                        print(self.name() + " is moving from " + str(self._last_position_x) + "," + str(self._last_position_y) + " to x= " + str(self._position_x) + " y= " + str(self._position_y))
                        k=self.name() + " is moving from " + str(self._last_position_x) + "," + str(self._last_position_y) + " to x= " + str(self._position_x) + " y= " + str(self._position_y)
                        self.world.get_messageinfo().append(k)
                        return
                if self._position_y > posy:
                    if self.world.is_empty(self._position_x,self._position_y-1)==NULL or self.world.is_empty(self._position_x,self._position_y-1)==sh:
                        self._position_y-=1
                        print(self.name() + " is moving from " + str(self._last_position_x) + "," + str(self._last_position_y) + " to x= " + str(self._position_x) + " y= " + str(self._position_y))
                        k=self.name() + " is moving from " + str(self._last_position_x) + "," + str(self._last_position_y) + " to x= " + str(self._position_x) + " y= " + str(self._position_y)
                        self.world.get_messageinfo().append(k)
                        return
                if self._position_y < posy:
                    if self.world.is_empty(self._position_x,self._position_y+1)==NULL or self.world.is_empty(self._position_x,self._position_y+1)==sh:
                        #self._position_y-=1
                        self._position_y+=1
                        print(self.name() + " is moving from " + str(self._last_position_x) + "," + str(self._last_position_y) + " to x= " + str(self._position_x) + " y= " + str(self._position_y))
                        k=self.name() + " is moving from " + str(self._last_position_x) + "," + str(self._last_position_y) + " to x= " + str(self._position_x) + " y= " + str(self._position_y)
                        self.world.get_messageinfo().append(k)
                        return
                else:
                    if obj==distance[-1]:
                        return
                    else:
                     continue
                        
    def collision(self):
        org = self.world.get_organism()
        for i in org:
            if i==NULL:
                continue
            if (i != self):
                if i.get_x() == self._position_x and i.get_y() == self._position_y:#collision of animal and org[i]
                    if i.name()=="Cybersheep": #collision with cybersheep
                        self.set_y(self.get_last_y())
                        self.set_x(self.get_last_x())
                        if len(org) < (self.world.get_m() * self.world.get_n()):
                            x = self._position_x
                            y = self._position_y
                            if (self._position_x - 1) >= 0 and self.world.is_empty(self._position_x - 1, self._position_y) == NULL:
                                x = self._position_x - 1
                                print("Add a new organism")
                                k="Add a Cybersheep"
                                self.world.get_messageinfo().append(k)
                                org.append(Cybersheep(x, y, self.world))
                                self.world.set_organism(org)
                                return
                            elif (self._position_y + 1) < self.world.get_m() and self.world.is_empty(self._position_x, self._position_y + 1) == NULL:
                                y = self._position_y + 1
                                print("Add a new organism")
                                k="Add a Cybersheep"
                                self.world.get_messageinfo().append(k)
                                org.append(Cybersheep(x, y, self.world))
                                self.world.set_organism(org)
                                return
                            elif (self._position_x+ 1) < self.world.get_n() and self.world.is_empty(self._position_x+ 1, self._position_y) == NULL:
                                x = self._position_x+ 1
                                print("Add a new organism")
                                k="Add a Cybersheep"
                                self.world.get_messageinfo().append(k)
                                org.append(Cybersheep(x, y, self.world))
                                self.world.set_organism(org)
                                return
                            elif (self._position_y - 1) >= 0 and self.world.is_empty(self._position_x, self._position_y - 1) == NULL:
                                y = self._position_y - 1
                                print("Add a new organism")
                                k="Add a Cybersheep"
                                self.world.get_messageinfo().append(k)
                                org.append(Cybersheep(x, y, self.world))
                                self.world.set_organism(org)
                                return
                            else:
                                return
                    if i.name()=="Sosnowskyshogweed":
                        print(self.name() + " eats Sosnowsky's hogweed")
                        k1=self.name() + " eats Sosnowsky's hogweed"
                        self.world.get_messageinfo().append(k1)
                        self.world.delete_organism(i)
                        return
                    if i.name() =="Belladonna":  #if org[i] is Belladonna
                        print(self.name() + " ate the poisonous plant")
                        k2=self.name() + " ate the poisonous plant"
                        self.world.get_messageinfo().append(k2)
                        self.world.delete_organism(self)
                        return
                    if i.name()=="Guarana": #collison with guarana
                        print("Guarana is eaten by " + self.name() + " Adding +3 strength.")
                        k3="Guarana is eaten by " + self.name() + " Adding +3 strength."
                        self.world.get_messageinfo().append(k3)
                        self.add_strength()
                        self.world.delete_organism(i)
                        return
                    if i.get_strength() <= self.get_strength(): #animal stronger than org[]
                        if i.name()=="Human":
                            print("Collison. " + self.name() + " kills " + i.name())
                            k4="Collison. " + self.name() + " kills " + i.name()
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
        return 'C'

    def name(self):
        return "Cybersheep"
    
    def color(self):
        return (70, 20, 120) #purple

