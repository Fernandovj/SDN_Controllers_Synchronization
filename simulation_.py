#Metric: Average Path Cost (APC) - the average of the constructed paths 
#(the cost of a path is the sum of the weights of its links)

#Goal: find paths with minimum cost, this is, reduce APC 


import random
import topology 

def 

class Network(object):
	def __init__(self, topology):
		self.topology = topology


class Controller(object):
	def __init__(self, domain, network):
		self.domain = domain
		self.network = network


net_A = Network(topology.get_topo("multidomain_topo"))
net_B = Network(topology.get_topo("multidomain_topo"))
net_C = Network(topology.get_topo("multidomain_topo"))
net_D = Network(topology.get_topo("multidomain_topo"))
net_E = Network(topology.get_topo("multidomain_topo"))
ctlr_A = Controller("A",net_A)
ctlr_B = Controller("A",net_B)
ctlr_C = Controller("A",net_C)
ctlr_D = Controller("A",net_D)
ctlr_E = Controller("A",net_E)


print(ctlr_A.domain)
print(net_B.topology.graph) 


for link_index in range(33):
	new_weight = random.randint(0,100)
	print(link_index,new_weight)









