import os
import pickle
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
import traci
from collections import defaultdict

Qtable = np.zeros((120,50,120,50,8,4))
# Qtable = np.zeros((180,180,4))
epsilon = 0.1
gamma = 0.9
alpha = 0.1
xmlfl = "reinforcement_choice.net.xml"
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
    # cars_rr_r = traci.edge.getLastStepVehicleNumber("rr_r")
    cars_r_c_left = traci.lane.getLastStepVehicleNumber("r_c_2")
    cars_r_c = cars_r_c - cars_r_c_left
    
    cars_l_c = traci.edge.getLastStepVehicleNumber("l_c")
    # cars_ll_l = traci.edge.getLastStepVehicleNumber("ll_l")
    cars_l_c_left = traci.lane.getLastStepVehicleNumber("l_c_2")
    cars_l_c = cars_l_c - cars_l_c_left

    cars_t_c = traci.edge.getLastStepVehicleNumber("t_c")
    # cars_tt_t = traci.edge.getLastStepVehicleNumber("tt_t")
    cars_t_c_left = traci.lane.getLastStepVehicleNumber("t_c_2")
    cars_t_c = cars_t_c - cars_t_c_left

    cars_b_c = traci.edge.getLastStepVehicleNumber("b_c")
    # cars_bb_b = traci.edge.getLastStepVehicleNumber("bb_b")
    cars_b_c_left = traci.lane.getLastStepVehicleNumber("b_c_2")
    cars_b_c = cars_b_c - cars_b_c_left


    # yoko = cars_t_c + cars_tt_t + cars_b_c + cars_bb_b
    # tate = cars_r_c + cars_rr_r + cars_l_c + cars_ll_l
    tate = (cars_t_c + cars_b_c)
    yoko = (cars_r_c + cars_l_c)
    tate_left = (cars_r_c_left + cars_l_c_left)
    yoko_left = (cars_t_c_left + cars_b_c_left)
    phase = traci.trafficlight.getPhase("c")

    state = [tate,tate_left,yoko,yoko_left,phase]
    # state = [tate,yoko]
    return state

def select_action(s):
    if epsilon < np.random.rand():
        q = Qtable[s[0]][s[1]][s[2]][s[3]][s[4]]
        # q = Qtable[s[0]][s[1]]
        actions = np.where(q == q.max())[0]
        return np.random.choice(actions)
    else:
        return np.random.choice(4)

def state_trans(a):
    phase = traci.trafficlight.getPhase("c")
    if a == 0:
        if phase == 0 or phase == 2:
            traci.trafficlight.setPhase("c",0)
        else:
            traci.trafficlight.setPhase("c",7)
    elif a == 1:
        if phase == 0 or phase == 2:
            traci.trafficlight.setPhase("c",2)
        else:
            traci.trafficlight.setPhase("c",1)
    elif a == 2:
        if phase == 4 or phase == 6:
            traci.trafficlight.setPhase("c",4)
        else:
            traci.trafficlight.setPhase("c",3)
    elif a == 3:
        if phase == 4 or phase == 6:
            traci.trafficlight.setPhase("c",6)
        else:
            traci.trafficlight.setPhase("c",5)


def reward():
    t_c = traci.edge.getLastStepHaltingNumber("t_c")
    # tt_t = traci.edge.getLastStepHaltingNumber("tt_t")
    r_c = traci.edge.getLastStepHaltingNumber("r_c")
    # rr_r = traci.edge.getLastStepHaltingNumber("rr_r")
    l_c = traci.edge.getLastStepHaltingNumber("l_c")
    # ll_l = traci.edge.getLastStepHaltingNumber("ll_l")
    b_c = traci.edge.getLastStepHaltingNumber("b_c")
    # bb_b = traci.edge.getLastStepHaltingNumber("bb_b")
    r =  -(t_c + r_c + l_c + b_c)/300
    # r =  -(t_c + tt_t + r_c + rr_r + l_c + ll_l + b_c + bb_b)
    return r

def get_Qvalue(s,a):
    return Qtable[s[0]][s[1]][a]

if __name__ =="__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))    
    rewards = []
    travel_time = []
    cycle = 0
    traci.start(["sumo", "-c", "reinforcement_choice.sumocfg"]) 
    # traci.start(["sumo-gui", "-c", "reinforcement_choice.sumocfg"]) 
    traci.simulationStep(5000)
    s = get_state()
    a = 0
    for iter in range(20):
        for step in range(1000):
            id = traci.vehicle.getIDList()
            count_traveltime(id,cycle)
            if step % 10 == 0:
                before_s = s
                s = get_state()
                before_a = a
                a = select_action(s)
                state_trans(a)
                r = reward()
                Qtable[before_s[0]][before_s[1]][before_a] = (1-alpha)*Qtable[before_s[0]][before_s[1]][before_a] + alpha*(r + gamma*get_Qvalue(s,a))
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

    print(travel_time)
    #plt.rcParams['font.family'] = "IPAexGothic"
    plt.plot(travel_time)
    plt.xlabel("step(×1000)")
    plt.ylabel("travel time")
    plt.show()
    # print(car_id)
