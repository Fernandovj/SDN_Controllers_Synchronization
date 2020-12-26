
import numpy as np 


class SillyAgent(): 
	def __init__(self,  num_state, num_actions, action_space): 
		""" 
		Contructor 
		Args: 
			
			num_state: The number of states 
			num_actions: The number of actions 
			action_space: To call the random action 
		"""
		
		self.num_state = num_state 
		self.num_actions = num_actions  
		self.action_space = action_space 

	def update(self, state, state2, reward, action, action2): 
		""" 
		Update the action value function using the Q-Learning update. 
		Q(S, A) = Q(S, A) + alpha(reward + (gamma * Q(S_, A_) - Q(S, A)) 
		Args: 
			prev_state: The previous state 
			next_state: The next state 
			reward: The reward for taking the respective action 
			prev_action: The previous action 
			next_action: The next action 
		Returns: 
			None 
		"""
		pass 

	def choose_action(self, state):		
		action = np.random.randint(0, self.num_actions-1) 
		return action