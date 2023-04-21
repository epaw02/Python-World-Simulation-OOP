from asyncio.windows_events import NULL
from Human import Human
from Organism import *
import random
from Wolf import *
from Sheep import *
from Antelope import *
from Fox import *
from Turtle import *
from Grass import *
from Guarana import *
from Belladonna import *
from Sowthistle import *
from Sosnowskyshogweed import *
from Cybersheep import *

class World:
	minimum_organisms=23

	def __init__(self, n, m, turn):
		self.__turn=int(turn)
		n=int(n)
		m=int(m)
		if n * m < self.minimum_organisms:
			print("The board is too small") #at least 2 instances of every organism at the beginning
			exit(1)
		else:
			self.__n= n
			self.__m= m
		
		self._o= [] #array of organisms
		self.board =[[' ' for i in range(m)] for j in range(n)]
		self._messageinfo=[] #list of commands

	def get_n(self):
		return self.__n

	def get_m(self):
		return self.__m

	def place_organism(self):
		v = 0
		t=[[0 for i in range(2)] for j in range(self.minimum_organisms)]
		while v < self.minimum_organisms: #we generate 23 different coordinates
			x = random.randint(0, self.__n-1)
			y  = random.randint(0, self.__m-1)
			i=0
			while i< v:
				if t[i][0]==x and t[i][1]==y:
					break
				i+=1

			if i==v:
				t[v][0] = x
				t[v][1] = y
				v+=1

		w1= Wolf(t[0][0], t[0][1],self) # putting the organisms on the boar
		w2= Wolf(t[1][0], t[1][1], self)

		s1= Sheep(t[2][0], t[2][1],self)
		s2= Sheep(t[3][0], t[3][1],self)

		a1=Antelope(t[4][0], t[4][1],self)
		a2=Antelope(t[5][0], t[5][1],self)

		f1=Fox(t[6][0], t[6][1],self)
		f2=Fox(t[7][0], t[7][1],self)

		t1=Turtle(t[8][0], t[8][1],self)
		t2=Turtle(t[9][0], t[9][1],self)

		gr1=Grass(t[10][0], t[10][1],self)
		gr2=Grass(t[11][0], t[11][1],self)

		gu1=Guarana(t[12][0], t[12][1],self)
		gu2=Guarana(t[13][0], t[13][1],self)

		b1=Belladonna(t[14][0], t[14][1],self)
		b2=Belladonna(t[15][0], t[15][1],self)

		sow1=Sowthistle(t[16][0], t[16][1],self)
		sow2=Sowthistle(t[17][0], t[17][1],self)

		ss1=Sosnowskyshogweed(t[18][0], t[18][1],self)
		ss2=Sosnowskyshogweed(t[19][0], t[19][1],self)

		c1=Cybersheep(t[20][0], t[20][1],self)
		c2=Cybersheep(t[21][0], t[21][1],self)

		self.human=Human(t[22][0], t[22][1], self)

		self._o.append(w1)
		self._o.append(w2)
		self._o.append(s1)
		self._o.append(s2)
		self._o.append(a1)
		self._o.append(a2)
		self._o.append(f1)
		self._o.append(f2)
		self._o.append(t1)
		self._o.append(t2)
		self._o.append(gr1)
		self._o.append(gr2)
		self._o.append(gu1)
		self._o.append(gu2)
		self._o.append(b1)
		self._o.append(b2)
		self._o.append(sow1)
		self._o.append(sow2)
		self._o.append(ss1)
		self._o.append(ss2)
		self._o.append(c1)
		self._o.append(c2)
		self._o.append(self.human)

	def make_turn(self):
		self.__turn+=1
		for obj in self._o:
			self._o.sort(key=lambda organism: organism.get_age(), reverse=True)
			self._o.sort(key=lambda organism: organism.get_initiative(), reverse=True)
			obj.action()
			obj.collision()

	def draw_world(self):
		self.board.clear()
		self.board =[[' ' for i in range(self.__m)] for j in range(self.__n)]
		v = 0
		for i in self._o: #placing organisms on the board
			x = i.get_x()
			y = i.get_y()
			self.board[x][y]=i.draw()
			v+=1
		print("Number of alive organisms: " + str(v))
		for row in self.board: #printing the board
			print(row)
		print("Human-X  Wolf-W  Sheep-S  Fox-F  Turtle-T  Antelope-A  Cybersheep-C")
		print("Grass - #  Sow thistle - &Guarana - @  Belladonna - % Sosnowsky's hogweed-$ ")


	def get_organism(self):
		return self._o
	
	def get_messageinfo(self):
		return self._messageinfo

	def get_board(self):
		return self.board
	
	def set_organism(self, array):
		self._o=array
	
	def set_turn(self, t):
		self.__turn=t

	def is_empty(self, x, y): #checking whether the position is empty
		for i in self._o: 
			if i!=NULL: #we only check completed position in o[]
				if i.get_x() == x and i.get_y() == y:
					return i  #not empty
		return NULL #empty

	def delete_organism(self, org):
		print("Deleting organism " + org.draw() + " x= " + str(org.get_x()) + " y= " + str(org.get_y())+'\n')
		self._o.remove(org)
	
	def save_game(self):
		file=open("wynik.txt", "w+")
		file.write("World size: " + str(self.__n) + " " + str(self.__m)+ '\n')
		file.write("Number of turns: " + str(self.__turn)+'\n')
		amount=0
		for i in self._o: 
			amount+=1
		file.write("Number of species: " + str(amount)+'\n')
		for i in self._o: 
			if i!=NULL:
				file.write(i.name() + " " + i.draw() + " " + str(i.get_x()) + " " + str(i.get_y())
						+ " " + str(i.get_initiative()) + " " + str(i.get_strength())+'\n')
		file.write("Human ability: "  + str(self.human.get_ability())+'\n')
		file.write("Cooldown: "  + str(self.human.get_noability())+'\n')
		file.close()
		print("Game saved")

	def get_human(self):
		return self.human
	
	def set_human(self, h):
		self.human = h
	




