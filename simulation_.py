#Metric: Average Path Cost (APC) - the average of the constructed paths 
#(the cost of a path is the sum of the weights of its links)

#Goal: find paths with minimum cost, this is, reduce APC 


import random
import topologies as tp

def update_weights(controllers,new_weights): 
#This function receives a list of controllers and a list of new weights
#to update the link weights in their corresponding domains 

	for c in controllers:
		links_list = c.network.topology.graph["links"]
		for i in range(len(links_list)):
			if links_list[i]["domain"] == c.domain:
				links_list[i]["weight"] = new_weights[i]

def sync(controller_X,controller_Y): 
#This function receives two controllers (X and Y) to update X's network view with Y's domain network view
	
	links_X = controller_X.network.topology.graph["links"]
	links_Y = controller_Y.network.topology.graph["links"]
	
	for i in range(len(links_Y)):
		if links_Y[i]["domain"] == controller_Y.domain:
			links_X[i]["weight"] = links_Y[i]["weight"] 	 


class Network(object):
	def __init__(self, topology):
		self.topology = topology


class Controller(object):
	def __init__(self, domain):
		self.domain = domain
		self.network = Network(tp.get_topo("multidomain_topo"))


ctlr_A = Controller("A")
ctlr_B = Controller("B")
ctlr_C = Controller("C")
ctlr_D = Controller("D")
ctlr_E = Controller("E")


new_weights = []
for link_index in range(33):
	new_weight = random.randint(0,100)
	#print(link_index,new_weight)
	new_weights.append(new_weight)
	
#if ctlr_A.network.topology.graph == ctlr_B.network.topology.graph:
#	print("yes")
#else:
#	print("no")

update_weights([ctlr_A,ctlr_B,ctlr_C,ctlr_D,ctlr_E],new_weights)
print(ctlr_A.network.topology.graph["links"])
print(ctlr_B.network.topology.graph["links"])

sync(ctlr_A,ctlr_B)
print()
print(ctlr_A.network.topology.graph["links"])
print(ctlr_B.network.topology.graph["links"])




