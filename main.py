# main.py 


import gym 
import numpy as np 
import sdnc_sync_env 
#from ExpectedSarsaAgent import ExpectedSarsaAgent 
#from QLearningAgent import QLearningAgent 
#from SarsaAgent import SarsaAgent 
from matplotlib import pyplot as plt 

# Using the gym library to create the environment 
#env = gym.make('CliffWalking-v0') 
env = sdnc_sync_env

# Defining all the required parameters 
epsilon = 0.1
total_episodes = 1
max_steps = 100
alpha = 0.5
gamma = 1
""" 
	The two parameters below is used to calculate 
	the reward by each algorithm 
"""
episodeReward = 0
totalReward = { 
	'SarsaAgent': [], 
	'QLearningAgent': [], 
	'ExpectedSarsaAgent': [] 
} 

# Defining all the three agents 
#expectedSarsaAgent = ExpectedSarsaAgent( 
#	epsilon, alpha, gamma, env.observation_space.n, 
#	env.action_space.n, env.action_space) 
#qLearningAgent = QLearningAgent( 
#	epsilon, alpha, gamma, env.observation_space.n, 
#	env.action_space.n, env.action_space) 
#sarsaAgent = SarsaAgent( 
#	epsilon, alpha, gamma, env.observation_space.n, 
#	env.action_space.n, env.action_space) 

# Now we run all the episodes and calculate the reward obtained by 
# each agent at the end of the episode 



for _ in range(total_episodes): 
	# Initialize the necesary parameters before 
	# the start of the episode 
	t = 0
	state1 = env.reset() 
	print("first_state:",state1)
	#action1 = agent.choose_action(state1)
	action1 = [1,0,0,0] 
	episodeReward = 0
	while t < max_steps: 

	# 	# Getting the next state, reward, and other parameters 

		state2, reward, done, info = env.step(action1)
		print("t:",t,"next_state:",state2,"reward:",reward)
	# 	# Choosing the next action 
	# 	action2 = agent.choose_action(state2) 
		action2 = [0,1,0,0]
		
	# 	# Learning the Q-value 
	 	#agent.update(state1, state2, reward, action1, action2)
		state1 = state2
		action1 = action2 
		
	# 	# Updating the respective vaLues 
		t += 1
	# 	episodeReward += reward 
		
	# 	# If at the end of learning process 
		if done:
			break



	# Append the sum of reward at the end of the episode 
	#totalReward[type(agent).__name__].append(episodeReward) 
#env.close() 


# Calculate the mean of sum of returns for each episode 
#meanReturn = { 
#	'SARSA-Agent': np.mean(totalReward['SarsaAgent']), 
#	'Q-Learning-Agent': np.mean(totalReward['QLearningAgent']), 
#	'Expected-SARSA-Agent': np.mean(totalReward['ExpectedSarsaAgent']) 
#} 

# Print the results 
#print(f"SARSA Average Sum of Reward: {meanReturn['SARSA-Agent']}") 
#print(f"Q-Learning Average Sum of Return: {meanReturn['Q-Learning-Agent']}") 
#print(f"Expected Sarsa Average Sum of Return: {meanReturn['Expected-SARSA-Agent']}") 
