
from Investment_instrument import Invest
import matplotlib.pyplot as plt
import numpy as np
from Input_dataset import *



def main():
	positions = prompt_positions()
	ntrials = prompt_ntrials()
	Investment_instrument = Invest(1000)
	results = ['Position Mean Std']
	

	for position in positions:
		print 'Stimulating with position {}'.format(position)
		daily_ret = Investment_instrument.simulation(ntrials,position)
		results.append(''.join(map(str,[position,np.mean(daily_ret),np.std(daily_ret)])))

		p = plt.figure()
		plt.hist(daily_ret,100,range=[-1,1])
		plt.title('Histogram of Daily Return with Positions')
		plt.xlabel('Daily Return')
		p.savefig('Histogram_{}_pos.pdf'.format(str(position).zfill(4)))

	print 'Saving results'
	with open('results.txt',"w") as f:
		f.write('\n'.join(results))


if __name__ == '__main__':
	main()
