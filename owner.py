import moneybox
class Owner:
	"Abstracction of the owner objects."
	def __init__(self,name) :
		'''Initialize a object owner and define the name of the owner.'''
		self.name = name
		self.moneybox = moneybox.Moneybox(0)
	def getName(self) :
		'''Return the name of the owner.'''
		return self.name
	def setName(self, name) :
		'''Set's a new name'''
		self.name = name
	name = property(getName,setName)
	def pressButton(self,color) :
		'''Simulate that if the owner press red color
		the moneybox give back all current money, if press button
		green the moneybox "says" the current money'''
		if color == 'red' :
			return self.moneybox.giveAllMoney()
		elif color == 'green' :
			return self.moneybox.getMoney()+' remain'
		else:
			return 'What are you doing?'
	def putMoney(self,money) :
		'''if moneybox recives money it does play a song'''
		if money > 0 :
			self.moneybox.money = self.moneybox.money + money
			return self.moneybox.playSong()
		else :
			return 'uhh?'
		
	
