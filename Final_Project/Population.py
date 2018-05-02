from Car_Logic import Car_Logic
import random

class Population:

	def __init__(self, pop_size, plain, road_size):
		self.pop_size = pop_size
		self.plain = plain
		self.road_size = road_size
		self.crashed = []
		self.pop = []
		self.fit = []
		self.car = []

	def init_pop(self):
		for i in range(self.pop_size): 
			self.pop.append(Car_Logic(self.plain, self.road_size, self.road_size))
			self.pop[i].init_table()
			self.crashed.append(False)
			self.fit.append([i, 1])
			self.car.append(i)

	def get_car(self, index):
		return self.pop[index]
	# might not need

	def make_move(self, road, obstacle, road_move):
		for i in range(self.pop_size):
			if not self.crashed[i]:
				car_move = self.pop[i].get_move(road, self.car[i], obstacle)
				if self.pop[i].crash(road, self.car[i], obstacle, road_move):
					self.crashed[i] = True
					# print("crashed: " + str(i))

				else:
					self.fit[i][1] += 1
					self.car[i] += road_move + car_move

	def get_move(self,index, road, car, obstacle):
		self.pop[index].get_move(road, car, obstacle)

	def done(self):
		for i in range(self.pop_size):
			if not self.crashed[i]:
				return False
		return True

	
	# list elements in order of fitness
	def rank_fitness(self):
		def take_second(elem):
			return elem[1]
		self.fit.sort(reverse=True, key=take_second)


	def mating_pool(self, new_pop_size, mode):
		roulette_wheel = []
		wheel_size = 0
		result = []
		if mode == 1:
			for i in range(self.pop_size):
				for j in range(self.pop_size - i):
					roulette_wheel.append(self.fit[i][0])
					wheel_size += 1
		elif mode == 2:
			for i in range(self.pop_size):
				wheel_size += self.fit[i][1]
			for i in range(self.pop_size):
				for j in range(self.fit[i][1]):
					roulette_wheel.append(self.fit[i][0])

		for i in range(new_pop_size):
			index = random.randint(0, wheel_size-1)
			result.append(roulette_wheel[index])
		return result

	def cross_over(self, mate_match):
		cp1 = random.randint(0, self.plain-1)
		cp2 = random.randint(0, self.road_size-1)
		cp3 = random.randint(0, self.road_size-1)
		table_one = self.pop[mate_match[0]].get_table()
		table_two = self.pop[mate_match[1]].get_table()
		temp = 0
		for i in range(cp1):
			for j in range(cp2):
				for k in range(cp3):
					temp = table_one[i][j][k]
					table_one[i][j][k] = table_two[i][j][k]
					table_two[i][j][k] = temp
		return table_one, table_two

	def mutation(self, tables, new_pop_size):
		for i in range(new_pop_size):
			if random.randint(0, new_pop_size-1) == 0:
				for j in range(self.plain):
					if random.randint(0, self.plain-1) == 0:
						for k in range(self.road_size):
							if random.randint(0, self.road_size-1) == 0:
								for l in range(self.road_size):
									if random.randint(0, self.road_size-1) == 0:
										tables[i][j][k][l] = random.randint(0, 2) - 1
		return tables

	def set_new_pop(self, tables, new_pop_size):
		self.pop = []
		self.crashed = []
		self.fit = []
		self.car = []
		for i in range(new_pop_size):
			self.pop.append(Car_Logic(self.plain, self.road_size, self.road_size))
			self.pop[i].set_table(tables[i])
			self.crashed.append(False)
			self.fit.append([i, 1])
			self.car.append(i)

	def breed(self, new_pop_size, chance_of_breed, mode):
		pool = self.mating_pool(new_pop_size, mode)
		mate_match = []
		result = []
		for i in range(0, len(pool)):
			if random.randint(0, 100) >= 100 - chance_of_breed:
				mate_match.append(pool[i])
			else:
				result.append(self.pop[pool[i]].get_table())
			if len(mate_match) == 2:
				x, y = self.cross_over(mate_match)
				result.append(x)
				result.append(y)
				mate_match = []
		if len(mate_match) == 1:
			result.append(self.pop[mate_match[0]].get_table())
		result = self.mutation(result, new_pop_size)
		self.set_new_pop(result, new_pop_size)
		return result

	def car_position(self, index):
		return self.car[index] + self.road



	def print_fit(self):
		print(self.fit)