from threading import Thread, Lock, Event
import time, random

mutex = Lock()

#Interval in seconds
processIntervalMin = 5
processIntervalMax = 15
processingDurationMin = 3
processingDurationMax = 15

class BarberShop:
	waitingCustomers = []

	def __init__(self, barber, numberOfSeats):
		self.barber = barber
		self.numberOfSeats = numberOfSeats
		print ('Memory initilized with {0} free spaces'.format(numberOfSeats))
		print ('Process min interval {0}'.format(processIntervalMin))
		print ('Process max interval {0}'.format(processIntervalMax))
		print ('Processing min duration {0}'.format(processingDurationMin))
		print ('Processing max duration {0}'.format(processIntervalMax))
		print ('---------------------------------------')

	def openShop(self):
		print ('System is Loading...')
		workingThread = Thread(target = self.barberGoToWork)
		workingThread.start()

	def barberGoToWork(self):
		while True:
			mutex.acquire()

			if len(self.waitingCustomers) > 0:
				c = self.waitingCustomers[0]
				del self.waitingCustomers[0]
				mutex.release()
				self.barber.cutHair(c)
			else:
				mutex.release()
				print ('All done. Memory Freed')
				barber.sleep()
				print ('Allocator Starts')
	
	def enterBarberShop(self, customer):
		mutex.acquire()
		print ('>> {0} entered the Memory and is looking for a free space'.format(customer.name))

		if len(self.waitingCustomers) == self.numberOfSeats:
			print ('Memory waiting room is full, {0} is leaving.'.format(customer.name))
			mutex.release()
		else:
			print ('{0} waits in the waiting room'.format(customer.name))
			self.waitingCustomers.append(c)	
			mutex.release()
			barber.wakeUp()

class Customer:
	def __init__(self, name):
		self.name = name

class Barber:
	barberWorkingEvent = Event()

	def sleep(self):
		self.barberWorkingEvent.wait()

	def wakeUp(self):
		self.barberWorkingEvent.set()

	def cutHair(self, customer):
		#Set barber as busy 
		self.barberWorkingEvent.clear()

		print ('{0} is being processed'.format(customer.name))

		randomHairCuttingTime = random.randrange(processingDurationMin, processingDurationMax+1)
		time.sleep(randomHairCuttingTime)
		print ('{0} is done'.format(customer.name))


if __name__ == '__main__':
	customers = []
	customers.append(Customer('P1'))
	customers.append(Customer('P2'))
	customers.append(Customer('P3'))
	customers.append(Customer('P4'))
	customers.append(Customer('P5'))
	customers.append(Customer('P6'))
	customers.append(Customer('P7'))
	customers.append(Customer('P8'))


	barber = Barber()

	barberShop = BarberShop(barber, numberOfSeats=3)
	barberShop.openShop()

	while len(customers) > 0:
		c = customers.pop()	
		#New customer enters the barbershop
		barberShop.enterBarberShop(c)
		customerInterval = random.randrange(processIntervalMin,processIntervalMax+1)
		time.sleep(customerInterval)

		

