import random
import math


class  WPBattle(object):

	def __init__(self, attackers, defenders, def_bonus):
		self.attackers = attackers
		self.defenders = defenders
		self.total = attackers + defenders
		self.def_bonus = def_bonus/2

		self.atk_per = self.round_to(attackers / float(self.total) * 100)
		self.def_per = self.round_to(defenders / float(self.total) * 100)

	def score_combat(self):
		scores = {}
		loss_dbonus_rolls = 2
		atk_rtypes = self.num_rolls(self.atk_per)
		def_rtypes = [droll+self.def_bonus for droll in self.num_rolls(self.def_per)]

		atk_rolls = [self.roll(roll) for roll in atk_rtypes]
		def_rolls = [self.roll(roll) for roll in def_rtypes]

		atk_score = sum(atk_rolls) 
		def_score = sum(def_rolls)

		if def_score >= atk_score:
			def_dead_rolls = (atk_score / len(atk_rolls)) 
			atk_dead_rolls = def_score / len(def_rolls) + loss_dbonus_rolls
		else:
			def_dead_rolls = atk_score / len(atk_rolls) + loss_dbonus_rolls
			atk_dead_rolls = (def_score / len(def_rolls)) 

		atk_dpercent = self.dead_percent(atk_dead_rolls)
		def_dpercent = self.dead_percent(def_dead_rolls)
	
		atk_dead = int(self.attackers * (atk_dpercent/100.0))
		def_dead = int(self.defenders * (def_dpercent/100.0))

		scores['atk_score'] = atk_score
		scores['def_score'] = def_score

		scores['atk_dead'] = atk_dead
		scores['def_dead'] = def_dead

		scores['atk_dpercent'] = atk_dpercent
		scores['def_dpercent'] = def_dpercent

		scores['atk_dead'] = atk_dead
		scores['def_dead'] = def_dead
		return scores


	def dead_percent(self, rolls):
		fiveD = 5
		dead_percent = [self.roll(fiveD) for r in xrange(0,rolls)]
		return sum(dead_percent)

	def num_rolls(self, tpercent):
		type_rolls = []
		tp = tpercent
		sixD = 6
		thrD = 3
		while tp > 0:
			if tp >= 10:
				type_rolls.append(sixD)
				tp -= 10
			else:
				type_rolls.append(thrD)
				tp -= 5
		return type_rolls

	def roll(self, dnum):
		return random.randint(1, dnum)

	def round_to(self, num, base=5):
		return int(base * round(float(num)/base))

	def output_battle(self):
		scores = self.score_combat()
		print scores
		print "Attackers: %s Defenders: %s Defense Bonus: %s" % (self.attackers, self.defenders, self.def_bonus)
		print "Atk Score: %s Def Score: %s" % (scores['atk_score'], scores['def_score'])
		print "Atk Casualties: %s Def Casualties: %s" % (scores['atk_dead'], scores['def_dead'])

WPB = WPBattle(100000, 50000, 3)
WPB.output_battle()
