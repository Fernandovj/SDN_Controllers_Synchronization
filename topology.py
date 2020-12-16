import json

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
    #link type: 0: intra-domain, 1: inter-domain    
    "links": [
        {"weight": 0, "source": 0, "target": 1, "type":0}, 
        {"weight": 0, "source": 0, "target": 2, "type":0}, 
        {"weight": 0, "source": 1, "target": 4, "type":1},
        {"weight": 0, "source": 2, "target": 3, "type":0}, 
        {"weight": 0, "source": 3, "target": 4, "type":0}, 
        {"weight": 0, "source": 3, "target": 6, "type":0}, 
        {"weight": 0, "source": 4, "target": 5, "type":0}, 
        {"weight": 0, "source": 4, "target": 6, "type":0}, 
        {"weight": 0, "source": 4, "target": 7, "type":0}, 
        {"weight": 0, "source": 5, "target": 8, "type":0}, 
        {"weight": 0, "source": 5, "target": 10, "type":0}, 
        {"weight": 0, "source": 6, "target": 7, "type":0}, 
        {"weight": 0, "source": 7, "target": 12, "type":0}, 
        {"weight": 0, "source": 8, "target": 9, "type":0}, 
        {"weight": 0, "source": 8, "target": 10, "type":0}, 
        {"weight": 0, "source": 9, "target": 11, "type":0}, 
        {"weight": 0, "source": 9, "target": 14, "type":0}, 
        {"weight": 0, "source": 10, "target": 11, "type":0}, 
        {"weight": 0, "source": 11, "target": 12, "type":0}, 
        {"weight": 0, "source": 11, "target": 17, "type":0}, 
        {"weight": 0, "source": 13, "target": 14, "type":0}, 
        {"weight": 0, "source": 13, "target": 15, "type":0}, 
        {"weight": 0, "source": 14, "target": 15, "type":0}, 
        {"weight": 0, "source": 14, "target": 16, "type":0}, 
        {"weight": 0, "source": 15, "target": 18, "type":0}, 
        {"weight": 0, "source": 16, "target": 17, "type":0}, 
        {"weight": 0, "source": 16, "target": 20, "type":0}, 
        {"weight": 0, "source": 18, "target": 19, "type":0},
        {"weight": 0, "source": 18, "target": 21, "type":0},
        {"weight": 0, "source": 19, "target": 22, "type":0},
        {"weight": 0, "source": 20, "target": 22, "type":0},
        {"weight": 0, "source": 21, "target": 22, "type":0}]
        }
}

def get_topo(name):
    topo = Topology()
    if name == "multidomain_topo":
        topo.set_graph(multidomain_topo["graph"])
    else:
        return "topology not found"
        
    return topo 

class Topology:
    def __init__(self):
        # self.id=ids
        self.graph = {}

    def set_graph(self,graph):
        self.graph = graph


