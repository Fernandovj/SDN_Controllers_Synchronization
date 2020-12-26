# import gym
import itertools
from collections import defaultdict
import numpy as np
from Agent import Agent 

class SarsaLambdaAgent(Agent):

    def __init__(self, trace_decay, gamma, nA):      
        self.trace_decay = trace_decay
        self.gamma = gamma
        self.num_actions = nA
        self.Q = defaultdict(lambda: np.zeros(nA))
        self.E = defaultdict(lambda: np.zeros(nA))
    
    def update(self, state, next_state, reward, action, next_action, Nas):
        type='accumulate'
        delta = reward + self.gamma*self.Q[next_state][next_action] - self.Q[state][action]

        self.E[state][action] += 1
        alpha = 1.0/ Nas[state][action]
        for s, _ in self.Q.items():
            self.Q[s][:] += alpha * delta * self.E[s][:]
            if type == 'accumulate':
                self.E[s][:] *= self.trace_decay * self.gamma
            elif type == 'replace':
                if s == state:
                    self.E[s][:] = 1
                else:
                    self.E[s][:] *= self.gamma * self.trace_decay