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
xmlfl = "single.net.xml"

def get_state():
    t = traci.edge.getLastStepVehicleNumber("t_c")
    b = traci.edge.getLastStepVehicleNumber("b_c")
    r = traci.edge.getLastStepVehicleNumber("r_c")
    l = traci.edge.getLastStepVehicleNumber("l_c")
    tate = t + b
    yoko = r + l
    state = (tate,yoko)
    return state

def select_action(s):
    if epsilon < np.random.rand():
        q = Qtable[s]
        actions = np.where(q == q.max())[0]
        return np.random.choice(actions)
    else:
        return np.random.choice(2)

def get_signal_state():
    times = []
    tree = ET.parse(xmlfl)
    tlLogic = tree.find('tlLogic')
    for p in tlLogic:
        if "GG" in p.attrib["state"]:
            times.append(int(p.attrib["duration"]))
    """
    timesは交差点で交差する両交通流の青現示時間を表している
    """
    # print(times)
    return tuple(times)

def state_trans(s,a):
    action = {0: (0, 0), 1: (2, -2), 2: (-2, 2)}
    times = tuple(np.array(get_signal_state()) + np.array(action[a]))
    if np.count_nonzero(times) == len(get_signal_state()):
        signal_state = tuple([x for x in times])
    tree = ET.parse(xmlfl)
    tlLogic = tree.find('tlLogic')
    i = 0
    for p in tlLogic:
        if "0" == p.attrib["index"] or "4" == p.attrib["index"] :
            p.set("duration", str(signal_state[i]))
            i += 1

    tree.write("single.net.xml", encoding='utf-8')
    return signal_state

def reward():
    """
    止まっている車の数で報酬を決める
    平均旅行時間で報酬を決めたい
    """
    stops = 0
    ves = traci.vehicle.getIDList()
    for v in ves:
        if traci.vehicle.getSpeed(v) == 0:
            stops += 1
    return -stops
    # stops = 0
    # for step in range(200):
    #     ves = traci.vehicle.getIDList()
    #     for v in ves:
    #         if traci.vehicle.getSpeed(v) == 0:
    #             stops += 1
    #     # traci.simulationStep()
    # # traci.close()
    # return -stops

def get_Qvalue(s,a):
    return Qtable[s][a]


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))    
    rewards = []
    traci.start(["sumo-gui", "-c", "single.sumocfg"])
    for step in range(1000):
        s = get_state()
        print("state:{0}".format(s))
        a = select_action(s)
        print("action:{0}".format(a))
        state_trans(s,a)
        r = reward()
        print("reward:{0}".format(r))
        next_s = get_state()
        next_Qvalue = get_Qvalue(next_s,select_action(next_s))
        print("next:{0}".format(next_Qvalue))
        Qtable[s][a] = (1 - alpha)*Qtable[s][a] + alpha*(r + get_Qvalue(next_s,select_action(next_s)))
        rewards.append(r)
        traci.simulationStep()

    plt.rcParams["font.family"] = "serif"
    # plt.plot(reward[0])
    fig = plt.figure(figsize=(8,5))
    ax = fig.add_subplot(111)
    ax.plot(rewards)
    plt.xlabel("episode")
    plt.ylabel("reward")
    plt.show()
