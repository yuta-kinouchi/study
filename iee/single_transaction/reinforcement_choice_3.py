import os
import pickle
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
import traci
from collections import defaultdict

Qtable = np.zeros((150,150,2,2))
epsilon = 0.3
gamma = 0.9
alpha = 0.1
xmlfl = "reinforcement.net.xml"
car_id = {}
car_id = defaultdict(list)

def count_traveltime(id,cycle):
    for i in id:
        if i not in car_id or car_id[i][1] != cycle:
            car_id[i] =[0, cycle]
            # print(car_id[i])
        else:
            car_id[i][0] += 1
            # print(car_id[i])

def get_state():
    cars_r_c = traci.edge.getLastStepVehicleNumber("r_c")
    cars_l_c = traci.edge.getLastStepVehicleNumber("l_c")
    cars_t_c = traci.edge.getLastStepVehicleNumber("t_c")
    cars_b_c = traci.edge.getLastStepVehicleNumber("b_c")
    tate = (cars_t_c + cars_b_c)
    yoko = (cars_r_c + cars_l_c)
    phase = traci.trafficlight.getPhase("c")
    if phase < 4:
        phase = 0
    else:
        phase = 1
    state = [tate,yoko,phase]
    return state

def select_action(s):
    if epsilon < np.random.uniform(0,1):
        # print(s[2])
        q = Qtable[s[0]][s[1]][s[2]]
        actions = np.where(q == q.max())[0]
        return np.random.choice(actions)
    else:
        return np.random.choice(2)

def select_action(s):
    q = Qtable[s[0]][s[1]][s[2]]
    actions = np.where(q == q.max())[0]
    return np.random.choice(actions)

def state_trans(a):
    phase = traci.trafficlight.getPhase("c")
    # print("action:{0}".format(a))
    # print("phase:{0}".format(phase))
    if a == 0:
        if phase == 0:
            traci.trafficlight.setPhase("c",0)
        else:
            traci.trafficlight.setPhase("c",6)
    elif a == 1:
        if phase == 4:
            traci.trafficlight.setPhase("c",5)
        else:
            traci.trafficlight.setPhase("c",1)



def reward():
    t_c = traci.edge.getLastStepHaltingNumber("t_c")
    r_c = traci.edge.getLastStepHaltingNumber("r_c")
    l_c = traci.edge.getLastStepHaltingNumber("l_c")
    b_c = traci.edge.getLastStepHaltingNumber("b_c")
    r =  -(t_c + r_c + l_c + b_c)/300
    return r

def get_Qvalue(s,a):
    return Qtable[s[0]][s[1]][s[2]][a]

if __name__ =="__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))    
    rewards = []
    travel_time = []
    cycle = 0
    # traci.start(["sumo", "-c", "reinforcement.sumocfg"]) 
    traci.start(["sumo-gui", "-c", "reinforcement.sumocfg"]) 
    # traci.simulationStep(2000)
    s = get_state()
    a = 0
    phase_before = 0
    num = 0
    for iter in range(200):
        for step in range(1000):
            id = traci.vehicle.getIDList()
            count_traveltime(id,cycle)
            phase = traci.trafficlight.getPhase("c")
            if phase_before == phase:
                if num == 5:
                    before_s = s
                    s = get_state()
                    before_a = a
                    a = select_action(s)
                    r = reward()
                    Qtable[before_s[0]][before_s[1]][before_s[2]][before_a] = (1-alpha)*Qtable[before_s[0]][before_s[1]][before_s[2]][before_a] + alpha*(r + gamma*get_Qvalue(s,a))
                    # print(Qtable[before_s[0]][before_s[1]][before_s[2]][before_a])
                    state_trans(a)
                    phase_before = traci.trafficlight.getPhase("c")
                    num = -1
            else:
                if num == 17:
                    before_s = s
                    s = get_state()
                    before_a = a
                    a = select_action(s)
                    r = reward()
                    Qtable[before_s[0]][before_s[1]][before_s[2]][before_a] = (1-alpha)*Qtable[before_s[0]][before_s[1]][before_s[2]][before_a] + alpha*(r + gamma*get_Qvalue(s,a))
                    # print(Qtable[before_s[0]][before_s[1]][before_s[2]][before_a])
                    state_trans(a)
                    phase_before = traci.trafficlight.getPhase("c")
                    num = -1
            num += 1
            traci.simulationStep()

        c = 0
        b = 1
        for i in car_id:
            if car_id[i][1] == cycle:
                c += car_id[i][0]
                b += 1
        traveltime = c / b
        travel_time.append(traveltime)
        # print(travel_time)
        cycle += 1

    #plt.rcParams['font.family'] = "IPAexGothic"
    # for t in Qtable:
    #     print(t)
    plt.plot(travel_time)
    plt.xlabel("step(×1000)")
    plt.ylabel("travel time")
    plt.show()
    # print(car_id)
