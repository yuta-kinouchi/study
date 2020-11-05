import os
import pickle
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
import traci
from collections import defaultdict

# Qtable = np.random.rand(-1,0,(300,300,3))
Qtable = np.full((300,300,3),-0.5)
epsilon = 0.1
gamma = 0.9
alpha = 0.1
xmlfl = "reinforcement.net.xml"
car_id = {}
car_id_2 = {}
car_id = defaultdict(list)
car_id_2 = defaultdict(list)

# 車の旅行時間を返す関数
def count_traveltime(id,cycle):
    for i in id:
        # そのIDがリストの中にあるかないかチェック
        if i not in car_id or car_id[i][1] != cycle:
            car_id[i] =[0, cycle]
            
        else:
            car_id[i][0] += 1
        # print(car_id[i])
        
def count_traveltime_2(id,cycle):
    for i in id:
        # そのIDがリストの中にあるかないかチェック
        if i not in car_id_2 or car_id_2[i][1] != cycle:
            car_id_2[i] =[0, cycle]
            
        else:
            car_id_2[i][0] += 1
        # print(car_id[i])
        # print(car_id[i][0])

# 状態を返す
def get_state_4():
    cars_r_c = traci.edge.getLastStepVehicleNumber("r_c")
    # cars_rr_r = traci.edge.getLastStepVehicleNumber("rr_r")
    cars_l_c = traci.edge.getLastStepVehicleNumber("l_c")
    # cars_ll_l = traci.edge.getLastStepVehicleNumber("ll_l")
    cars = cars_r_c + cars_l_c
    return cars
def get_state_9():
    cars_t_c = traci.edge.getLastStepVehicleNumber("t_c")
    # cars_tt_t = traci.edge.getLastStepVehicleNumber("tt_t")
    cars_b_c = traci.edge.getLastStepVehicleNumber("b_c")
    # cars_bb_b = traci.edge.getLastStepVehicleNumber("bb_b")
    cars = cars_t_c + cars_b_c
    return cars

# 得られた状態から行動の選択を行う
def select_action(s_4,s_9):
    if epsilon < np.random.rand():
        q = Qtable[s_4][s_9]
        # print(q)
        actions = np.where(q == q.max())[0]
        # print(actions)
        return np.random.choice(actions)
    else:
        return np.random.choice(3)

# 信号の青時間を取得
def get_signal():
    times = []
    tree = ET.parse(xmlfl)
    tlLogic = tree.find('tlLogic')
    for signal in tlLogic:
        if "0" == signal.attrib["index"]:
            times.append(int(signal.attrib["duration"]))
        elif "5" == signal.attrib["index"]:
            times.append(int(signal.attrib["duration"]))
    # print("time:{0}".format(times))
    return tuple(times)

# 状態遷移を行う　書き換えを行っている
def state_trans(a):
    action = {0: (0, 0), 1: (-1, 1), 2: (1, -1)}
    times_old = tuple(np.array(get_signal()))
    times_new = tuple(np.array(get_signal()) + np.array(action[a]))
    for time in times_new:
        if time < 10:
            # print(times_old)
            return times_old
    tree = ET.parse(xmlfl)
    tlLogic = tree.find('tlLogic')
    i = 0
    for p in tlLogic:
        if "0" == p.attrib["index"] or "5" == p.attrib["index"] :
            p.set("duration", str(times_new[i]))
            i += 1
    tree.write("reinforcement.net.xml", encoding='utf-8')
    # print(times_new)
    return times_new

# 現在の状態、行動
def reward():
    t_c = traci.edge.getLastStepHaltingNumber("t_c")
    if t_c > 60:
        t_c = 1000
        # print("a")
    # print(t_c)
    # tt_t = traci.edge.getLastStepHaltingNumber("tt_t")
    r_c = traci.edge.getLastStepHaltingNumber("r_c")
    if r_c > 60:
        r_c = 1000
    # print(r_c)
    # rr_r = traci.edge.getLastStepHaltingNumber("rr_r")
    l_c = traci.edge.getLastStepHaltingNumber("l_c")
    if l_c > 60:
        l_c = 1000
    # print(l_c)

    # ll_l = traci.edge.getLastStepHaltingNumber("ll_l")
    b_c = traci.edge.getLastStepHaltingNumber("b_c")
    if b_c > 60:
        b_c = 1000
        # print("b")


    # bb_b = traci.edge.getLastStepHaltingNumber("bb_b")
    r =  -(t_c + r_c + l_c + b_c )/150
    # print(r)
    return r

def get_Qvalue(s_4,s_9,a):
    return Qtable[s_4][s_9][a]


if __name__ == "__main__":

    os.chdir(os.path.dirname(os.path.abspath(__file__)))    
    rewards = []
    travel_time_2 = []
    # traci.start(["sumo-gui", "-c", "rulebase.sumocfg"])
    traci.start(["sumo", "-c", "rulebase.sumocfg"])
    traci.simulationStep(10000)
    cycle = 0
    for iter in range(1000):
        for step in range(95):
            # r = reward()
            # rewards.append(r)
            id = traci.vehicle.getIDList()
            # check_car()
            count_traveltime_2(id,cycle)
            traci.simulationStep()

        if iter % 10 == 0:
            a = 0
            b = 1
            for i in car_id_2:
                if car_id_2[i][1] == cycle:
                    a += car_id_2[i][0]
                    b += 1
            traveltime = a / b
            print(traveltime)
            travel_time_2.append(traveltime)
            # travel_time_2[0] = None
            # print(travel_time)
            cycle += 1
    traci.close()

    os.chdir(os.path.dirname(os.path.abspath(__file__)))    
    rewards = []
    travel_time = []
    cycle = 0
    traci.start(["sumo", "-c", "reinforcement.sumocfg"]) 
    # traci.start(["sumo-gui", "-c", "reinforcement.sumocfg"]) 
    s_4 = 0
    s_9 = 0
    a = 0
    r = 0
    traci.simulationStep(1000)
    for iter in range(1000):
        i = 0
        j = 0
        for step in range(95):
            id = traci.vehicle.getIDList()
            count_traveltime(id,cycle)
            phase = traci.trafficlight.getPhase("c")
            signal = get_signal()
            # print(signal)
            if phase == 0:
                time = signal[0] - i
                # print(time)
                traci.trafficlight.setPhaseDuration("c",time)
                i += 1
                # print("action1:{0}".format(a))
            if phase == 4:
                before_s_4 = s_4
                s_4 = get_state_4()
                # print("action4:{0}".format(a))
            if phase == 5:
                time = signal[1] - j
                # print(time)
                traci.trafficlight.setPhaseDuration("c",time)
                j += 1
                # print("action5:{0}".format(a))
            if phase == 9:
                before_s_9 = s_9
                s_9 = get_state_9()
                r = reward()
                # print("action:{0}".format(a))
                # print("reward:{0}".format(r))
                # print("s_4:{0}".format(s_4))
                # print("s_9:{0}".format(s_9))
                Qtable[before_s_4][before_s_9][a] = (1-alpha)*Qtable[before_s_4][before_s_9][a] + alpha*(r + gamma*get_Qvalue(s_4,s_9,select_action(s_4,s_9)))
                a = select_action(s_4,s_9)
                state_trans(a)
                


                # print(s_4)
                # print(s_9)
                # print(select_action(next_s_4,next_s_9))
                #print(r)
            traci.simulationStep()
        
        if iter % 10 == 0:
            c = 0
            d = 1
            for i in car_id:
                if car_id[i][1] == cycle:
                    c += car_id[i][0]
                    d += 1
            traveltime = c / d
            print(traveltime)
            travel_time.append(traveltime)
            # travel_time[0] = None
            # print(travel_time)
            cycle += 1
    traci.close()
    



    print(travel_time)
    #plt.rcParams['font.family'] = "IPAexGothic"
    p1 = plt.plot(travel_time)
    p2 = plt.plot(travel_time_2)
    plt.legend((p1[0], p2[0]), ("reinforcement", "rulebase"), loc=2)
    plt.xlabel("episode")
    plt.ylabel("travel time")
    plt.show()


    # plt.rcParams["font.family"] = "serif"
    # # plt.plot(reward[0])
    # fig = plt.figure(figsize=(8,5))
    # ax = fig.add_subplot(111)
    # ax.plot(rewards)
    # plt.xlabel("episode")
    # plt.ylabel("reward")
    # plt.show()