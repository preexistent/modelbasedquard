import numpy as np 
import argparse

import pdb
from scipy.spatial.distance import cdist
from scipy.optimize import linear_sum_assignment
import time

def distcheck(a,b,R):
	l = len(a)
	thresh = 2*(2**0.5)*R
	distance = cdist(a,b,'euclidean')
	dist_list = list(distance[np.triu_indices(l,2)])

	
	if any(i < thresh for i in dist_list):
		raise Exception('Minimum separation violated')	
	#distance.append(dist)
	return np.asarray(distance)

def main(args):
	goals = args.goals
	robots = args.robots
	goal_locs = np.random.randn(goals,2)*10
	start_locs = np.random.randn(robots,2)*10
	traj,unassigned_goals = captbasic(start_locs,goal_locs,0.01)


def captbasic(start,goal,R):
	
	startdistmat = distcheck(start,start,R)
	goaldistmat = distcheck(goal,goal,R)
	dist = distcheck(start,goal,R)
	start = time.time()

	matrix = linear_sum_assignment(dist)
	end = time.time()
	print(end - start)

	pdb.set_trace()
	#add check for distance between start locations
	
	#add check for distance between goal locations

	#compute a distance matrix between all start and goal locations

	#do hungarian optimality assignment
	#



if __name__=='__main__':

	parser = argparse.ArgumentParser(description='CAPT')

	parser.add_argument('--goals',type=int,default=1000,help='number of goals')
	parser.add_argument('--robots',type=int,default=1000,help='number of robots')

	args = parser.parse_args()

	main(args)