import json
import copy

multidomain_topo = {
"graph": {

    "nodes": [
        {"id": 0, "name": "a1", "domain": "A"}, 
        {"id": 1, "name": "a2", "domain": "A"}, 
        {"id": 2, "name": "a3", "domain": "A"}, 
        {"id": 3, "name": "a4", "domain": "A"}, 
        {"id": 4, "name": "b1", "domain": "B"}, 
        {"id": 5, "name": "b2", "domain": "B"}, 
        {"id": 6, "name": "b3", "domain": "B"}, 
        {"id": 7, "name": "b4", "domain": "B"}, 
        {"id": 8, "name": "c1", "domain": "C"}, 
        {"id": 9, "name": "c2", "domain": "C"}, 
        {"id": 10, "name": "c3", "domain": "C"}, 
        {"id": 11, "name": "c4", "domain": "C"}, 
        {"id": 12, "name": "c5", "domain": "C"}, 
        {"id": 13, "name": "d1", "domain": "D"}, 
        {"id": 14, "name": "d2", "domain": "D"},
        {"id": 15, "name": "d3", "domain": "D"},
        {"id": 16, "name": "d4", "domain": "D"},
        {"id": 17, "name": "d5", "domain": "D"},
        {"id": 18, "name": "e1", "domain": "E"},
        {"id": 19, "name": "e2", "domain": "E"},
        {"id": 20, "name": "e3", "domain": "E"},
        {"id": 21, "name": "e4", "domain": "E"},
        {"id": 22, "name": "e5", "domain": "E"}],
    #   
    "links": [
        {"weight": 0, "source": 0, "target": 1, "domain":"A"}, 
        {"weight": 0, "source": 0, "target": 2, "domain":"A"}, 
        {"weight": 0, "source": 1, "target": 2, "domain":"A"},
        {"weight": 0, "source": 1, "target": 4, "domain":"AB"},
        {"weight": 0, "source": 2, "target": 3, "domain":"A"}, 
        {"weight": 0, "source": 3, "target": 4, "domain":"AB"}, 
        {"weight": 0, "source": 3, "target": 6, "domain":"AB"}, 
        {"weight": 0, "source": 4, "target": 5, "domain":"B"}, 
        {"weight": 0, "source": 4, "target": 6, "domain":"B"}, 
        {"weight": 0, "source": 4, "target": 7, "domain":"B"}, 
        {"weight": 0, "source": 5, "target": 8, "domain":"BC"}, 
        {"weight": 0, "source": 5, "target": 10, "domain":"BC"}, 
        {"weight": 0, "source": 6, "target": 7, "domain":"B"}, 
        {"weight": 0, "source": 7, "target": 12, "domain":"BC"}, 
        {"weight": 0, "source": 8, "target": 9, "domain":"C"}, 
        {"weight": 0, "source": 8, "target": 10, "domain":"C"}, 
        {"weight": 0, "source": 9, "target": 11, "domain":"C"}, 
        {"weight": 0, "source": 9, "target": 14, "domain":"CD"}, 
        {"weight": 0, "source": 10, "target": 11, "domain":"C"}, 
        {"weight": 0, "source": 11, "target": 12, "domain":"C"}, 
        {"weight": 0, "source": 11, "target": 17, "domain":"CD"}, 
        {"weight": 0, "source": 13, "target": 14, "domain":"D"}, 
        {"weight": 0, "source": 13, "target": 15, "domain":"D"}, 
        {"weight": 0, "source": 14, "target": 15, "domain":"D"}, 
        {"weight": 0, "source": 14, "target": 16, "domain":"D"}, 
        {"weight": 0, "source": 15, "target": 18, "domain":"DE"}, 
        {"weight": 0, "source": 16, "target": 17, "domain":"D"}, 
        {"weight": 0, "source": 16, "target": 20, "domain":"DE"}, 
        {"weight": 0, "source": 18, "target": 19, "domain":"E"},
        {"weight": 0, "source": 18, "target": 21, "domain":"E"},
        {"weight": 0, "source": 19, "target": 22, "domain":"E"},
        {"weight": 0, "source": 20, "target": 22, "domain":"E"},
        {"weight": 0, "source": 21, "target": 22, "domain":"E"}]
        }
}

def get_topo(name):
    topo = Topology()
    if name == "multidomain_topo":
        topo.set_graph(copy.deepcopy(multidomain_topo["graph"]))
    else:
        return "topology not found"
        
    return topo 

class Topology:
    def __init__(self):
        # self.id=ids
        self.graph = {}

    def set_graph(self,graph):
        self.graph = graph


