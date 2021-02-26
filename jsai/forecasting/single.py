# 600秒ごとに交通量が変化する環境で実験を行う

import os
import pickle
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import collections
import random
import statistics
import math
import os, sys
import traci
import pickle


def rulebase():
    car_id = {}
    car_id = defaultdict(list)

    def count_traveltime(id,cycle):
        for i in id:
            # そのIDがリストの中にあるかないかチェック
            if i not in car_id or car_id[i][1] != cycle:
                car_id[i] =[0, cycle]
                
            else:
                car_id[i][0] += 1
            # print(car_id[i])
            # print(car_id[i][0])
    
    def add_car(tf,step,episode):
        x = str(step)
        y = str(episode)
        if tf[0] == 0:
            p = 0.25
        elif tf[0] == 1:
            p = 0.5
        elif tf[0] == 2:
            p = 0.75
        else:
            p = 1

        if tf[1] == 0:
            q = 0.2
        elif tf[1] == 1:
            q = 0.4
        elif tf[1] == 2:
            q = 0.6
        else:
            q = 0.8

        if np.random.uniform(0,1) < p*q*0.5:
            traci.vehicle.addFull(vehID=x + y  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
        if np.random.uniform(0,1) < p*q*0.5:
            traci.vehicle.addFull(vehID=x + y + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
        if np.random.uniform(0,1) < (p-p*q)*0.5:
            traci.vehicle.addFull(vehID=x + y + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
        if np.random.uniform(0,1) < (p-p*q)*0.5:
            traci.vehicle.addFull(vehID=x + y + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   

    def choice_trafficflow():
        a = random.randint(0,3)
        b = random.randint(0,3)
        tf = [a,b]
        return tf

    rewards = []
    travel_time = []
    cycle = 0
    j = 0
    for episode in range(10):
        # traci.start(["sumo-gui", "-c", "single.sumocfg"])
        traci.start(["sumo", "-c", "single.sumocfg"])
        for step in range(3600):
            if step % 600 == 0:
                tf = choice_trafficflow()
            add_car(tf,step,episode)
            # r = reward()
            # rewards.append(r)
            id = traci.vehicle.getIDList()
            # check_car()
            count_traveltime(id,cycle)
            traci.simulationStep()
        if j == 0:
            j += 1
        else:
            a = 0
            b = 1
            for i in car_id:
                if car_id[i][1] == cycle:
                    a += car_id[i][0]
                    b += 1
            traveltime = a / b
            # print(traveltime)
            travel_time.append(traveltime)
            # print(travel_time)
            cycle += 1
        traci.close()
    return travel_time

def reinforcement():
    Qtable = np.zeros((150,150,2,2))
    epsilon = 0.1
    gamma = 0.9
    alpha = 0.1
    xmlfl = "reinforcement.net.xml"
    car_id = {}
    car_id = defaultdict(list)

    def count_traveltime(id,cycle):
        for i in id:
            if i not in car_id or car_id[i][1] != cycle:
                car_id[i] =[0, cycle]
            else:
                car_id[i][0] += 1

    def get_state():
        cars_r_c = traci.edge.getLastStepVehicleNumber("r_c")
        cars_l_c = traci.edge.getLastStepVehicleNumber("l_c")
        cars_t_c = traci.edge.getLastStepVehicleNumber("t_c")
        cars_b_c = traci.edge.getLastStepVehicleNumber("b_c")
        tate = (cars_t_c + cars_b_c)
        yoko = (cars_r_c + cars_l_c)
        phase = traci.trafficlight.getPhase("c")
        if phase < 2:
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

    # def select_action(s):
    #     q = Qtable[s[0]][s[1]][s[2]]
    #     actions = np.where(q == q.max())[0]
    #     return np.random.choice(actions)

    def reward():
        t_c = traci.edge.getLastStepHaltingNumber("t_c")
        r_c = traci.edge.getLastStepHaltingNumber("r_c")
        l_c = traci.edge.getLastStepHaltingNumber("l_c")
        b_c = traci.edge.getLastStepHaltingNumber("b_c")
        r =  -(t_c + r_c + l_c + b_c)/300
        # r =  -(t_c + r_c + l_c + b_c)
        return r

    def state_trans(a):
        phase = traci.trafficlight.getPhase("c")
        if a == 0:
            if phase == 0:
                traci.trafficlight.setPhase("c",0)
            else:
                traci.trafficlight.setPhase("c",3)
        elif a == 1:
            if phase == 2:
                traci.trafficlight.setPhase("c",2)
            else:
                traci.trafficlight.setPhase("c",1)

    def get_Qvalue(s,a):
        return Qtable[s[0]][s[1]][s[2]][a]

    def add_car(tf,step,episode):
        x = str(step)
        y = str(episode)
        if tf[0] == 0:
            p = 0.25
        elif tf[0] == 1:
            p = 0.5
        elif tf[0] == 2:
            p = 0.75
        else:
            p = 1

        if tf[1] == 0:
            q = 0.2
        elif tf[1] == 1:
            q = 0.4
        elif tf[1] == 2:
            q = 0.6
        else:
            q = 0.8

        if np.random.uniform(0,1) < p*q*0.5:
            traci.vehicle.addFull(vehID=x + y  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
        if np.random.uniform(0,1) < p*q*0.5:
            traci.vehicle.addFull(vehID=x + y + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
        if np.random.uniform(0,1) < (p-p*q)*0.5:
            traci.vehicle.addFull(vehID=x + y + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
        if np.random.uniform(0,1) < (p-p*q)*0.5:
            traci.vehicle.addFull(vehID=x + y + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   

    def choice_trafficflow():
        a = random.randint(0,3)
        b = random.randint(0,3)
        tf = [a,b]
        return tf

    os.chdir(os.path.dirname(os.path.abspath(__file__)))    
    rewards = []
    travel_time = []
    heikin = []
    cycle = 0
    a = 0
    phase_before = 0
    num = 0
    for episode in range(50):
        traci.start(["sumo", "-c", "single.sumocfg"]) 
        # traci.start(["sumo-gui", "-c", "single.sumocfg"]) 
        s = get_state()
        for step in range(3600):
            if step % 600 == 0:
                tf = choice_trafficflow()
            id = traci.vehicle.getIDList()
            count_traveltime(id,cycle)
            add_car(tf,step,episode)
            phase = traci.trafficlight.getPhase("c")
            if phase_before == phase:
                if num == 10:
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
                if num == 13:
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
        if episode >=20:
            heikin.append(traveltime)
        travel_time.append(traveltime)
        # print(travel_time)
        cycle += 1
        traci.close()
    return travel_time

# 普段の状態入力に、車両の発生確率を加える
def reinforcement2():
    Qtable = np.zeros((150,150,2,4,4,2))
    epsilon = 0.1
    gamma = 0.9
    alpha = 0.1
    xmlfl = "reinforcement.net.xml"
    car_id = {}
    car_id = defaultdict(list)

    def count_traveltime(id,cycle):
        for i in id:
            if i not in car_id or car_id[i][1] != cycle:
                car_id[i] =[0, cycle]
            else:
                car_id[i][0] += 1

    def get_state(tf):
        cars_r_c = traci.edge.getLastStepVehicleNumber("r_c")
        cars_l_c = traci.edge.getLastStepVehicleNumber("l_c")
        cars_t_c = traci.edge.getLastStepVehicleNumber("t_c")
        cars_b_c = traci.edge.getLastStepVehicleNumber("b_c")
        tate = (cars_t_c + cars_b_c)
        yoko = (cars_r_c + cars_l_c)
        phase = traci.trafficlight.getPhase("c")
        if phase < 2:
            phase = 0
        else:
            phase = 1
        state = [tate,yoko,phase,tf[0],tf[1]]
        return state

    def select_action(s):
        if epsilon < np.random.uniform(0,1):
            # print(s[2])
            q = Qtable[s[0]][s[1]][s[2]][s[3]][s[4]]
            actions = np.where(q == q.max())[0]
            return np.random.choice(actions)
        else:
            return np.random.choice(2)

    # def select_action(s):
    #     q = Qtable[s[0]][s[1]][s[2]]
    #     actions = np.where(q == q.max())[0]
    #     return np.random.choice(actions)

    def reward():
        t_c = traci.edge.getLastStepHaltingNumber("t_c")
        r_c = traci.edge.getLastStepHaltingNumber("r_c")
        l_c = traci.edge.getLastStepHaltingNumber("l_c")
        b_c = traci.edge.getLastStepHaltingNumber("b_c")
        r =  -(t_c + r_c + l_c + b_c)/300
        # r =  -(t_c + r_c + l_c + b_c)
        return r

    def state_trans(a):
        phase = traci.trafficlight.getPhase("c")
        if a == 0:
            if phase == 0:
                traci.trafficlight.setPhase("c",0)
            else:
                traci.trafficlight.setPhase("c",3)
        elif a == 1:
            if phase == 2:
                traci.trafficlight.setPhase("c",2)
            else:
                traci.trafficlight.setPhase("c",1)

    def get_Qvalue(s,a):
        return Qtable[s[0]][s[1]][s[2]][s[3]][s[4]][a]

    def add_car(tf,step,episode):
        x = str(step)
        y = str(episode)
        if tf[0] == 0:
            p = 0.25
        elif tf[0] == 1:
            p = 0.5
        elif tf[0] == 2:
            p = 0.75
        else:
            p = 1

        if tf[1] == 0:
            q = 0.2
        elif tf[1] == 1:
            q = 0.4
        elif tf[1] == 2:
            q = 0.6
        else:
            q = 0.8

        if np.random.uniform(0,1) < p*q*0.5:
            traci.vehicle.addFull(vehID=x + y  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
        if np.random.uniform(0,1) < p*q*0.5:
            traci.vehicle.addFull(vehID=x + y + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
        if np.random.uniform(0,1) < (p-p*q)*0.5:
            traci.vehicle.addFull(vehID=x + y + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
        if np.random.uniform(0,1) < (p-p*q)*0.5:
            traci.vehicle.addFull(vehID=x + y + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   

    def choice_trafficflow():
        a = random.randint(0,3)
        b = random.randint(0,3)
        tf = [a,b]
        return tf

    os.chdir(os.path.dirname(os.path.abspath(__file__)))    
    rewards = []
    travel_time = []
    heikin = []
    cycle = 0
    a = 0
    phase_before = 0
    num = 0
    for episode in range(100):
        # traci.start(["sumo", "-c", "single.sumocfg"]) 
        traci.start(["sumo-gui", "-c", "single.sumocfg"]) 
        tf = choice_trafficflow()
        s = get_state(tf)
        for step in range(3600):
            if step % 600 == 0:
                tf = choice_trafficflow()
            id = traci.vehicle.getIDList()
            count_traveltime(id,cycle)
            add_car(tf,step,episode)
            phase = traci.trafficlight.getPhase("c")
            if phase_before == phase:
                if num == 10:
                    before_s = s
                    s = get_state(tf)
                    before_a = a
                    a = select_action(s)
                    r = reward()
                    Qtable[before_s[0]][before_s[1]][before_s[2]][before_s[3]][before_s[4]][before_a] = (1-alpha)*Qtable[before_s[0]][before_s[1]][before_s[2]][before_s[3]][before_s[4]][before_a] + alpha*(r + gamma*get_Qvalue(s,a))
                    # print(Qtable[before_s[0]][before_s[1]][before_s[2]][before_a])
                    state_trans(a)
                    phase_before = traci.trafficlight.getPhase("c")
                    num = -1
            else:
                if num == 13:
                    before_s = s
                    s = get_state(tf)
                    before_a = a
                    a = select_action(s)
                    r = reward()
                    Qtable[before_s[0]][before_s[1]][before_s[2]][before_s[3]][before_s[4]][before_a] = (1-alpha)*Qtable[before_s[0]][before_s[1]][before_s[2]][before_s[3]][before_s[4]][before_a] + alpha*(r + gamma*get_Qvalue(s,a))
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
        if episode >=20:
            heikin.append(traveltime)
        travel_time.append(traveltime)
        # print(travel_time)
        cycle += 1
        traci.close()
    return travel_time

# reinforcementに、状態入力として、車両数を追加
def reinforcement3():
    Qtable = np.zeros((150,150,150,150,2,2))
    epsilon = 0.1
    gamma = 0.9
    alpha = 0.1
    xmlfl = "reinforcement.net.xml"
    car_id = {}
    car_id = defaultdict(list)

    def count_traveltime(id,cycle):
        for i in id:
            if i not in car_id or car_id[i][1] != cycle:
                car_id[i] =[0, cycle]
            else:
                car_id[i][0] += 1

    def get_state():
        cars_r_c = traci.edge.getLastStepVehicleNumber("r_c")
        cars_l_c = traci.edge.getLastStepVehicleNumber("l_c")
        cars_t_c = traci.edge.getLastStepVehicleNumber("t_c")
        cars_b_c = traci.edge.getLastStepVehicleNumber("b_c")
        r_c = traci.edge.getLastStepHaltingNumber("r_c")
        l_c = traci.edge.getLastStepHaltingNumber("l_c")
        t_c = traci.edge.getLastStepHaltingNumber("t_c")
        b_c = traci.edge.getLastStepHaltingNumber("b_c")
        tate = (cars_t_c + cars_b_c)
        yoko = (cars_r_c + cars_l_c)
        t = (t_c + b_c)
        y = (r_c + l_c)
        phase = traci.trafficlight.getPhase("c")
        if phase < 2:
            phase = 0
        else:
            phase = 1
        state = [tate,yoko,t,y,phase]
        return state

    def select_action(s):
        if epsilon < np.random.uniform(0,1):
            # print(s[2])
            q = Qtable[s[0]][s[1]][s[2]][s[3]][s[4]]
            actions = np.where(q == q.max())[0]
            return np.random.choice(actions)
        else:
            return np.random.choice(2)

    # def select_action(s):
    #     q = Qtable[s[0]][s[1]][s[2]]
    #     actions = np.where(q == q.max())[0]
    #     return np.random.choice(actions)

    def reward():
        t_c = traci.edge.getLastStepHaltingNumber("t_c")
        r_c = traci.edge.getLastStepHaltingNumber("r_c")
        l_c = traci.edge.getLastStepHaltingNumber("l_c")
        b_c = traci.edge.getLastStepHaltingNumber("b_c")
        r =  -(t_c + r_c + l_c + b_c)/300
        # r =  -(t_c + r_c + l_c + b_c)
        return r

    def state_trans(a):
        phase = traci.trafficlight.getPhase("c")
        if a == 0:
            if phase == 0:
                traci.trafficlight.setPhase("c",0)
            else:
                traci.trafficlight.setPhase("c",3)
        elif a == 1:
            if phase == 2:
                traci.trafficlight.setPhase("c",2)
            else:
                traci.trafficlight.setPhase("c",1)

    def get_Qvalue(s,a):
        return Qtable[s[0]][s[1]][s[2]][s[3]][s[4]][a]

    def add_car(tf,step,episode):
        x = str(step)
        y = str(episode)
        if tf[0] == 0:
            p = 0.25
        elif tf[0] == 1:
            p = 0.5
        elif tf[0] == 2:
            p = 0.75
        else:
            p = 1

        if tf[1] == 0:
            q = 0.2
        elif tf[1] == 1:
            q = 0.4
        elif tf[1] == 2:
            q = 0.6
        else:
            q = 0.8

        if np.random.uniform(0,1) < p*q*0.5:
            traci.vehicle.addFull(vehID=x + y  + "tb",routeID="t_b", typeID='DEFAULT_VEHTYPE')
        if np.random.uniform(0,1) < p*q*0.5:
            traci.vehicle.addFull(vehID=x + y + "bt",routeID="b_t", typeID='DEFAULT_VEHTYPE')
        if np.random.uniform(0,1) < (p-p*q)*0.5:
            traci.vehicle.addFull(vehID=x + y + "rl",routeID="r_l", typeID='DEFAULT_VEHTYPE')  
        if np.random.uniform(0,1) < (p-p*q)*0.5:
            traci.vehicle.addFull(vehID=x + y + "lr",routeID="l_r", typeID='DEFAULT_VEHTYPE')   

    def choice_trafficflow():
        a = random.randint(0,3)
        b = random.randint(0,3)
        tf = [a,b]
        return tf

    os.chdir(os.path.dirname(os.path.abspath(__file__)))    
    rewards = []
    travel_time = []
    heikin = []
    cycle = 0
    a = 0
    phase_before = 0
    num = 0
    for episode in range(500):
        traci.start(["sumo", "-c", "single.sumocfg"]) 
        # traci.start(["sumo-gui", "-c", "single.sumocfg"]) 
        s = get_state()
        for step in range(3600):
            if step % 600 == 0:
                tf = choice_trafficflow()
            id = traci.vehicle.getIDList()
            count_traveltime(id,cycle)
            add_car(tf,step,episode)
            phase = traci.trafficlight.getPhase("c")
            if phase_before == phase:
                if num == 10:
                    before_s = s
                    s = get_state()
                    before_a = a
                    a = select_action(s)
                    r = reward()
                    Qtable[before_s[0]][before_s[1]][before_s[2]][before_s[3]][before_s[4]][before_a] = (1-alpha)*Qtable[before_s[0]][before_s[1]][before_s[2]][before_s[3]][before_s[4]][before_a] + alpha*(r + gamma*get_Qvalue(s,a))
                    # print(Qtable[before_s[0]][before_s[1]][before_s[2]][before_a])
                    state_trans(a)
                    phase_before = traci.trafficlight.getPhase("c")
                    num = -1
            else:
                if num == 13:
                    before_s = s
                    s = get_state()
                    before_a = a
                    a = select_action(s)
                    r = reward()
                    Qtable[before_s[0]][before_s[1]][before_s[2]][before_s[3]][before_s[4]][before_a] = (1-alpha)*Qtable[before_s[0]][before_s[1]][before_s[2]][before_s[3]][before_s[4]][before_a] + alpha*(r + gamma*get_Qvalue(s,a))
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
        if episode >=20:
            heikin.append(traveltime)
        travel_time.append(traveltime)
        # print(travel_time)
        cycle += 1
        traci.close()
    return travel_time,Qtable

# rulebase = rulebase()
reinforcement = reinforcement()
# reinforcement2 = reinforcement2()
reinforcement3 = reinforcement3()

f = open("qtable/list.txt","wb")
list_row = reinforcement3[1]
pickle.dump(list_row,f)

p1 = plt.plot(reinforcement)
p2 = plt.plot(reinforcement3[0])
plt.legend((p1[0],p2[0]),("reinforcement","reinforcement3"),loc = 2)
plt.xlabel("episode")
plt.show()


import gym

class SumoEnv(gym.Env):
    def __init__(self):
        ACTION_NUM=4 #アクションの数が3つの場合
        self.action_space = gym.spaces.Discrete(ACTION_NUM) 
        
        #状態の下限と上限
        LOW=[0,0,0,0,0,0,0,0,0,0]
        HIGH=[50,50,50,50,50,50,50,50,1,1]
        self.observation_space = gym.spaces.Box(low=LOW, high=HIGH)

    def reset(self):
        return observation

    def step(self, action_index):
        return observation, reward, done, {}

    def render(self):
        pass