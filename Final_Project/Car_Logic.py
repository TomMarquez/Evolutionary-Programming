class Car_Logic:


	# table[road][car][obstacle] = -1 , 0, 1
	def __init__(self, road, car, obstacle):
		self.road = road
		self.car = car
		self.obstacle = obstacle
		
	def init_table(self):
		self.table = [[[(random.randint(0, 2) -1) for x in range(self.obstacle)] for y in range(self.car)] for z in range(self.road)]


	def print_table(self):
		self.table[3][0][0] = 5
		print (self.table)

	def set_table(self, table):
		self.table = table

	def get_table(self):
		return self.table

	def get_move(self, road, car, obstacle):
		return self.table[road][car][obstacle]

	def crash(self, road, car, obstacle):
		move = self.table[road][car][obstacle]
		if car == obstacle and move == 0:
			return True
		if car == 0 and move == -1:
			return True
		if car == 9 and move == 1:
			return True
		if car == -1 and move != 1:
			return True
		if car == 10 and move != -1:
			return True
		if car - obstacle == -1 and move == 1:
			return True
		if car - obstacle == 1 and move == -1:
			return True
		return False