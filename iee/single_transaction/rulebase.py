import os
import pickle
import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
import traci
from collections import defaultdict

Qtable = np.zeros((150,150,2))
epsilon = 0.1
gamma = 0.9
alpha = 0.1
xmlfl = "rulebase.net.xml"
car_id = {}
car_id = defaultdict(list)
car_id_2 = {}
car_id_2 = defaultdict(list)

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




def count_traveltime(id,cycle):
    for i in id:
        # そのIDがリストの中にあるかないかチェック
        if i not in car_id or car_id[i][1] != cycle:
            car_id[i] =[0, cycle]
            
        else:
            car_id[i][0] += 1
        # print(car_id[i])
        # print(car_id[i][0])

def count_traveltime_2(id,cycle):
    for i in id:
        # そのIDがリストの中にあるかないかチェック
        if i not in car_id_2 or car_id_2[i][1] != cycle:
            car_id_2[i] =[0, cycle]
            
        else:
            car_id_2[i][0] += 1
        # print(car_id[i])
        # print(car_id[i][0])
        

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))    
    rewards = []
    travel_time = []
    # traci.start(["sumo-gui", "-c", "rulebase.sumocfg"])
    traci.start(["sumo", "-c", "rulebase.sumocfg"])
    traci.simulationStep(1000)
    cycle = 0
    j = 0
    for iter in range(500):
        for step in range(475):
            # r = reward()
            # rewards.append(r)
            id = traci.vehicle.getIDList()
            # check_car()
            count_traveltime(id,cycle)
            traci.simulationStep()
        
        if iter % 10 == 0:
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

    rewards_2 = []
    travel_time_2 = []
    # traci.start(["sumo-gui", "-c", "rulebase2.sumocfg"])
    traci.start(["sumo", "-c", "rulebase2.sumocfg"])
    traci.simulationStep(1000)
    cycle = 0
    j = 0
    for iter in range(500):
        for step in range(475):
            # r = reward()
            # rewards.append(r)
            id = traci.vehicle.getIDList()
            # check_car()
            count_traveltime_2(id,cycle)
            traci.simulationStep()
        
        if iter % 10 == 0:
            if j == 0:
                j += 1
            else:
                a = 0
                b = 1
                for i in car_id_2:
                    if car_id_2[i][1] == cycle:
                        a += car_id_2[i][0]
                        b += 1
                traveltime_2 = a / b
                # print(traveltime)
                travel_time_2.append(traveltime_2)
                # print(travel_time)
                cycle += 1
            
    print("1")
    print(len(car_id))
    print("2")
    print(len(car_id_2))
    p1 = plt.plot(travel_time)
    p2 = plt.plot(travel_time_2)
    # Aがボルツマン、Bが等間隔
    plt.legend((p1[0], p2[0]), ("A", "B"), loc=2)
    plt.xlabel("step(×5000)")
    plt.ylabel("travel time")
    plt.show()

    
    # time = sum(car_id.values())
    # number_of_car = len(car_id)
    # travel_time = time / number_of_car
    # print(travel_time)


    # plt.rcParams["font.family"] = "serif"
    # # plt.plot(reward[0])
    # fig = plt.figure(figsize=(8,5))
    # ax = fig.add_subplot(111)
    # ax.plot(rewards)
    # plt.xlabel("episode")
    # plt.ylabel("reward")
    # plt.show()