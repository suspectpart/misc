import random

class Triell(object):
	def __init__(self, players):
		self.players = players

	def start(self):		
		while len(self.players) > 1:
			for player in self.players:
				if not player.alive:
					continue
				player.shoot(filter(lambda p: p.alive and p != player, self.players))

			self.players = filter(lambda p: p.alive, self.players)
		
		return self.players[0].name

class Player(object):
	def __init__(self, name, kill_probability):
		self.name = name
		self.alive = True
		self.kill_probability = kill_probability

	def shoot(self, opponents):
		bullet = random.randint(1, self.kill_probability)
		target = min(opponents, key=lambda x: x.kill_probability)
		target.take(bullet)

		print self.name, "shoots at", target.name, "and", "misses" if target.alive else "kills", "him."

	def take(self, bullet):
		self.alive = bullet != 1


class Mister_Black(Player):
	def __init__(self):
		Player.__init__(self, "Mister Black", 3)

class Mister_Black_Smart(Mister_Black):

	def shoot(self, opponents):
		bullet = random.randint(1, self.kill_probability)
		if len(opponents) > 1:
			print "Mister Black shoots a bird"
			return

		else:
			target = min(opponents, key=lambda x: x.kill_probability)
			target.take(bullet)

			print self.name, "shoots at", target.name, "and", "misses" if target.alive else "kills", "him."

class Mister_Gray(Player):
	def __init__(self):
		Player.__init__(self, "Mister Gray", 2)

class Mister_White(Player):
	def __init__(self):
		Player.__init__(self, "Mister White", 1)



def stats():
	winners = []
	for i in range(0,1000):
		players = [Mister_Black_Smart(), Mister_Gray(), Mister_White()]
		triell = Triell(players)
		winner = triell.start()
		winners.append(winner)

	print "Mister Black won", (float(winners.count("Mister Black")) / 1000) * 100, "% of all triells."
	print "Mister Gray won", (float(winners.count("Mister Gray")) / 1000) * 100, "% of all triells."
	print "Mister White won", (float(winners.count("Mister White")) / 1000) * 100, "% of all triells."

stats()