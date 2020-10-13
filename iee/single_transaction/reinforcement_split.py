import os
import pickle
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
import traci

Qtable = np.zeros((150,150,2))
epsilon = 0.1
gamma = 0.9
alpha = 0.1
xmlfl = "reinforcement.net.xml"
car_id = {}

# 車の旅行時間を返す関数
def count_traveltime(id):
    for i in id:
        # そのIDがリストの中にあるかないかチェック
        if i not in car_id:
            car_id[i] = 0
        else:
            time = car_id[i]
            time += 1
            car_id[i] = time
    return car_id

# 状態を返す
def get_state_4():
    cars_r_c = traci.edge.getLastStepVehicleNumber("r_c")
    cars_rr_r = traci.edge.getLastStepVehicleNumber("rr_r")
    cars_l_c = traci.edge.getLastStepVehicleNumber("l_c")
    cars_ll_l = traci.edge.getLastStepVehicleNumber("ll_l")
    cars = cars_r_c + cars_rr_r + cars_l_c + cars_ll_l
    return cars
def get_state_9():
    cars_t_c = traci.edge.getLastStepVehicleNumber("t_c")
    cars_tt_t = traci.edge.getLastStepVehicleNumber("tt_t")
    cars_b_c = traci.edge.getLastStepVehicleNumber("b_c")
    cars_bb_b = traci.edge.getLastStepVehicleNumber("bb_b")
    cars = cars_t_c + cars_tt_t + cars_b_c + cars_bb_b
    return cars

# 得られた状態から行動の選択を行う
def select_action(s_4,s_9):
    if epsilon < np.random.rand():
        q = Qtable[s_4][s_9]
        actions = np.where(q == q.max())[0]
        return np.random.choice(actions)
    else:
        return np.random.choice()

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
    print("time:{0}".format(times))
    return tuple(times)

# 状態遷移を行う
def state_trans():
    action = {0: (0, 0), 1: (1, -1), 2: (-1, 1)}
    times_old = tuple(np.array(get_signal()))
    times_new = tuple(np.array(get_signal()) + np.array(action[a]))
    for time in times_new:
        if time < 10:
            return times_old
    tree = ET.parse(xmlfl)
    tlLogic = tree.find('tlLogic')
    i = 0
    for p in tlLogic:
        if "0" == p.attrib["index"] or "5" == p.attrib["index"] :
            p.set("duration", str(signal_state[i]))
            i += 1
    tree.write("reinforcement.net.xml", encoding='utf-8')
    return times_new

# 現在の状態、行動
def reward():
    t_c = traci.edge.getLastStepHaltingNumber("t_c")
    tt_t = traci.edge.getLastStepHaltingNumber("tt_t")
    r_c = traci.edge.getLastStepHaltingNumber("r_c")
    rr_r = traci.edge.getLastStepHaltingNumber("rr_r")
    l_c = traci.edge.getLastStepHaltingNumber("l_c")
    ll_l = traci.edge.getLastStepHaltingNumber("ll_l")
    b_c = traci.edge.getLastStepHaltingNumber("b_c")
    bb_b = traci.edge.getLastStepHaltingNumber("bb_b")
    r =  -(t_c + tt_t + r_c + rr_r + l_c + ll_l + b_c + bb_b)
    return r

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))    
    rewards = []
    traci.start(["sumo-gui", "-c", "reinforcement.sumocfg"]) 
    for step in range(10000):
        id = traci.vehicle.getIDList()
        count_traveltime(id)
        phase = traci.trafficlight.getPhase("c")
        if phase == 4:
            s_4 = get_state_4()
        if phase == 9:
            get_signal()
            s_9 = get_state_9()
            a = select_action(s_4,s_9)
            state_trans()
            r = reward()
        traci.simulationStep()


    time = sum(car_id.values())
    number_of_car = len(car_id)
    travel_time = time / number_of_car
    print(travel_time)


    # plt.rcParams["font.family"] = "serif"
    # # plt.plot(reward[0])
    # fig = plt.figure(figsize=(8,5))
    # ax = fig.add_subplot(111)
    # ax.plot(rewards)
    # plt.xlabel("episode")
    # plt.ylabel("reward")
    # plt.show()