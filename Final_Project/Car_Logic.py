import random

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

	def crash(self, road, car, obstacle, road_move):
		move = self.table[road][car][obstacle]
		if car + road_move + move  == obstacle and obstacle != -1:
			# print("crash1 " + str(road) + " " + str(car) + " " + str(obstacle) + " " + str(move) + " " + str(road_move))
			return True
		if car + road_move + move < 0:
			# print("crash2 " + str(road) + " " + str(car) + " " + str(obstacle) + " " + str(move) + " " + str(road_move))
			return True
		if car + road_move + move > 9:
			# print("crash3 " + str(road) + " " + str(car) + " " + str(obstacle) + " " + str(move) + " " + str(road_move))
			return True
		# print(str(road) + " " + str(car) + " " + str(obstacle) + " " + str(move) + " " + str(road_move))
		return False