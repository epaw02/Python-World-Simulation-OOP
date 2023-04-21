from abc import ABC, abstractmethod
from asyncio.windows_events import NULL
import random
from Organism import *


class Plant(Organism, ABC):
	
	@abstractmethod
	def name(self):
		pass

	def action(self):
		pass
	
	def collision(self):
		pass

