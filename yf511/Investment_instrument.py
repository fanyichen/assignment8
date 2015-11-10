#@author Yichen @ Nov 10th, 2015
'''This program is going to determine how to make prediction by simulating real life  investment
Computer will randomly determine Gain or Loss with certain probability
If wins, you will Gain in double of number of position value or Loss with nothing
You will have 1000 in total, position equals 1000/domination you chose
The average gain or loss will be find by repeating n times of trial'''
import numpy as np

class Invest(object):# run the simulation of investment by class
	def __init__(self,asset):
		self.asset = asset


	def simulation(self,ntrials,position):# simulate the investment according to the number of shares

		position_value = self.asset / position #size of each investment with given position
		cumu_ret=[]
		for trail in xrange(ntrials):
			margin = np.random.choice(2,position,p=[0.49,0.51]) # p[0]=0.49 and p[1]=0.51
			cumu_ret.append(margin.sum()*position_value*2) #gain with double or loss with nothing
		daily_ret = [float(ret)/float(1000)-1 for ret in cumu_ret]#calculate daily_ret by cumu_ret
		return daily_ret
	


