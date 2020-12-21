# Agent.py 

import numpy as np 

class Agent: 
	""" 
	The Base class that is implemented by 
	other classes to avoid the duplicape 'choose_action' 
	method 
	"""
	def choose_action(self, state): 
		action = 0
		if np.random.uniform(0, 1) < self.epsilon: 
			#action = self.action_space.sample() 
			action = np.random.randint(0, self.num_actions)
    
		else: 
			#action = np.argmax(self.Q[state, :])
			action = np.argmin(self.Q[state, :]) 
		return action 
