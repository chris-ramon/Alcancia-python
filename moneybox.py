class Moneybox:
	"Abstracction of the moneybox objects."
	def __init__(self,money):
		'''Initialize the moneybox object and define the data.''' 
		self.money = money
	def getMoney(self):
		'''Return the current amount money.'''
		return str(self.money)+" dolars"
	def setMoney(self,money):
		'''Sets new amount money.'''
		self.money = money
	def playSong(self):
		'''Just a string simulating that the moneybox is playing a song.'''
		return 'Playing a random song!'
	def giveAllMoney(self):
		'''Just a string simulating that the moneybox is giving back all
		the current money.'''
		if self.money > 0 :
			m = self.money
			self.setMoney(0)
			return 'Giving all the money back: '+str(m)+" dolars"
		else:
			return 'No money left'
		
	'''Property function helps for return and set data of especific
	attribute'''
	money = property(getMoney,setMoney)

	


	
