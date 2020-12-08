import os
import pickle
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
import traci
from collections import defaultdict
import pickle

# Qtable = np.zeros((120,50,120,50,8,4))
Qtable = np.zeros((150,150,2,2))
epsilon = 0.1
gamma = 0.9
alpha = 0.1
xmlfl = "reinforcement.net.xml"
car_id = {}
car_id_2 = {}
car_id = defaultdict(list)
car_id_2 = defaultdict(list)

np.set_printoptions(threshold=np.inf)

def count_traveltime(id,cycle):
    for i in id:
        if i not in car_id or car_id[i][1] != cycle:
            car_id[i] =[0, cycle]
            # print(car_id[i])
        else:
            car_id[i][0] += 1
            # print(car_id[i])

def count_traveltime_2(id,cycle):
    for i in id:
        if i not in car_id_2 or car_id_2[i][1] != cycle:
            car_id_2[i] =[0, cycle]
            # print(car_id[i])
        else:
            car_id_2[i][0] += 1
            # print(car_id[i])

def get_state():
    cars_r_c = traci.edge.getLastStepHaltingNumber("r_c")
    # cars_rr_r = traci.edge.getLastStepVehicleNumber("rr_r")
    # cars_r_c_left = traci.lane.getLastStepVehicleNumber("r_c_2")
    # cars_r_c = cars_r_c - cars_r_c_left
    
    cars_l_c = traci.edge.getLastStepHaltingNumber("l_c")
    # cars_ll_l = traci.edge.getLastStepVehicleNumber("ll_l")
    # cars_l_c_left = traci.lane.getLastStepVehicleNumber("l_c_2")
    # cars_l_c = cars_l_c - cars_l_c_left

    cars_t_c = traci.edge.getLastStepHaltingNumber("t_c")
    # cars_tt_t = traci.edge.getLastStepVehicleNumber("tt_t")
    # cars_t_c_left = traci.lane.getLastStepVehicleNumber("t_c_2")
    # cars_t_c = cars_t_c - cars_t_c_left

    cars_b_c = traci.edge.getLastStepHaltingNumber("b_c")
    # cars_bb_b = traci.edge.getLastStepVehicleNumber("bb_b")
    # cars_b_c_left = traci.lane.getLastStepVehicleNumber("b_c_2")
    # cars_b_c = cars_b_c - cars_b_c_left


    # yoko = cars_t_c + cars_tt_t + cars_b_c + cars_bb_b
    # tate = cars_r_c + cars_rr_r + cars_l_c + cars_ll_l
    tate = (cars_t_c + cars_b_c)
    yoko = (cars_r_c + cars_l_c)
    # tate_left = (cars_r_c_left + cars_l_c_left)
    # yoko_left = (cars_t_c_left + cars_b_c_left)
    phase = traci.trafficlight.getPhase("c")
    if phase < 4:
        phase = 0
    else:
        phase = 1

    # state = [tate,tate_left,yoko,yoko_left,phase]
    state = [tate,yoko,phase]
    return state

def select_action(s):
    if epsilon < np.random.rand():
        # print(s[2])
        q = Qtable[s[0]][s[1]][s[2]]
        actions = np.where(q == q.max())[0]
        return np.random.choice(actions)
    else:
        return np.random.choice(2)

def select_greedy_action(s):
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
            # print("1")
        else:
            traci.trafficlight.setPhase("c",5)
            # print("2")
    elif a == 1:
        if phase == 4:
            traci.trafficlight.setPhase("c",4)
            # print("1")
        else:
            traci.trafficlight.setPhase("c",1)
            # print("2")




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
    return Qtable[s[0]][s[1]][s[2]][a]

if __name__ =="__main__":

    # os.chdir(os.path.dirname(os.path.abspath(__file__)))    
    # rewards = []
    # travel_time_2 = []
    # # traci.start(["sumo-gui", "-c", "rulebase.sumocfg"])
    # traci.start(["sumo", "-c", "rulebase.sumocfg"])
    # traci.simulationStep(1000)
    # cycle = 0
    # z = 0
    # for iter in range(10):
    #     for step in range(95):
    #         # r = reward()
    #         # rewards.append(r)
    #         id = traci.vehicle.getIDList()
    #         # check_car()
    #         count_traveltime_2(id,cycle)
    #         traci.simulationStep()

    #     if iter % 10 == 0:
    #         if z == 0:
    #             z += 1
    #         else:
    #             a = 0
    #             b = 1
    #             for i in car_id_2:
    #                 if car_id_2[i][1] == cycle:
    #                     a += car_id_2[i][0]
    #                     b += 1
    #             traveltime = a / b
    #             # print(traveltime)
    #             travel_time_2.append(traveltime)
    #             # travel_time_2[0] = None
    #             # print(travel_time)
    #             cycle += 1
    # traci.close()

    os.chdir(os.path.dirname(os.path.abspath(__file__)))    
    rewards = []
    travel_time = []
    cycle = 0
    traci.start(["sumo", "-c", "reinforcement.sumocfg"]) 
    # traci.start(["sumo-gui", "-c", "reinforcement.sumocfg"]) 
    # traci.simulationStep(2000)
    s = get_state()
    a = 0
    phase_before = 0
    num = 0
    for iter in range(2000):
        for step in range(1000):
            id = traci.vehicle.getIDList()
            count_traveltime(id,cycle)
            phase = traci.trafficlight.getPhase("c")
            # print(num)
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
                if num == 27:
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

    # print("拡張子を除くフォルダ名")
    # folder = input()
    # folder = "./qtable/" + folder + ".txt"
    # f = open(folder,"wb")
    # pickle.dump(Qtable,f)
    #plt.rcParams['font.family'] = "IPAexGothic"
    # for t in Qtable:
    #     print(t)
    # print(Qtable)
    plt.plot(travel_time)
    # p1 = plt.plot(travel_time)
    # p2 = plt.plot(travel_time_2)
    # plt.legend((p1[0], p2[0]), ("reinforcement", "rulebase"), loc=2)
    plt.xlabel("step(×1000)")
    plt.ylabel("travel time")
    plt.show()
    # print(car_id)
