import owner ### we import the owner module in order to create the object
### Now we simulate the givin case ###
owner = owner.Owner('Tomas')
print owner.name+' has a moneybox'
print owner.name+' adds 2342 dolars'
print '		moneybox: '+str(owner.putMoney(2342))
print owner.name+' adds 22 dolars'
print '		moneybox: '+str(owner.putMoney(22))
print owner.name+' press red button:'
print '		moneybox: '+str(owner.pressButton('red'))
print owner.name+' press green button:'
print '		moneybox: '+str(owner.pressButton('green'))
print owner.name+' press red button:'
print '		moneybox: '+str(owner.pressButton('red'))
