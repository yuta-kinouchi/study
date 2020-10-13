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
xmlfl = "rulebase.net.xml"
car_id = {}

# 交差点に車が入ってきているか確認する関数
def check_car():
    tree = ET.parse(xmlfl)
    tlLogic = tree.find("tlLogic")
    for signal in tlLogic:
        if "0" == signal.attrib["index"]:
            cars_t = traci.edge.getLastStepVehicleNumber("t_c")
            cars_b = traci.edge.getLastStepVehicleNumber("b_c")
            cars = cars_t + cars_b
            if cars == 0:
                traci.trafficlight.setPhase("c",1)
                print("change 1")
        if "4" == signal.attrib["index"]:
            cars_r = traci.edge.getLastStepVehicleNumber("r_c")
            cars_l = traci.edge.getLastStepVehicleNumber("l_c")
            cars = cars_r + cars_l
            if cars == 0:
                traci.trafficlight.setPhase("c",5)
                print("change 5")




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
        

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))    
    rewards = []
    traci.start(["sumo-gui", "-c", "rulebase.sumocfg"])
    for step in range(10000):
        # r = reward()
        # rewards.append(r)
        id = traci.vehicle.getIDList()
        check_car()
        count_traveltime(id)
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