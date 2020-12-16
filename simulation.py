
import random
import time

REPS = 1 #number of repetitions
EPISODES = 1 #number of episodes
WEIGHTS_CHANGE_TIME = 3
SYNC_TIME = 5

class Evento:
    def __init__(self, tipo, inicio, extra, function):
        self.tipo = tipo
        self.inicio = inicio
        self.extra = extra
        self.function = function

    def __str__(self):
        return "("+self.tipo+","+str(self.inicio)+","+str(self.extra)+")"


class Sim:
    def __init__(self):
        self.eventos = []
        self.total_events = 0
        self.horario = 0
        self.run_till = -1

        #metrics
        self.APC = 0 #average path cost
        self.xtime = 0                    

    def set_run_till(self, t):
        self.run_till = t

    def create_event(self, tipo, inicio, extra=None, f=None):
        if inicio<self.horario:
            print("***false")
            return False
        # else:     
        e = Evento(tipo, inicio, extra, f)
        return e

    def binary_search (self, arr, l, r, x):
        if r >= l:       
            mid = int(l + (r - l)/2)
            if arr[mid].inicio == x: 
                return mid
            elif arr[mid].inicio > x: 
                return self.binary_search(arr, l, mid-1, x) 
            else: 
                return self.binary_search(arr, mid+1, r, x)   
        else:             
            return l


    def add_event(self, evt):        
        request = {}
        #encontrar indice y adicionar evt en esa posicion
        index = self.binary_search(self.eventos, 0, len(self.eventos)-1, evt.inicio)
        self.eventos = self.eventos[:index] + [evt] + self.eventos[index:] 



    def print_eventos(self):
        print("HORARIO: ",self.horario,"\nTotal Eventos:",len(self.eventos))
        for i in range(len(self.eventos)): 
            print(self.eventos[i].tipo,self.eventos[i].inicio, end=" > ")
        print("\n")

    def get_proximo_evento(self):
        if len(self.eventos)==0:
            return None
        else:
            p = self.eventos.pop(0)
            self.horario = p.inicio
            return p


    def run(self):
        while self.horario<self.run_till:
            self.print_eventos()
            proximo = self.get_proximo_evento()
            if proximo==None:
                return    

            proximo.function(self,proximo)



def get_state(simulation):    
    state = [0,0,0,0]
    return state

def update_weights(sim, evt): #modify weights in links according to a distribution
    
    #print("change_weights function")
    
    sim.add_event(sim.create_event(tipo="weights_change",inicio=sim.horario+WEIGHTS_CHANGE_TIME, extra={}, f=update_weights))



def synchronize(sim, evt):
    #It is time for syncronization event, controller A will decide which of the other controllers to syncronize with     
    #print("synchronize function")

    if evt.extra["first_state"]:
        #first state index
        print("first_state")
    #    state = get_state(c.substrate,c.simulation)
        
    #    s = translateStateToIndex(state)
    #    a = agente.take_action(s,True)
        s = [0,0,0,0]
        a = 0
        #a = agente.step(state,0)
    else:
        s = evt.extra["current_state"]
        a = evt.extra["action"]
        #print("##agent",agente.last_state," ",agente.last_action)          
    
    evt = sim.create_event(tipo="sync",inicio=sim.horario+SYNC_TIME, extra={"first_state":False,"current_state":s,"action":a}, f=synchronize)    
    sim.add_event(evt)
  
def prepare_sim(sim):
    evt = sim.create_event(tipo="weights_change",inicio=sim.horario+WEIGHTS_CHANGE_TIME,extra={},f=update_weights)
    sim.add_event(evt)

    evt = sim.create_event(tipo="sync",inicio=sim.horario+SYNC_TIME,extra={"first_state":True,},f=synchronize)
    sim.add_event(evt)


                       
def main():                                                                                                                        
        
    APC_rep = []
    xtime_rep = []   
    
    for i in range(EPISODES):
        APC_rep.append([])
        xtime_rep.append([])
    
    for i in range(REPS):

        for j in range(EPISODES):

            print("\n","episode:",j,"\n")       

            simulation = Sim()
            simulation.set_run_till(30)
            prepare_sim(simulation) 
            simulation.run()

            #APC_rep[j].append(controller.APC)
            #xtime_rep[j].append(controller.xtime)

  
        #f = open("results.txt","w+")
        #f.write("Repetition: "+str(i)+"\n")
        #f.write("xtime*:\n")
        #f.write(str(xtime_rep)+"\n\n")
        #f.write("**Reward:\n")
        #f.write(str(APC_rep)+"\n\n")              
        #f.close()

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()









