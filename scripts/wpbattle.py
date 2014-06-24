import random
import math


class  WPBattle(object):

	def __init__(self, attackers, defenders, def_bonus):
		self.attackers = attackers
		self.defenders = defenders
		self.total = attackers + defenders
		self.def_bonus = def_bonus

		self.atk_per = self.round_to(attackers / float(self.total) * 100)
		self.def_per = self.round_to(defenders / float(self.total) * 100)

	def score_combat(self):
		scores = {}
		def_roll_bonus = float(self.def_bonus)/2
		atk_rtypes = self.num_rolls(self.atk_per)
		def_rtypes = [round(droll+def_roll_bonus) for droll in self.num_rolls(self.def_per)]

		atk_rolls = [self.roll(roll) for roll in atk_rtypes]
		def_rolls = [self.roll(roll) for roll in def_rtypes]

		atk_score = sum(atk_rolls) 
		def_score = sum(def_rolls) + self.def_bonus


		if def_score >= atk_score:
			def_dead_ramount = (float(atk_score) / len(atk_rolls)) 
			atk_dead_ramount = (float(def_score) / len(def_rolls)) 

		else:
			def_dead_ramount = (atk_score / len(atk_rolls)) 
			atk_dead_ramount = (def_score / len(def_rolls)) 

		atk_dead_rolls = self.dead_percent(atk_dead_ramount)
		def_dead_rolls = self.dead_percent(def_dead_ramount)
		atk_dpercent = sum(atk_dead_rolls)
		def_dpercent = sum(def_dead_rolls)

		if def_score >= atk_score:
			atk_dpercent += (def_score - atk_score)
		else:
			def_dpercent += (atk_score - def_score)
	
		if self.defenders >= self.attackers:
			atk_dead = int(self.attackers * (atk_dpercent/100.0))
			def_dead = int(self.attackers * (def_dpercent/100.0))
		else:
			atk_dead = int(self.defenders * (atk_dpercent/100.0))
			def_dead = int(self.defenders * (def_dpercent/100.0))

		scores['def_dead_ramount'] = def_dead_ramount
		scores['atk_dead_ramount'] = atk_dead_ramount

		scores['atk_rtype'] = atk_rtypes
		scores['def_rtype'] = def_rtypes

		scores['def_dead_rolls'] = def_dead_rolls
		scores['atk_dead_rolls'] = atk_dead_rolls

		scores['atk_percent'] = self.atk_per
		scores['def_percent'] = self.def_per

		scores['atk_rolls'] = atk_rolls
		scores['def_rolls'] = def_rolls

		scores['atk_score'] = atk_score
		scores['def_score'] = def_score

		scores['atk_dead'] = atk_dead
		scores['def_dead'] = def_dead

		scores['atk_dpercent'] = atk_dpercent
		scores['def_dpercent'] = def_dpercent
		return scores


	def dead_percent(self, rolls):
		fiveD = 5
		dead_percent = [self.roll(fiveD) for r in xrange(0,int(rolls))]
		return dead_percent

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

		print "Attackers: %s | %s%%" % (self.attackers, scores['atk_percent'])
		print "DRolls: %s of %s" % (len(scores['atk_rtype']), scores['atk_rtype'])
		print "Rolls: %s = %s" % (str(scores['atk_rolls']), scores['atk_score'])
		print ""
		print "Defenders: %s | Defense Bonus: %s | %s%%" % (self.defenders, self.def_bonus, scores['def_percent'])
		print "DRolls: %s of %s" % (len(scores['def_rtype']),scores['def_rtype'])
		print "Rolls: %s + %s = %s" % (str(scores['def_rolls']), self.def_bonus , scores['def_score'])
		print ""
		print "Casualties: Lower Army count used. \nRolls = (score / rolls), ex, Atk dead rolls = (high_score/num_rolls). \nLoser uses higher score to determine dead. Score difference added to loser percentage"
		
		if scores['def_score'] >= scores['atk_score']:
			print "Atk %s D5 rolls: %s + %s = %s" % (int(scores['atk_dead_ramount']), scores['atk_dead_rolls'], 
													(scores['def_score'] - scores['atk_score']) , scores['atk_dpercent'])
			print "Def %s D5 rolls: %s = %s" % (int(scores['def_dead_ramount']), scores['def_dead_rolls'], scores['def_dpercent'])
		else:
			print "Atk %s D5 rolls: %s = %s" % (int(scores['atk_dead_ramount']), scores['atk_dead_rolls'], scores['atk_dpercent'])
			print "Atk %s D5 rolls: %s + %s = %s" % (int(scores['def_dead_ramount']), scores['def_dead_rolls'], 
													(scores['atk_score'] - scores['def_score']) , scores['def_dpercent'])


		if self.defenders >= self.attackers:
			print "Atk Casualties: %s * %s = %s " % (self.attackers, scores['atk_dpercent'], scores['atk_dead'])
			print "Def Casualties: %s * %s = %s " % (self.attackers, scores['def_dpercent'], scores['def_dead'])
		else:
			print "Atk Casualties: %s * %s = %s " % (self.defenders, scores['atk_dpercent'], scores['atk_dead'])
			print "Def Casualties: %s * %s = %s " % (self.defenders, scores['def_dpercent'], scores['def_dead'])

		print "Atk Remain: %s Def Remain: %s" % (self.attackers - scores['atk_dead'], self.defenders - scores['def_dead'])

try:
	attackers = int(input("Attackers: "))
	defenders = int(input("Defenders: "))
	bonus = int(input("Bonus: "))
	
	WPB = WPBattle(attackers, defenders, bonus)
	WPB.output_battle()
except:
	print "Are you sure you entered numbers?"
